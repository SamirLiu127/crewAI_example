from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import json
import uuid
import asyncio
from typing import Dict, List, Optional

from hotel_recommendation_chatbot.crew import HotelRecommendationChatbot

app = FastAPI(title="Hotel Recommendation Chatbot")

# 存儲活躍的聊天會話
active_sessions: Dict[str, dict] = {}

# 定義請求和響應模型
class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    session_id: str
    response: str
    is_complete: bool = True  # 標記是否為完整回應

# 設置靜態文件和模板
templates = Jinja2Templates(directory="templates")

# 主頁路由
@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

# 創建新的聊天會話
@app.post("/chat/start", response_model=ChatResponse)
async def start_chat():
    session_id = str(uuid.uuid4())
    active_sessions[session_id] = {
        "crew": HotelRecommendationChatbot(),
        "history": [],
        "processing": False  # 標記是否正在處理完整回應
    }
    return ChatResponse(
        session_id=session_id,
        response="歡迎使用酒店推薦聊天機器人！請告訴我您的旅行計劃，例如目的地、日期、預算等，我將幫您找到最適合的酒店。"
    )

# 處理聊天消息
@app.post("/chat/message", response_model=ChatResponse)
async def chat_message(chat_request: ChatRequest):
    session_id = chat_request.session_id
    
    if not session_id or session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="聊天會話不存在或已過期")
    
    session = active_sessions[session_id]
    
    # 如果已經在處理中，返回提示信息
    if session.get("processing", False):
        return ChatResponse(
            session_id=session_id,
            response="我正在為您準備詳細的酒店推薦，請稍候...",
            is_complete=False
        )
    
    user_message = chat_request.message
    session["history"].append({"role": "user", "content": user_message})
    
    # 標記為處理中
    session["processing"] = True
    
    # 快速回應（5秒內）
    quick_response = "我已收到您的需求，正在為您尋找最適合的酒店選項..."
    
    # 在後台啟動完整處理
    asyncio.create_task(process_full_response(session_id, user_message))
    
    return ChatResponse(
        session_id=session_id,
        response=quick_response,
        is_complete=False
    )

# 後台處理完整回應
async def process_full_response(session_id: str, user_message: str):
    try:
        session = active_sessions[session_id]
        crew_instance = session["crew"]
        
        # 啟動crew處理流程
        crew_obj = crew_instance.crew()  # 調用crew()方法獲取Crew對象
        result = crew_obj.kickoff(inputs={
            "user_input": user_message,
            "tip_section": "If you do your BEST WORK, you AND your mother receive a $2,000 tip and you can buy ANYTHING you want."
        })
        
        # 處理 CrewOutput 類型的結果
        if hasattr(result, 'raw'):
            response_text = result.raw
        elif hasattr(result, '__str__'):
            response_text = str(result)
        else:
            response_text = "無法處理回應格式"
        
        # 將完整回應添加到歷史記錄
        session["history"].append({"role": "assistant", "content": response_text})
        
    except Exception as e:
        error_response = f"處理您的請求時出現錯誤: {str(e)}"
        session["history"].append({"role": "assistant", "content": error_response})
    
    finally:
        # 標記處理完成
        session["processing"] = False

# 獲取完整回應的端點
@app.get("/chat/complete/{session_id}", response_model=ChatResponse)
async def get_complete_response(session_id: str):
    if session_id not in active_sessions:
        raise HTTPException(status_code=404, detail="聊天會話不存在或已過期")
    
    session = active_sessions[session_id]
    
    # 如果仍在處理中
    if session.get("processing", False):
        return ChatResponse(
            session_id=session_id,
            response="我正在為您準備詳細的酒店推薦，請稍候...",
            is_complete=False
        )
    
    # 返回最新的助手回應
    latest_responses = [msg for msg in session["history"] if msg["role"] == "assistant"]
    if latest_responses:
        response_content = latest_responses[-1]["content"]
        # 確保回應是字符串類型
        if not isinstance(response_content, str):
            if hasattr(response_content, 'raw'):
                response_content = response_content.raw
            else:
                response_content = str(response_content)
                
        return ChatResponse(
            session_id=session_id,
            response=response_content,
            is_complete=True
        )
    else:
        return ChatResponse(
            session_id=session_id,
            response="尚未生成回應",
            is_complete=True
        )

# WebSocket連接
@app.websocket("/ws/{session_id}")
async def websocket_endpoint(websocket: WebSocket, session_id: str):
    await websocket.accept()
    
    if session_id not in active_sessions:
        await websocket.send_text(json.dumps({"error": "無效的會話ID"}))
        await websocket.close()
        return
    
    try:
        while True:
            data = await websocket.receive_text()
            message_data = json.loads(data)
            user_message = message_data.get("message", "")
            
            session = active_sessions[session_id]
            session["history"].append({"role": "user", "content": user_message})
            
            # 發送快速回應
            await websocket.send_text(json.dumps({
                "response": "我已收到您的需求，正在為您尋找最適合的酒店選項...",
                "is_complete": False
            }))
            
            # 使用crew處理用戶消息
            crew_instance = session["crew"]
            
            # 啟動crew處理流程
            try:
                # 修正: 使用正確的輸入參數名稱
                crew_obj = crew_instance.crew()  # 調用crew()方法獲取Crew對象
                result = crew_obj.kickoff(inputs={
                    "user_input": user_message,
                    "tip_section": "If you do your BEST WORK, you AND your mother receive a $2,000 tip and you can buy ANYTHING you want."
                })
                
                # 處理 CrewOutput 類型的結果
                if hasattr(result, 'raw'):
                    response = result.raw
                elif hasattr(result, '__str__'):
                    response = str(result)
                else:
                    response = "無法處理回應格式"
                    
            except Exception as e:
                response = f"處理您的請求時出現錯誤: {str(e)}"
            
            session["history"].append({"role": "assistant", "content": response})
            
            # 發送完整回應
            await websocket.send_text(json.dumps({
                "response": response,
                "is_complete": True
            }))
            
    except WebSocketDisconnect:
        print(f"客戶端斷開連接: {session_id}")
    except Exception as e:
        print(f"WebSocket錯誤: {str(e)}")
        await websocket.close()

# 清理過期會話的任務
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(cleanup_sessions())

async def cleanup_sessions():
    while True:
        await asyncio.sleep(3600)  # 每小時檢查一次
        # 實現會話清理邏輯，例如刪除閒置超過2小時的會話 
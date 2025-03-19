#!/usr/bin/env python
import uvicorn
from hotel_recommendation_chatbot.api import app

def main():
    """Run the hotel recommendation chatbot API server"""
    print("啟動酒店推薦聊天機器人服務...")
    print("請在瀏覽器中訪問 http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    main() 
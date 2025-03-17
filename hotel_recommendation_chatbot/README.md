# HotelRecommendationChatbot Crew

Welcome to the HotelRecommendationChatbot Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/hotel_recommendation_chatbot/config/agents.yaml` to define your agents
- Modify `src/hotel_recommendation_chatbot/config/tasks.yaml` to define your tasks
- Modify `src/hotel_recommendation_chatbot/crew.py` to add your own logic, tools and specific args
- Modify `src/hotel_recommendation_chatbot/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the hotel_recommendation_chatbot Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The hotel_recommendation_chatbot Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the HotelRecommendationChatbot Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

## Agent 架構說明

本專案使用 crewAI 框架建立了一個酒店推薦聊天機器人，由四個專業 AI 代理組成，各自負責不同的任務：

1. **用戶需求分析師 (User Analyst)**
   - 角色：深入理解用戶的旅行偏好、預算和需求
   - 工具：使用 `hotel_parameters_tools` 查詢酒店參數，如設施類型、地區 ID 等
   - 任務：分析用戶輸入，提取關鍵信息並生成結構化數據

2. **酒店專家 (Hotel Expert)**
   - 角色：根據用戶需求和預算推薦最適合的住宿選項
   - 工具：使用 `hotel_search_tools` 搜索符合條件的酒店
   - 任務：提供 3-5 個最適合的住宿選項

3. **當地探索專家 (Local Explorer)**
   - 角色：推薦住宿地點周邊的景點和活動
   - 工具：使用 `nearby_search_tools` 查詢周邊景點
   - 任務：為每個推薦的住宿提供周邊景點建議

4. **旅行顧問 (Travel Advisor)**
   - 角色：整合所有專家的建議，提供完整的旅遊方案
   - 任務：整合所有信息，生成最終推薦報告

系統採用順序處理流程 (Sequential Process)，代理按照預定順序執行任務，每個代理的輸出作為下一個代理的輸入，形成完整的工作流程：

用戶輸入 → 用戶需求分析 → 酒店搜索 → 周邊景點探索 → 最終推薦報告

這種架構確保了推薦過程的專業性和全面性，為用戶提供量身定制的酒店推薦服務。

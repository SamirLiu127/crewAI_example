#!/usr/bin/env python
import os
import sys
from dotenv import load_dotenv
from hotel_recommendation_chatbot.crew import HotelRecommendationChatbot

load_dotenv()
if os.getenv('LANGTRACE_API_KEY'):
    from langtrace_python_sdk import langtrace
    langtrace.init(api_key = os.getenv('LANGTRACE_API_KEY'))

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'user_input': '台北市兩天一夜,日期為2025-04-12到2025-04-13,3人(兩大一小),預算30000,有親子友善與健身房會更好,目的為家庭旅遊',
        'tip_section': 'If you do your BEST WORK, you AND your mother receive a $2,000 tip and you can buy ANYTHING you want.'
    }
    
    try:
        HotelRecommendationChatbot().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'user_input': '台北市兩天一夜,日期為2025-04-12到2025-04-13,3人(兩大一小),預算30000,有親子友善與健身房會更好,目的為家庭旅遊',
        'tip_section': 'If you do your BEST WORK, you AND your mother receive a $2,000 tip and you can buy ANYTHING you want.'
    }
    try:
        HotelRecommendationChatbot().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        HotelRecommendationChatbot().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'user_input': '台北市兩天一夜,日期為2025-04-12到2025-04-13,3人(兩大一小),預算30000,有親子友善與健身房會更好,目的為家庭旅遊',
        'tip_section': 'If you do your BEST WORK, you AND your mother receive a $2,000 tip and you can buy ANYTHING you want.'
    }
    try:
        HotelRecommendationChatbot().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

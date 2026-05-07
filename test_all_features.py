import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the current directory to sys.path
sys.path.append(os.getcwd())

# Load environment variables
load_dotenv(os.path.join("health_food_agent", ".env"))

from health_food_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

async def run_query(runner, user_id, session_id, query):
    print(f"\nUser: {query}")
    print("Agent: ", end="", flush=True)
    
    user_message = Content(
        role="user",
        parts=[Part(text=query)]
    )
    
    response_text = ""
    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=user_message
    ):
        if event.is_final_response() and event.content and event.content.parts:
            response_text = event.content.parts[0].text
            print(response_text)
    return response_text

async def main():
    APP_NAME = "health_app"
    USER_ID = "tester_007"
    SESSION_ID = "full_test_session"
    
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    await session_service.create_session(app_name=APP_NAME, user_id=USER_ID, session_id=SESSION_ID)
    
    print("Starting Comprehensive Health Agent Test...")
    print("=" * 40)
    
    # 1. Test Calorie Agent
    await run_query(runner, USER_ID, SESSION_ID, "How many calories are in 100g of paneer?")
    
    # 2. Test Recipe Agent
    await run_query(runner, USER_ID, SESSION_ID, "Give me a healthy recipe for chicken.")
    
    # 3. Test Step Agent (Adding)
    await run_query(runner, USER_ID, SESSION_ID, "I just walked 3500 steps, please add them.")
    
    # 4. Test Step Agent (Retrieving)
    await run_query(runner, USER_ID, SESSION_ID, "What is my total step count now?")
    
    # 5. Combined Test
    await run_query(runner, USER_ID, SESSION_ID, "I ate an egg. How many calories does it have and what can I cook with it?")

if __name__ == "__main__":
    asyncio.run(main())

import asyncio
import os
import sys
from dotenv import load_dotenv

# Add the current directory to sys.path so we can import health_food_agent
sys.path.append(os.getcwd())

# Load environment variables
load_dotenv(os.path.join("health_food_agent", ".env"))

from health_food_agent.agent import root_agent
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai.types import Content, Part

async def main():
    # Setup
    APP_NAME = "health_app"
    USER_ID = "test_user"
    SESSION_ID = "session_1"
    
    session_service = InMemorySessionService()
    runner = Runner(
        agent=root_agent,
        app_name=APP_NAME,
        session_service=session_service
    )
    
    # Create session
    await session_service.create_session(
        app_name=APP_NAME,
        user_id=USER_ID,
        session_id=SESSION_ID
    )
    
    print("Health Agent is ready!")
    print("-" * 20)
    
    # Test query
    query = "How many calories are in an apple and what can I cook with it?"
    print(f"User: {query}")
    
    user_message = Content(
        role="user",
        parts=[Part(text=query)]
    )
    
    print("Agent: ", end="", flush=True)
    
    try:
        async for event in runner.run_async(
            user_id=USER_ID,
            session_id=SESSION_ID,
            new_message=user_message
        ):
            if event.is_final_response() and event.content and event.content.parts:
                print(event.content.parts[0].text)
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    asyncio.run(main())

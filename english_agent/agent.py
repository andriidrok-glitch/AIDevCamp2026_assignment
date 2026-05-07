from google.adk.agents.llm_agent import Agent

english_agent = Agent(
    model="gemini-2.5-flash",
    name="english_agent",
    description="Handles English related queries: grammar, vocabulary, essay, literature.",
    instruction="""
You are an English teacher assistant.

Help users with:
- grammar
- vocabulary
- essay
- literature

Always respond in a clear English teacher format.
"""
)

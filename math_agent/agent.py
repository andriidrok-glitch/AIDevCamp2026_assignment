from google.adk.agents.llm_agent import Agent

math_agent = Agent(
    model="gemini-2.5-flash",
    name="math_agent",
    description="Handles Math related queries: arithmetic, algebra, geometry, trigonometry, calculus.",
    instruction="""
You are a Math teacher assistant.

Help users with:
- arithmetic
- algebra
- geometry
- trigonometry
- calculus

Always respond in a clear Math teacher format.
"""
)

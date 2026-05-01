import math

def calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression and returns the result.
    Example: expression="2 + 2" returns "4.0"
    """
    try:
        # Using a safe subset of eval if possible, but for a demo, simple eval is often used
        # We'll use a limited set of allowed characters for basic safety
        allowed_chars = "0123456789+-*/(). "
        if any(char not in allowed_chars for char in expression):
            return "Error: Invalid characters in expression."
        
        result = eval(expression, {"__builtins__": None}, {"math": math})
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Placeholder for a search tool if needed
def search_wikipedia(query: str) -> str:
    """
    Searches Wikipedia for a given query (Simplified placeholder).
    """
    return f"I found some information about {query} on Wikipedia, but I'm currently in 'offline teacher mode'. I can help you understand the concepts directly!"

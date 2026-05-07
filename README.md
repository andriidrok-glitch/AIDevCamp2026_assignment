# School Agent Platform 🏫

A powerful, multi-agent educational platform built using **Google ADK**. The system uses an **Agent-to-Agent (A2A)** architecture where a central Root Agent (the Principal) orchestrates specialized subject teachers.

## 🌟 Key Features
- **Multi-Agent Architecture**: Dedicated platforms for School Subjects and **Health/Nutrition**.
- **Smart Routing**: Root agents identify user intent and delegate to the correct specialist sub-agents.
- **Integrated Tools**: Built-in `calculator` for school tasks and **MCP (Model Context Protocol)** for health data.
- **Real-time Data**: Health agents fetch live nutrition data from Open Food Facts and recipes from TheMealDB.
- **Contextual Memory**: Remembers conversation history for a seamless experience.

## 📂 Project Structure
- `school_agent/`: Root orchestrator agent.
- `math_agent/`: Specialist for Algebra, Geometry, and Calculus.
- `english_agent/`: Specialist for Grammar and Literature.
- `geography_agent/`: Specialist for Maps and Topography.
- `cs_agent/`: Specialist for Programming and Algorithms.
- `health_food_agent/`: Orchestrator for health and nutrition coaching.
- `calorie_agent/`: Specialist for nutrition data via Open Food Facts.
- `recipe_agent/`: Specialist for meal ideas via TheMealDB.
- `step_agent/`: Specialist for tracking daily activity and steps.
- `tools.py`: Utility functions like the calculator.

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Google API Key (Gemini 2.5 Flash supported)

### Installation
1. Activate the virtual environment:
   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```
2. Install dependencies (if not already installed):
   ```powershell
   pip install google-adk
   ```

### Running the Agent
To start the interactive CLI:
```powershell
adk run school_agent
```

To start the Web UI:
```powershell
adk web --port 8000
```

### Testing the Health Agent
You can run the health-specific test scripts:
```powershell
# Run the basic test
python run_health.py

# Run the comprehensive test (all specialists)
python test_all_features.py
```

---
*Built with ❤️ using Google Agent Development Kit.*

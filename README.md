# School Agent Platform 🏫

A powerful, multi-agent educational platform built using **Google ADK**. The system uses an **Agent-to-Agent (A2A)** architecture where a central Root Agent (the Principal) orchestrates specialized subject teachers.

## 🌟 Key Features
- **Multi-Agent Architecture**: Dedicated agents for Math, English, Geography, and Computer Science.
- **Smart Routing**: Root agent identifies the user's intent and delegates to the correct specialist.
- **Integrated Tools**: Built-in `calculator` for complex mathematical expressions.
- **Contextual Memory**: Remembers conversation history for a seamless learning experience.

## 📂 Project Structure
- `school_agent/`: Root orchestrator agent.
- `math_agent/`: Specialist for Algebra, Geometry, and Calculus.
- `english_agent/`: Specialist for Grammar and Literature.
- `geography_agent/`: Specialist for Maps and Topography.
- `cs_agent/`: Specialist for Programming and Algorithms.
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

---
*Built with ❤️ using Google Agent Development Kit.*

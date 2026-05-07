# 🥗 Health Food Agent
A friendly, multi-agent health coaching system built with **Google ADK** and **MCP (Model Context Protocol)**.

## 🌟 Overview
The Health Food Agent acts as a personal health coach that orchestrates three specialized agents to help you manage your diet, discover recipes, and track your fitness progress.

## 🤖 The Agents

### 1. 🍎 Calorie Agent (Nutritionist)
- **Role**: Expert in food energy and nutritional values.
- **Tool**: Uses the `get_calories` tool.
- **Source**: Fetches live data from the **Open Food Facts** API.
- **Capabilities**: Provides calorie estimates per 100g for thousands of food products.

### 2. 👨‍🍳 Recipe Agent (Chef)
- **Role**: Creative cooking assistant.
- **Tool**: Uses the `get_recipe` tool.
- **Source**: Fetches meal ideas from **TheMealDB**.
- **Capabilities**: Suggests recipes based on ingredients or specific cuisines.

### 3. 👟 Step Agent (Fitness Tracker)
- **Role**: Activity and movement monitor.
- **Tool**: Uses the `manage_steps` tool.
- **Source**: Local state management (persistent JSON or session-based).
- **Capabilities**: Can `add`, `get`, and `reset` your daily step count.

## 🛠️ Technology: MCP Tools
This project demonstrates the power of **MCP (Model Context Protocol)**. The sub-agents don't just "chat"—they connect to a specialized `mcp_health_server.py` that handles all external API calls and local storage logic.

## 🚀 How to Run

### Command Line
Navigate to the root and run the test scripts:
```powershell
python run_health.py
```

### Example Queries
- *"How many calories are in a banana?"*
- *"I have some spinach and eggs, what can I cook?"*
- *"I just walked 5000 steps, please record that."*
- *"Show me my total progress for today."*

---
*Developed for the AI Dev Camp 2026 Assignment.*

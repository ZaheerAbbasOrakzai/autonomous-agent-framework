# Autonomous Agent Framework

<div align="center">

![Autonomous Agent Framework Thumbnail](../assets/autonomous_agent_thumbnail.jpg)

[![Author](https://img.shields.io/badge/Author-Zaheer%20Abbas%20Orakzai-indigo.svg?style=for-the-badge&logo=github)](https://github.com/ZaheerAbbasOrakzai)
[![Version](https://img.shields.io/badge/version-2.0.0-blue.svg?style=for-the-badge)](pyproject.toml)
[![UI Engine](https://img.shields.io/badge/UI-Streamlit%20Interactive-ff4b4b.svg?style=for-the-badge&logo=streamlit)](app.py)
[![License](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)

**A Production-Ready, Extensible Framework for Multi-Agent Orchestration, StateGraph Workflows, and Tool Integrations.**

</div>

---

## 🖥️ Interactive Streamlit Physical UI Testbench

Run the interactive dashboard to physically test, inspect, and visualize the multi-agent swarm in real time:

```bash
# Launch interactive Streamlit UI
python -m streamlit run app.py
```

---

## Architecture Overview

**Autonomous Agent Framework** provides robust abstractions for designing, building, and deploying autonomous multi-agent swarms:

```
                    ┌─────────────────┐
                    │ Supervisor Node │
                    └───────┬─────────┘
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │  Researcher  │  │    Writer    │  │   Reviewer   │
  │    Agent     │  │    Agent     │  │    Agent     │
  └──────────────┘  └──────────────┘  └──────────────┘
          │                 │                 │
          └─────────────────┴─────────────────┘
                            │
                            ▼
                    ┌───────────────┐
                    │ Tool Registry │
                    │ (MCP Bridge)  │
                    └───────────────┘
```

---

## Key Features

- **StateGraph Execution Engine**: Directed cyclic & acyclic state graphs with fine-grained checkpointing and node-level transition logic.
- **Dynamic Tool Registry**: Decorator-driven schema reflection (`@tool`) with type validation and MCP compliance.
- **Role-Based Agent Swarms**: Supervisor-Worker architecture for multi-turn collaboration, refinement, and autonomous goal fulfillment.
- **Interactive Visual Inspector**: Real-time Streamlit dashboard showing node execution traces and data mutation states.

---

## Project Structure

```
autonomous-agent-framework/
├── app.py                      # Interactive Streamlit Swarm Inspector UI
├── pyproject.toml              # Modern build specification
├── requirements.txt            # Dependency manifest
├── src/
│   └── agent_framework/
│       ├── __init__.py         # Public exports
│       ├── cli.py              # Framework CLI & swarm simulation runner
│       └── core/
│           ├── engine.py       # StateGraph & GraphState runtime
│           ├── tools.py        # Tool decorators & registry dispatcher
│           └── multi_agent.py  # Supervisor & Worker swarm orchestrator
└── tests/
    └── test_agents.py          # Pytest validation test suite
```

---

## Quick Start

### Installation & CLI Execution

```bash
cd autonomous-agent-framework
pip install -e .

# Run Multi-Agent CLI Demo
python -m src.agent_framework.cli demo

# Run Pytest Suite
pytest tests/
```

---

## Example Usage

```python
from agent_framework import StateGraph, ToolRegistry, tool, MultiAgentSystem

# 1. Register Tools
registry = ToolRegistry()

@tool(name="fetch_data", description="Fetches external database records")
def fetch_data(table_name: str) -> dict:
    return {"status": "ok", "records": [1, 2, 3]}

registry.register(fetch_data)

# 2. Run Swarm
system = MultiAgentSystem()
response = system.execute("Perform market analysis on distributed AI architectures")
print(response["final_data"])
```

---

## Author & License

Developed by **[Zaheer Abbas Orakzai](https://github.com/ZaheerAbbasOrakzai)** under the [MIT License](LICENSE).

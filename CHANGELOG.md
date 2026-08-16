# Changelog - Autonomous Agent Framework

## [2.0.0] - Modernization & Core Engine Overhaul
- **Core Engine**: Implemented `StateGraph` and `GraphState` execution pipeline in `src/agent_framework/core/engine.py`.
- **Dynamic Tool Registry**: Added `@tool` decorator, automatic schema inspection, and registry dispatcher in `src/agent_framework/core/tools.py`.
- **Supervisor-Worker Architecture**: Implemented `SupervisorAgent`, `WorkerAgent`, and `MultiAgentSystem` in `src/agent_framework/core/multi_agent.py`.
- **CLI & Test Suite**: Added `agent_framework.cli` runner and unit test harness in `tests/test_agents.py`.
- **Documentation**: Cleaned up legacy repository references, updated pyproject metadata, and unified module structures.

import pytest
from src.agent_framework.core.engine import StateGraph, GraphState
from src.agent_framework.core.tools import ToolRegistry, tool
from src.agent_framework.core.multi_agent import MultiAgentSystem, WorkerAgent, SupervisorAgent


def test_state_graph_basic():
    graph = StateGraph()
    graph.add_node("step1", lambda s: (s.set("val", s.get("val", 0) + 10), s)[1])
    graph.add_node("step2", lambda s: (s.set("val", s.get("val", 0) * 2), s)[1])
    graph.add_edge("step1", "step2")
    graph.set_entry_point("step1")

    state = graph.run(initial_data={"val": 5})
    assert state.get("val") == 30
    assert len(state.history) == 2


def test_tool_registry():
    registry = ToolRegistry()

    @tool(name="multiply", description="Multiply two numbers")
    def mult(a: int, b: int) -> int:
        return a * b

    registry.register(mult)
    res = registry.execute("multiply", a=6, b=7)
    assert res == 42
    
    tools = registry.list_tools()
    assert len(tools) == 1
    assert tools[0]["name"] == "multiply"


def test_multi_agent_system():
    system = MultiAgentSystem()
    result = system.execute("Build a scalable cloud microservice")
    assert result["success"] is True
    assert "Researcher_output" in result["final_data"]
    assert "Writer_output" in result["final_data"]
    assert "Reviewer_output" in result["final_data"]

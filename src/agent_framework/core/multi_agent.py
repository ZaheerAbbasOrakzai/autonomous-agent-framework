"""
Multi-Agent Orchestration & Role-Based Agent Teams.
"""
from typing import Dict, Any, List, Optional
from .engine import StateGraph, GraphState
from .tools import ToolRegistry


class WorkerAgent:
    """Specialized worker agent capable of specific sub-domain processing."""

    def __init__(self, name: str, role: str, system_prompt: str, tools: Optional[ToolRegistry] = None):
        self.name = name
        self.role = role
        self.system_prompt = system_prompt
        self.tools = tools or ToolRegistry()

    def process(self, state: GraphState) -> GraphState:
        input_query = state.get("query", "")
        # Mock simulated agent reasoning
        state.set(f"{self.name}_output", f"[{self.role}] Completed task for: {input_query}")
        return state


class SupervisorAgent:
    """Supervisory agent that evaluates workflow progress and routes between workers."""

    def __init__(self, name: str = "Supervisor"):
        self.name = name

    def route(self, state: GraphState) -> GraphState:
        phase = state.get("phase", "research")
        if phase == "research":
            state.set("phase", "draft")
            state.next_node = "Researcher"
        elif phase == "draft":
            state.set("phase", "review")
            state.next_node = "Writer"
        elif phase == "review":
            state.set("phase", "done")
            state.next_node = "Reviewer"
        else:
            state.is_terminal = True
        return state


class MultiAgentSystem:
    """Composite system linking Supervisor and Worker nodes into an executable StateGraph."""

    def __init__(self):
        self.graph = StateGraph()
        self.supervisor = SupervisorAgent()
        self.researcher = WorkerAgent("Researcher", "Web & Data Research", "Find factual context.")
        self.writer = WorkerAgent("Writer", "Synthesis & Content", "Draft coherent structured answers.")
        self.reviewer = WorkerAgent("Reviewer", "Quality & Safety", "Validate constraints and accuracy.")

        self._build_graph()

    def _build_graph(self):
        self.graph.add_node("Supervisor", self.supervisor.route)
        self.graph.add_node("Researcher", self.researcher.process)
        self.graph.add_node("Writer", self.writer.process)
        self.graph.add_node("Reviewer", self.reviewer.process)

        self.graph.add_edge("Researcher", "Supervisor")
        self.graph.add_edge("Writer", "Supervisor")
        self.graph.add_edge("Reviewer", "Supervisor")

        self.graph.set_entry_point("Supervisor")

    def execute(self, query: str) -> Dict[str, Any]:
        result = self.graph.run(initial_data={"query": query, "phase": "research"})
        return {
            "query": query,
            "final_data": result.data,
            "history": result.history,
            "success": result.is_terminal or result.get("phase") == "done"
        }

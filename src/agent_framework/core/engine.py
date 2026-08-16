"""
State Graph Engine and Execution Loop for Multi-Agent Workflows.
"""
from typing import Dict, Any, List, Callable, Optional, Union
from dataclasses import dataclass, field


@dataclass
class GraphState:
    """State container passed across agent graph nodes."""
    data: Dict[str, Any] = field(default_factory=dict)
    history: List[Dict[str, Any]] = field(default_factory=list)
    next_node: Optional[str] = None
    is_terminal: bool = False

    def get(self, key: str, default: Any = None) -> Any:
        return self.data.get(key, default)

    def set(self, key: str, value: Any):
        self.data[key] = value

    def append_history(self, node: str, message: str, payload: Any = None):
        self.history.append({"node": node, "message": message, "payload": payload})


class AgentNode:
    """Represents a computational or decision step within a StateGraph."""

    def __init__(self, name: str, handler: Callable[[GraphState], GraphState]):
        self.name = name
        self.handler = handler

    def execute(self, state: GraphState) -> GraphState:
        return self.handler(state)


class StateGraph:
    """Directed state graph runner with conditional transitions."""

    def __init__(self):
        self.nodes: Dict[str, AgentNode] = {}
        self.edges: Dict[str, Dict[str, str]] = {}
        self.entry_point: Optional[str] = None

    def add_node(self, name: str, handler: Callable[[GraphState], GraphState]) -> "StateGraph":
        self.nodes[name] = AgentNode(name, handler)
        return self

    def set_entry_point(self, name: str) -> "StateGraph":
        if name not in self.nodes:
            raise ValueError(f"Node '{name}' must be added before setting as entry point.")
        self.entry_point = name
        return self

    def add_edge(self, from_node: str, to_node: str) -> "StateGraph":
        if from_node not in self.edges:
            self.edges[from_node] = {}
        self.edges[from_node]["default"] = to_node
        return self

    def run(self, initial_data: Optional[Dict[str, Any]] = None, max_steps: int = 50) -> GraphState:
        if not self.entry_point:
            raise ValueError("Entry point has not been configured.")

        state = GraphState(data=initial_data or {})
        current_node_name = self.entry_point
        step_count = 0

        while current_node_name and step_count < max_steps and not state.is_terminal:
            step_count += 1
            node = self.nodes.get(current_node_name)
            if not node:
                break

            state = node.execute(state)
            state.append_history(current_node_name, f"Executed node {current_node_name}")

            # Check for explicit routing in state or transition table
            if state.next_node:
                current_node_name = state.next_node
                state.next_node = None
            elif current_node_name in self.edges:
                current_node_name = self.edges[current_node_name].get("default")
            else:
                break

        return state

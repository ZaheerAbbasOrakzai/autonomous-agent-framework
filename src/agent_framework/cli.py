"""
CLI runner for Autonomous Agent Framework.
"""
import argparse
import sys
from .core.multi_agent import MultiAgentSystem
from .core.tools import ToolRegistry, tool


@tool(name="calculator", description="Performs basic arithmetic calculation")
def calc(expr: str) -> str:
    return str(eval(expr, {"__builtins__": {}}, {}))


def run_demo():
    print("=== Autonomous Agent Framework: Multi-Agent Swarm Demo ===")
    system = MultiAgentSystem()
    query = "Analyze real-time market trends in autonomous AI agents and LangGraph systems."
    print(f"\n[Goal] {query}")
    print("\n--- Starting Execution Loop ---")
    
    res = system.execute(query)
    for h in res["history"]:
        print(f"  * Node [{h['node']}]: {h['message']}")
        
    print("\n--- Final Multi-Agent Output Payload ---")
    for k, v in res["final_data"].items():
        print(f"  {k}: {v}")
    print("\n Multi-Agent Workflow Executed Successfully!")


def main():
    parser = argparse.ArgumentParser(description="Autonomous Agent Framework CLI")
    parser.add_argument("command", choices=["demo", "version"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "demo":
        run_demo()
    elif args.command == "version":
        print("2.0.0")


if __name__ == "__main__":
    main()

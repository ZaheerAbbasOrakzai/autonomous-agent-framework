"""
Tool execution, schema reflection, and MCP bridge for Agent Framework.
"""
from typing import Dict, Any, Callable, List, Optional
import inspect


def tool(name: Optional[str] = None, description: Optional[str] = None):
    """Decorator to register functions as structured agent tools."""
    def decorator(fn: Callable):
        tool_name = name or fn.__name__
        tool_desc = description or fn.__doc__ or "No description provided."
        sig = inspect.signature(fn)
        params = {k: str(v.annotation) for k, v in sig.parameters.items()}
        
        fn._is_tool = True
        fn._tool_name = tool_name
        fn._tool_desc = tool_desc
        fn._tool_params = params
        return fn
    return decorator


class ToolRegistry:
    """Central repository and invocation dispatcher for registered tools."""

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register(self, fn: Callable):
        name = getattr(fn, "_tool_name", fn.__name__)
        self._tools[name] = fn

    def execute(self, tool_name: str, **kwargs) -> Any:
        if tool_name not in self._tools:
            raise KeyError(f"Tool '{tool_name}' is not registered.")
        return self._tools[tool_name](**kwargs)

    def list_tools(self) -> List[Dict[str, Any]]:
        manifest = []
        for name, fn in self._tools.items():
            manifest.append({
                "name": name,
                "description": getattr(fn, "_tool_desc", fn.__doc__ or ""),
                "parameters": getattr(fn, "_tool_params", {}),
            })
        return manifest

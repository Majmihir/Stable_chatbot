from tools.calculator import calculate

def execute_tool(tool_name: str, args: dict):
    if tool_name == "calculate":
        return calculate(args["expression"])
    raise ValueError(f"Unknown tool: {tool_name}")

"""
In this example, we create a simple MCP server using FastMCP that provides basic arithmetic operations
(addition, subtraction, multiplication, division) as tools. Additionally, we define a resource that
returns a greeting message for a given name.

Write any python function as a tool by decorating it with @mcp.tool(). Each tool function can take parameters
and return results. Doc strings are used to document the tools which Agents use to understand the tool's functionality.

The resource function is decorated with @mcp.resource() and can be accessed via a URI pattern.
"""

# Import FastMCP from fastmcp
from fastmcp import FastMCP

# Create an instance of FastMCP. The "mcp" object is important when you call the mcp server via http protocol
# Usuall the url path would be http://localhost:8000/mcp which follows the pattern http://<host>:<port>/<object_name>
# We can give other name as well like app
mcp = FastMCP("Calculator MCP server")

@mcp.tool()
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b    

@mcp.tool()
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b    

@mcp.tool()
def multiply(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b    

@mcp.tool()
def divide(a: float, b: float) -> float:
    """Divide two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

@mcp.resource("greeting://{name}")
def greeting(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

# This block is optional in case someone wants to run the server directly using python command
# when you run this via fastmcp run, this part will be ignored
# and fastmcp will take care of running the server

# To run the server with inspector
# It will install @modelcontextprotocol/inspector. say yes to proceed.
# fastmcp dev calculator_fastmcp.py:mcp

# To directly run the server without inspector, via stdio protocol
# fastmcp run calculator_fastmcp.py:mcp

# To directly run the server without inspector, via streamable http protocol
# fastmcp run calculator_fastmcp.py:mcp -t streamable-http --host 0.0.0.0 --port 8083 

if __name__ == "__main__":
    #mcp.run()
    mcp.run(transport="http", host="0.0.0.0", port=8081)


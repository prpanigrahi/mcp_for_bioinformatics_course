import asyncio
from fastmcp import Client

client = Client("http://localhost:8083/mcp")

async def call_tool(tool_name: str, params: dict):
    async with client:
        result = await client.call_tool(tool_name, params)
        return result

result = asyncio.run(call_tool("add", {"a": 5, "b": 6}))
print(result.structured_content)
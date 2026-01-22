## Build a Calculator MCP server using fastmcp


**Run the server in inspector mode and test it**

Note that this MCP inspector works in stdio mode
```sh
# We can just give calculator_fastmcp.py also if the fastmcp object is named as mcp
fastmcp dev calculator_fastmcp.py:mcp
```

**Run the server via fastmcp run**
```sh
fastmcp run calculator_fastmcp.py:mcp
```
This will run the MCP server via stdio mode. So you can not direclty interact with this. You have to write a single python script where you start the server as subprocess and then connect to that in the same script. 

Alternate approach once your testing is over, run in streamable http mode
as shown below

**Run the server via http protocol**

0.0.0.0 gives access from anywhere. so running a server in windows wsl and u can connect via windows host.

Can give any other number for port

```sh
fastmcp run calculator_fastmcp.py:mcp -t streamable-http --host 0.0.0.0 --port 8081 
```

## Connect to the running MCP server via FastMCP client
```sh
python3 calculator_fastmcp_client.py
```

## Connect to the running MCP server via AI SDK (OpenAI sdk agent)
```sh
python3 calculator_fastmcp_openai_sdk_agent.py
```

## Interact via chatbot with OpenAI SDK agent configured with running MCP server
```sh
python3 calculator_fastmcp_openai_sdk_agent_chatbot.py 
```

## Configure the running server in Claude Desktop

Add below configuation in Claude config json file

```json
{
  "mcpServers": {
    "calculator_mcp": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": [
        "mcp-remote",
        "http://localhost:8081/mcp"
      ]
    }
  }
}

```





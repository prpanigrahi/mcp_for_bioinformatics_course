
# Calculator MCP Server Demo with FastMCP

This tutorial demonstrates how to build, run, and interact with a simple Calculator MCP server using FastMCP. The server exposes basic arithmetic operations (add, subtract, multiply, divide) as tools, and provides a greeting resource. You will learn how to test the server, run it in different modes, and connect to it using multiple clients—including a FastMCP client, an OpenAI SDK agent, and a chatbot interface.

---

## 1. Build and Test the Calculator MCP Server

The server is implemented in `calculator_fastmcp.py` using FastMCP. It exposes arithmetic tools and a greeting resource.

### Inspector Mode (Recommended for Testing)
Inspector mode lets you interactively test your MCP server using stdio protocol:

```sh
fastmcp dev calculator_fastmcp.py:mcp
```

### Stdio Mode (Programmatic Access)
You can also run the server in stdio mode for programmatic access. In this mode, you typically connect to the server from the same Python script. So instead run the server in http mode (see below). We rarely use this.

```sh
fastmcp run calculator_fastmcp.py:mcp
```

### HTTP Mode (Expose as a Web Service)
To make the server accessible over HTTP (e.g., for use with agents or chatbots):

```sh
fastmcp run calculator_fastmcp.py:mcp -t streamable-http --host 0.0.0.0 --port 8081
```
You can use any available port. `0.0.0.0` allows access from your host system (e.g., if running in WSL).

---

## 2. Interacting with the MCP Server

You can connect to the running Calculator MCP server in several ways:

### a) FastMCP Client (Direct Python Client)
Use the provided client script to call tools directly:
```sh
python3 calculator_fastmcp_client.py
```
This script demonstrates how to call the `add` tool via HTTP.

### b) OpenAI SDK Agent (LLM-Powered Agent)
Use the OpenAI SDK agent to interact with the MCP server using natural language:
```sh
python3 calculator_fastmcp_openai_sdk_agent.py
```
This script configures an agent to use the MCP server as a tool provider and answers questions like "what is 5 plus 6?".

### c) Chatbot Interface (Gradio Web UI)
Launch a web-based chatbot that connects to the MCP server via the OpenAI SDK agent:
```sh
python3 calculator_fastmcp_openai_sdk_agent_chatbot.py
```
This provides a chat interface for interactive tool use.

---

## 3. Integrate with Claude Desktop

You can also configure Claude Desktop to use your running Calculator MCP server. Add the following to your Claude config JSON:

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

---

This demo shows the full workflow: building a custom MCP server, testing it, exposing it over HTTP, and connecting to it from multiple clients and agents. Explore the provided scripts for more details and try extending the server with your own tools!


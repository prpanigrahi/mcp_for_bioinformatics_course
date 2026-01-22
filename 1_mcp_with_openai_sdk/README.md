# Using OpenAI SDK Agent with MCP Servers

This section demonstrates how to use the OpenAI SDK Agent to connect to Model Context Protocol (MCP) servers using both stdio and HTTP protocols. Two labs are provided:

---

## Lab 1: Connecting via stdio (Python/Node MCP servers)

In this lab, you'll learn how to:
- Build an agent using the OpenAI SDK Agent framework
- Connect to community MCP servers using the stdio protocol
- Interact with both Python-based (uvx) and Node-based (npx) MCP servers

### Example MCP Servers
- **Time** (Python/uvx): Time and timezone conversion
- **Filesystem** (Node/npx): Secure file operations

### Steps
1. **Import required libraries**: Use dotenv, agents, and MCPServerStdio from the OpenAI SDK Agent package.
2. **Configure the agent**: Set up the agent to use the desired MCP server (e.g., Time or Filesystem).
3. **List available tools**: Query the MCP server for its available tools.
4. **Run queries**: Ask questions such as "What is the current time in Chennai, India?" or interact with the filesystem.
5. **Create a chatbot interface**: Use Gradio to build a simple chat UI for your agent.

### Key Code Concepts
- Use `uvx` for Python-based MCP servers and `npx` for Node-based servers.
- Example fetch parameters for Time server:
	```python
	fetch_params = {"command": "uvx", "args": ["mcp-server-time"]}
	```
- Example fetch parameters for Filesystem server:
	```python
	fetch_params = {"command": "npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/host/path1", "/host/path2"]}
	```

---

## Lab 2: Connecting via HTTP (Uniprot MCP server)

In this lab, you'll learn how to:
- Connect an agent to an MCP server using the streamable HTTP protocol
- Run and interact with a Uniprot MCP server locally
- Build a chat interface for Uniprot queries

### Example MCP Server
- **Uniprot**: Query protein and gene information

### Steps
1. **Set up the Uniprot MCP server**: Clone the repo, install dependencies, and start the server (see notebook for details).
2. **Import required libraries**: Use dotenv, agents, and MCPServerStreamableHttp.
3. **Connect to the server**: Use the HTTP endpoint (e.g., `http://localhost:8787/mcp`).
4. **List available tools**: Query the MCP server for its available tools.
5. **Build a chatbot interface**: Use Gradio to interact with the Uniprot agent.

### Key Code Concepts
- Example connection parameters:
	```python
	async with MCPServerStreamableHttp(params={
			"url": "http://localhost:8787/mcp",
			"timeout": 60,
			"sse_read_timeout": 300,
	}, ... ) as server:
			...
	```
- Example queries:
	- Get Uniprot IDs for gene TP53
	- Describe a specific Uniprot ID (e.g., P04637)

---

These labs provide a hands-on introduction to integrating OpenAI SDK agents with MCP servers using both stdio and HTTP protocols, covering both Python and Node server implementations. See the notebooks for full code and interactive examples.

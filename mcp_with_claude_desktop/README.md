# Integrating Claude Desktop with MCP Servers

This section demonstrates how to connect Claude Desktop (AI assistant) to various Model Context Protocol (MCP) servers using both stdio and HTTP protocols. You will learn how to configure Claude to use community MCP servers for tool-augmented AI workflows.

> **Note:** As of now, Claude Desktop is only supported on Windows. You must install required tools (such as npm, uvx, etc.) on your Windows system and provide their full paths in the configuration when connecting to MCP servers.

---

## Prerequisites

- **Claude Desktop** installed (see [setup.md](../setup.md) for instructions)
- **uvx** (for Python-based MCP servers) and **node.js/npx** (for Node-based MCP servers) installed on Windows
- Refer to [setup.md](../setup.md) in the repo root for detailed installation steps

---

## Lab 3: Connect Claude Desktop to MCP Servers (stdio protocol)

In this lab, you'll learn how to:
- Configure Claude Desktop to connect to MCP servers using the stdio protocol
- Use both Python-based (Time) and Node-based (Filesystem) MCP servers

### Steps
1. **Enable Developer Mode** in Claude Desktop: Go to Help → Enable Developer Mode. This helps to debug. 
2. **Find the path to uvx and npx**:
	 - Open a Windows command prompt and run:
		 ```sh
		 where uvx
		 where npx
		 ```
3. **Edit Claude's config**: Go to Settings → Developer → Edit config.
4. **Add MCP server entries** to the config JSON. Example:
	 ```json
	 {
		 "mcpServers": {
			 "time": {
				 "command": "C:\\Users\\YourUser\\.local\\bin\\uvx.exe",
				 "args": ["mcp-server-time"]
			 },
			 "filesystem": {
				 "command": "C:\\Program Files\\nodejs\\npx.cmd",
				 "args": ["-y", "@modelcontextprotocol/server-filesystem", "C:\\path\\to\\folder"]
			 }
		 }
	 }
	 ```
5. **Restart Claude Desktop** to apply the changes or (Menu → Developer → Reload MCP configuration)

---

## Lab 4: Connect Claude Desktop to MCP Servers (HTTP protocol)

In this lab, you'll learn how to:
- Connect Claude Desktop to an MCP server using the streamable HTTP protocol
- Use the Uniprot MCP server as an example

### Steps
1. **Set up the Uniprot MCP server**: Clone, install, and run the server locally (see notebook for details)
2. **Edit Claude's config**: Add an entry for the Uniprot MCP server using HTTP:
	 ```json
	 {
		 "mcpServers": {
			 "uniprot": {
				 "command": "C:\\Program Files\\nodejs\\npx.cmd",
				 "args": ["mcp-remote", "http://localhost:8787/mcp"]
			 }
		 }
	 }
	 ```
3. **Restart Claude Desktop** to apply the changes

### Example Queries
- Get Uniprot IDs for gene TP53 ("just 5 is enough, only Uniprot IDs")
- Describe in 2 lines about P04637

---

These labs show how to integrate Claude Desktop with both Python and Node-based MCP servers, using both stdio and HTTP protocols. For installation and setup, always refer to the [setup.md](../setup.md) file in the repo root.

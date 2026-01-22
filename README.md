
## MCP for Bioinformatics Course

This course explores practical applications of Model Context Protocol (MCP) in building and integrating AI agents for bioinformatics workflows. Each lab focuses on a specific use case, protocol, or integration method, guiding you from basic concepts to advanced deployment.

---

## Course Topics

### Introduction
- What is MCP?
- Transport modes: stdio and HTTP for client-server communication

### Connecting to MCP from AI SDKs
- **Lab 1:** Use OpenAI SDK agent to connect to an MCP server (stdio protocol)
- **Lab 2:** Use OpenAI SDK agent to connect to an MCP server (streamable HTTP protocol)

### Connecting to MCP from AI Assistants
- **Lab 3:** Use Claude Desktop to connect to an MCP server (stdio protocol)
- **Lab 4:** Use Claude Desktop to connect to an MCP server (streamable HTTP protocol)

### Building and Inspecting MCP Servers
- **Lab 5:**
  - Build and inspect custom MCP servers using the FastMCP package
  - Explore stdio mode and test with mcp-inspector
  - Connect via FastMCP client
  - Integrate with OpenAI SDK agent (non-chat and chat modes)
  - Integrate with Claude Desktop

### NGS Quality Control MCP

In Lab 6, you will build and deploy an MCP server for NGS (Next-Generation Sequencing) quality control. The server uses FastQC to analyze sequencing data, automates report extraction, and parses key quality metrics. This enables streamlined, programmatic QC workflows for bioinformatics pipelines, making it easier to integrate quality checks into larger data analysis systems.

**Use cases:**
- Automate FastQC runs on raw sequencing data
- Extract and parse QC metrics for downstream analysis
- Enable remote or programmatic access to QC tools via MCP and HTTP

### Dockerizing the NGS QC MCP Server

In Lab 7, you will learn how to package your MCP server and all dependencies (including FastQC) into a Docker container. This makes deployment and sharing easy, and ensures reproducibility across environments.

**Use cases:**
- Containerize MCP servers for scalable deployment
- Share ready-to-use bioinformatics tools with collaborators
- Integrate Dockerized MCP servers with AI agents and assistants

---
By the end of this course, you will be able to build, inspect, deploy, and integrate MCP servers for bioinformatics, using both local and containerized environments, and connect them to popular AI agents and assistants.

---
Some advanced use cases will be added soon.
- Differential gene expression analysis MCP server.
- Pathway enrichment MCP server
- FastAPI integration

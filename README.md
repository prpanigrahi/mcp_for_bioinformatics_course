# mcp_for_bioinformatics_course

In this course we explore different topics related to MCP in AI Agents. 

Topics

**Introduction**
- What is MCP
- Two transport mode (stdio, http) for client-server connection

**Connect to MCP server in a AI SDK (OpenAI SDK agent)**
- Lab_1: Use openai sdk agent to use a MCP server (stdio protocol)
- Lab_2: Use openai sdk agent to use a MCP server (streamable http protocol)

**Connect to MCP server in a AI Assistant (Claude Desktop)**
- Lab_3: Use Claude Desktop to use a MCP serve (stdio protocol)
- Lab_4: Use Claude Desktop to use a MCP serve (http protocol)

**Build and inspect MCP server using FastMCP**
- Lab_5: 
  - How to build and inspect custom MCP server using FastMCP package.
  - Learn stdio mode, test using mcp-inspector
  - Connect via FastMCP client
  - Connect via openai sdk agent (nonchat mode, chat mode)
  - Connect via Claude Desktop

## Lab 6: NGS Quality Control MCP

In Lab 6, we will build and use an MCP server for NGS (Next-Generation Sequencing) quality control. The server leverages FastQC to analyze sequencing data files, automates report extraction, and parses key quality metrics. This enables streamlined, programmatic QC workflows for bioinformatics pipelines, making it easier to integrate quality checks into larger data analysis systems.

**Use case:**
- Automate FastQC runs on raw sequencing data
- Extract and parse QC metrics for downstream analysis
- Enable remote or programmatic access to QC tools via MCP and HTTP

- Lab_7: Differential gene expression analysis MCP server.
- Lab_8: Pathway enrichment MCP server

**Advanced Topics: Deploy MCP server**
- Lab_11: Dockerize MCP server
- Lab_12: FastAPI integration

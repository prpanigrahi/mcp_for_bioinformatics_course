## NGS QC MCP Server

This example demonstrates how to build an MCP server using FastMCP to provide quality control tools for NGS data using FastQC. The server exposes four tools for running FastQC, unzipping reports, and parsing FastQC output.

### Tools Provided

1. **run_fastqc**  
  Runs FastQC on a given FASTQ file and saves the report to a specified directory.  
  _Input:_ Path to FASTQ file, output directory. Give WSL paths and not windows since server is running on WSL
  _Output:_ Success/failure message

2. **unzip_fastqc_report**  
  Unzips a FastQC `.zip` report file to a target directory.  
  _Input:_ Path to `.zip` file, extraction directory  
  _Output:_ None (prints extraction status)

3. **parse_basic_statistics**  
  Parses the "Basic Statistics" section from a FastQC report (`fastqc_data.txt`).  
  _Input:_ Path to `fastqc_data.txt`  
  _Output:_ Dictionary of basic statistics

4. **parse_per_base_sequence_quality**  
  Parses the "Per base sequence quality" section from a FastQC report and computes mean/median base quality.  
  _Input:_ Path to `fastqc_data.txt`  
  _Output:_ Dictionary with result, mean, and median base quality

### Usage

- The server is designed to run on WSL (Linux) and exposes the MCP server via HTTP:
  ```sh
  fastmcp run ngs_qc_mcp.py:mcp -t streamable-http --host 0.0.0.0 --port 8082
  ```
- Ensure FastQC is installed and available in your WSL environment.
- When using Claude or other clients, configure them to connect to the MCP server at the HTTP endpoint (e.g., `http://localhost:8082/mcp`).
- Always provide WSL-accessible paths to your FASTQ and report files. e.g /mnt/c/Users/PriyabrataPanigrahi/Downloads/mcp_for_bioinformatics_course/4_build_ngs_qc_mcp_server/1_control_18S_2019_minq7.fastq

**Run the server in inspector mode and test it**

Note that this MCP inspector works in stdio mode
```sh
# We can just give  ngs_qc_mcp.py also if the fastmcp object is named as mcp
fastmcp dev ngs_qc_mcp.py:mcp
```

**Run the server in http protocol**
0.0.0.0 gives access from anywhere. so running a server in windows wsl and u can connect via windows host.

Can give any other number for port

```sh
fastmcp run ngs_qc_mcp.py:mcp -t streamable-http --host 0.0.0.0 --port 8082 
```

## Configure the running server in Claude Desktop

Add below configuation in Claude config json file

```json
{
  "mcpServers": {
    "ngs_qc_mcp": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": [
        "mcp-remote",
        "http://localhost:8082/mcp"
      ]
    }
  }
}

```
Test the server with wsl path for fastq file e.g. /mnt/c/Users/PriyabrataPanigrahi/Downloads/mcp_for_bioinformatics_course/4_build_ngs_qc_mcp_server/1_control_18S_2019_minq7.fastq



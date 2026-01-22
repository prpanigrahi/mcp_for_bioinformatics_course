
# NGS QC MCP Server: Dockerized Quality Control for NGS Data

This project demonstrates how to build and run a Docker container for the NGS QC MCP server. The Docker image includes all necessary dependencies, such as FastQC and Python packages, so you can perform NGS quality control out-of-the-box.

**Key features:**
- Uses `ngs_qc_mcp.py` as the MCP server entry point
- FastQC and all dependencies are pre-installed in the image
- The server runs on port **8083** inside the container
- Host directory is mounted to `/workdir` in the container for easy file access
- Designed for integration with Claude Desktop or any MCP-compatible client

**Workflow overview:**
1. Build the Docker image (all dependencies included)
2. Run the container, mounting your data directory to `/workdir`
3. The MCP server is available at `http://localhost:8083/mcp`
4. Configure Claude Desktop to connect to the running server
5. Use `/workdir/yourfile.fastq` as the file path in requests

---


## Building and Running the Docker Container

### 1. Build the Docker Image

Open a terminal and navigate to the project directory:

```sh
cd /mnt/c/Users/PriyabrataPanigrahi/Downloads/ai/prpanigrahi/git/mcp_for_bioinformatics_course/5_run_mcp_server_as_docker
sudo docker build -t ngsqc_mcp .
```

### 2. Run the Docker Container

To make your data files accessible inside the container, mount the host directory to `/workdir`:

```sh
sudo docker run -p 8083:8083 \
  -v /mnt/c/Users/PriyabrataPanigrahi/Downloads/ai/prpanigrahi/git/mcp_for_bioinformatics_course/5_run_mcp_server_as_docker:/workdir \
  ngsqc_mcp
```

The MCP server will be available at:

**http://localhost:8083/mcp**

### 3. Configure Claude Desktop to Use the MCP Server

Add the following configuration to your Claude Desktop config JSON file to connect to the MCP server:

```json
{
  "mcpServers": {
    "ngs_qc_mcp_docker": {
      "command": "C:\\Program Files\\nodejs\\npx.cmd",
      "args": [
        "mcp-remote",
        "http://localhost:8083/mcp"
      ]
    }
  }
}
```

### 4. File Paths for Data

When specifying file paths in Claude or other clients, use the container's mount path. For example:

```
/workdir/1_control_18S_2019_minq7.fastq
```

This corresponds to the file on your host at:

```
/mnt/c/Users/PriyabrataPanigrahi/Downloads/ai/prpanigrahi/git/mcp_for_bioinformatics_course/5_run_mcp_server_as_docker/1_control_18S_2019_minq7.fastq
```

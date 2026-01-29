# Use an official Python image as the base
FROM python:3.11


# Install Java (required for FastQC) and utilities
RUN apt-get update && \
    apt-get install -y openjdk-21-jre wget unzip && \
    rm -rf /var/lib/apt/lists/*

# Set environment variable for Java
ENV JAVA_HOME=/usr/lib/jvm/java-21-openjdk-amd64

# Install FastQC
RUN wget -O /tmp/fastqc.zip https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.12.1.zip && \
    unzip /tmp/fastqc.zip -d /opt && \
    chmod +x /opt/FastQC/fastqc && \
    ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc && \
    rm /tmp/fastqc.zip

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Run the MCP server in HTTP mode, listening on all interfaces
CMD ["fastmcp", "run", "ngs_qc_mcp.py", "--transport", "http", "--host", "0.0.0.0", "-p", "8083"]

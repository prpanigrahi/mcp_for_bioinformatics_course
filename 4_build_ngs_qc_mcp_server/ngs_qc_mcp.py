# In this example, we create an MCP server using FastMCP that provides tools to run FastQC
# on NGS data files and parse the resulting reports.

# Import FastMCP from fastmcp
from fastmcp import FastMCP

# We will need os and subprocess to run FastQC commands and handle files
import os, subprocess

# We will need zipfile to unzip FastQC report files
import zipfile

# Create an instance of FastMCP. 
# The "mcp" object is important when you call the mcp server via http protocol
# Usually the url path would be http://localhost:8000/mcp which follows the pattern http://<host>:<port>/<object_name>
# We can give other name as well like app
mcp = FastMCP("NGS QC MCP Server")

# Define a tool to run FastQC
# The tool takes an input FASTQ file and an optional output directory
@mcp.tool
def run_fastqc(input_file: str = "1_control_18S_2019_minq7.fastq", output_dir: str = ".") -> str:
    """
    Runs FastQC on the given input file.

    Args:
        input_file: Path to the input FASTQ file.
        output_dir: Directory to save the FastQC report. Defaults to current directory.

    Returns:
        Return code from the FastQC command.
    """
    if not os.path.isfile(input_file):
        return "Input file is not present."
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # On linux calling fastqc is straightforward
    command = ["fastqc", "-o", output_dir, input_file]

    # On windows, we may need to pass explicit path to java and fastqc.bat
    # Here is an example command
    # to run via cmd /c to change directory and run the batch file
    # When you download FastQC, you get a folder named such as fastqc_v0.12.1
    # Inside that folder, there will be a run_fastqc.bat file to run FastQC
    # Open that file and edit the java path explicitely if needed as given below
    # "C:\Program Files\Java\jre1.8.0_481\bin\java.exe" -Xmx250m -classpath .;./sam-1.103.jar;./jbzip2-0.9.jar uk.ac.babraham.FastQC.FastQCApplication %*
    # command = ["cmd", "/c", f"cd /d C:\\Users\\PriyabrataPanigrahi\\Downloads\\fastqc_v0.12.1\\FastQC && run_fastqc.bat {input_file}"]
    result = subprocess.run(command, capture_output=True, text=True)
    
    if result.returncode == 0:
        return f"FastQC completed successfully for {input_file}. Report saved to {output_dir}."
    else:
        return f"FastQC failed for {input_file} with exit code {result.returncode}."

# Define a tool to unzip FastQC report files
@mcp.tool
def unzip_fastqc_report(zip_path: str, extract_to: str = ".") -> None:
    """
    Unzips a FastQC .zip report file. The zip file is created by FastQC after running on an input FASTQ file.
    It will be created in the output directory specified when running FastQC.
    
    Parameters:
        zip_path (str): Path to the FastQC .zip file.
        extract_to (str, optional): Directory to extract files to. If None, extracts to the same directory as the zip file.
    """
    if extract_to is None:
        extract_to = os.path.dirname(zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Extracted {zip_path} to {extract_to}")

# Define a tool to parse Basic Statistics from FastQC report
@mcp.tool
def parse_basic_statistics(fastqc_data_path: str) -> dict:
    fastqc_data_path = fastqc_data_path.strip()
    """
    In the extracted FastQC report folder, there will be a file named fastqc_data.txt
    Parses the 'Basic Statistics' section from this fastqc_data.txt file.
    
    Parameters:
        fastqc_data_path (str): Path to the fastqc_data.txt file.
        
    Returns:
        dict: Dictionary of basic statistics.
    """
    stats = {}
    with open(fastqc_data_path, 'r') as f:
        lines = f.readlines()
    in_section = False
    for line in lines:
        if line.startswith(">>Basic Statistics"):
            in_section = True
            continue
        if in_section:
            if line.startswith(">>END_MODULE"):
                break
            if line.startswith("#") or line.strip() == "":
                continue
            if "\t" in line:
                key, value = line.strip().split("\t", 1)
                stats[key] = value
    return stats

# Define a tool to parse Per Base Sequence Quality from FastQC report
@mcp.tool
def parse_per_base_sequence_quality(fastqc_data_path: str) -> dict:
    fastqc_data_path = fastqc_data_path.strip()
    """
    In the extracted FastQC report folder, there will be a file named fastqc_data.txt
    Parses the 'Per base sequence quality' section from this fastqc_data.txt file and computes overall mean and median base quality.
    
    Parameters:
        fastqc_data_path (str): Path to the fastqc_data.txt file.
    Returns:
        dict: {
            'result': 'pass' or 'fail',
            'mean_base_quality': float,
            'median_base_quality': float
        }
    """
    import statistics
    mean_qualities = []
    median_qualities = []
    result = None
    with open(fastqc_data_path, 'r') as f:
        lines = f.readlines()
    in_section = False
    for line in lines:
        if line.startswith(">>Per base sequence quality"):
            in_section = True
            # The result (pass/fail) is on the same line, after a tab or space
            parts = line.strip().split()
            if len(parts) > 4:
                result = parts[-1]
            elif len(parts) > 1:
                result = parts[1]
            continue
        if in_section:
            if line.startswith(">>END_MODULE"):
                break
            if line.startswith("#") or line.strip() == "":
                continue
            # Table: base_range, mean, median, ...
            cols = line.strip().split()
            if len(cols) >= 3:
                try:
                    mean_qualities.append(float(cols[1]))
                    median_qualities.append(float(cols[2]))
                except ValueError:
                    continue
    mean_base_quality = statistics.mean(mean_qualities) if mean_qualities else None
    median_base_quality = statistics.median(median_qualities) if median_qualities else None
    return {
        "result": result,
        "mean_base_quality": mean_base_quality,
        "median_base_quality": median_base_quality
    }

# Define a tool to parse all module verdicts from FastQC report
@mcp.tool
def parse_all_module_verdicts(fastqc_data_path: str) -> dict:
    fastqc_data_path = fastqc_data_path.strip()
    """
    In the extracted FastQC report folder, there will be a file named fastqc_data.txt
    Parses all module verdicts (pass/warn/fail) from this fastqc_data.txt file.
    Returns a dictionary: {module_name: verdict, ...}
    """
    verdicts = {}
    with open(fastqc_data_path, 'r') as f:
        for line in f:
            if line.startswith(">>") and not line.startswith(">>END_MODULE"):
                # Remove leading '>>', then split by tab or multiple spaces
                line_content = line[2:].strip()
                # Split on two or more spaces or tab
                import re
                parts = re.split(r'\s{2,}|\t', line_content)
                if len(parts) >= 2:
                    module = parts[0].strip()
                    verdict = parts[1].strip()
                    verdicts[module] = verdict
    return verdicts

# This block is optional in case someone wants to run the server directly using python command
# when you run this via fastmcp run, this part will be ignored
# and fastmcp will take care of running the server
if __name__ == "__main__":
    mcp.run()

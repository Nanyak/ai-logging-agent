from langchain.tools import tool
from pathlib import Path
from config import Config
import os

@tool 
def read_log_file(file_name: str) -> str:
    """
    Read contents of a log file from the logs directory.

    Args:
        file_name (str): The name of the log file.


    Returns:
        str: The content of the log file or an error message if reading fails.

    """
    log_path = Path(Config.LOGS_DIRECTORY) / file_name
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Add metadata
            file_size = os.path.getsize(log_path)
            line_count = content.count('\n') + 1
        return f"File: {file_name}\nSize: {file_size} bytes\nLines: {line_count}\n\n{content}"
    except FileNotFoundError:
        return f"Error: Log file '{file_name}' not found in {Config.LOGS_DIRECTORY}."
    except PermissionError:
        return f"Error: Permission denied when trying to read '{file_name}'."
    except Exception as e:
        return f"Error: An unexpected error occurred while reading '{file_name}': {str(e)}"

@tool
def list_log_files() -> str:
    """
    List all available log files in the logs directory.
    
    Returns:
        String containing list of available log files with their sizes
    """
    log_dir = Path(Config.LOGS_DIRECTORY)
    
    if not log_dir.exists():
        return f"Error: Log directory '{Config.LOGS_DIRECTORY}' does not exist"
    
    try:
        log_files = [f for f in log_dir.iterdir() if f.is_file() and f.suffix == '.log']
        
        if not log_files:
            return f"No .log files found in {Config.LOGS_DIRECTORY}/ directory"
        
        result = f"Available log files in {Config.LOGS_DIRECTORY}/:\n\n"
        for log_file in sorted(log_files):
            size = log_file.stat().st_size
            size_kb = size / 1024
            result += f"  - {log_file.name} ({size_kb:.2f} KB)\n"
        
        return result
    
    except Exception as e:
        return f"Error listing log files: {str(e)}"


@tool
def search_logs(filename: str, search_term: str) -> str:
    """
    Search for a specific term in a log file and return matching lines.
    
    Args:
        filename: Name of the log file to search
        search_term: Term to search for (case-insensitive)
    
    Returns:
        String containing matching log lines with line numbers
    """
    log_path = Path(Config.LOGS_DIRECTORY) / filename
    
    try:
        with open(log_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        matches = []
        for line_num, line in enumerate(lines, 1):
            if search_term.lower() in line.lower():
                matches.append(f"Line {line_num}: {line.rstrip()}")
        
        if not matches:
            return f"No matches found for '{search_term}' in {filename}"
        
        result = f"Found {len(matches)} matches for '{search_term}' in {filename}:\n\n"
        result += '\n'.join(matches)
        
        return result
    
    except FileNotFoundError:
        return f"Error: Log file '{filename}' not found in {Config.LOGS_DIRECTORY}."
    except Exception as e:
        return f"Error searching '{filename}': {str(e)}"


def get_log_tools() -> list:
    """
    Get all log-related tools for the agent.
    
    Returns:
        List of tool functions
    """
    return [read_log_file, list_log_files, search_logs]
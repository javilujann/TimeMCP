# server.py
from mcp.server.fastmcp import FastMCP
import time


# Create the MCP server instance
mcp = FastMCP("Example MCP Server")

# Timestamp tool
@mcp.tool()
def getTime() -> float:
    """
    Get the current Unix timestamp.
    
    Returns:
        float: The current time as seconds since January 1, 1970 (Unix epoch).
        This is a standardized way to represent time as a single number.
        Example: 1687302487.654321
    """
    result = time.time()
    return result

# Readable time tool
@mcp.tool()
def readableTime(timestamp: float) -> str:
    """
    Convert a Unix timestamp to a human-readable date and time string.
    
    Args:
        timestamp (float): A Unix timestamp (seconds since epoch) to convert.
            Can be obtained from the getTime() function.
            
    Returns:
        str: A formatted date and time string in the format:
            "Weekday, Day Month Year Hour:Minute:Second"
            Example: "Wednesday, 19 June 2025 15:30:45"
    """
    result = time.strftime("%A, %d %B %Y %H:%M:%S", time.localtime(timestamp))
    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")
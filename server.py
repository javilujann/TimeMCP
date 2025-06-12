# server.py
from mcp.server.fastmcp import FastMCP
import time


# Create the MCP server instance
mcp = FastMCP("Example MCP Server")

# Timestamp tool
@mcp.tool()
def getTime() -> float:
    """returns the current timestamp, seconds since the epoch"""
    result = time.time()
    return result

# Readable time tool
@mcp.tool()
def readableTime(timestamp: float) -> str:
    """returns a human-readable time string for the given timestamp"""
    result = time.strftime("%A, %d %B %Y %H:%M:%S", time.localtime(timestamp))
    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")
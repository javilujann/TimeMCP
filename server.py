# server.py
import logging
from mcp.server.fastmcp import FastMCP
import time
import locale

# Configura locale al español
locale.setlocale(locale.LC_TIME, "es_ES.UTF-8") 

# Configure logging
logging.basicConfig(level=logging.INFO, handlers=[logging.FileHandler('log.txt', encoding='utf-8')])
logger = logging.getLogger(__name__)

# Create the MCP server instance
mcp = FastMCP("Example MCP Server")

# Timestamp tool
@mcp.tool()
def getTime() -> float:
    """devuelve el timestamp actual"""
    result = time.time()
    logger.info(f"Timestamp actual: {result}")
    return result

# Readable time tool
@mcp.tool()
def readableTime(timestamp: float) -> str:
    """Convierte un timestamp en una cadena legible"""
    result = time.strftime("%A %d de %B de %Y %H:%M", time.localtime(timestamp))
    logger.info(f"Readable time for timestamp {timestamp}: {result}")
    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")
from typing import Any
""" 
https://modelcontextprotocol.io/docs/develop/build-server
A simple MCP server that provides weather information using the National Weather Service API.
"""
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP()

# TODO: Implement your MCP server methods here

def main():
    # Initialize and run the server
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
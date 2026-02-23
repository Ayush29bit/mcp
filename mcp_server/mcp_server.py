from mcp.server import FastMCP

mcp = FastMCP("mcp_server")

@mcp.tool()
async def echo(message : str) -> str:
    """Echoes the input message back to the caller."""
    return message

@mcp.prompt()
async def greeting_prompt(name : str) -> str:
    """A simple greeting prompt that takes a name and returns a greeting message."""
    return f"Hello {name} from the greeting prompt!"

@mcp.resource("file://./hello.txt")
def greeting_file() -> str:
    """A simple resource that returns the contents of a text file."""
    with open("hello.txt", "r") as f:
        return f.read()
    
if __name__ == "__main__":
    mcp.run(transport = "stdio")
# Model Context Protocol

A minimal **Model Context Protocol (MCP)** implementation demonstrating:

- ✅ Custom MCP server using `FastMCP`
- ✅ Stdio-based client–server communication
- ✅ Tool, Prompt, and Resource registration
- ✅ Async client session handling
- ✅ Clean modular project structure

---

## 📦 Project Structure

MCP/
│
├── mcp_server/
│ └── mcp_server.py # MCP server definition
│
├── mcp_client/
│ ├── init.py
│ ├── main.py # Client entry point
│ ├── mcp_client.py # Client session manager
│ ├── cli.py
│ ├── chat.py
│ └── handlers.py

### Server Responsibilities
- Expose tools
- Provide prompt templates
- Serve resources
- Handle MCP protocol

### Client Responsibilities
- Spawn server process
- Establish stdio connection
- Initialize MCP session
- Call tools / prompts / resources
  
---

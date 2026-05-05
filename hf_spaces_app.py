"""
Hugging Face Spaces App for AI Voice Clone MCP Server
Provides both MCP endpoint and web UI
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import os

app = FastAPI(title="AI Voice Clone MCP Server")

@app.get("/")
async def root():
    """Web UI homepage"""
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Voice Clone MCP Server</title>
        <style>
            body { font-family: sans-serif; max-width: 800px; margin: 40px auto; padding: 20px; }
            h1 { color: #333; }
            .badge { background: #10b981; color: white; padding: 4px 8px; border-radius: 4px; font-size: 12px; }
            .endpoint { background: #f3f4f6; padding: 10px; border-radius: 4px; margin: 10px 0; }
        </style>
    </head>
    <body>
        <h1>🎙️ AI Voice Clone MCP Server</h1>
        <p><span class="badge">MCP Server</span> <span class="badge">Hugging Face Spaces</span></p>
        
        <h2>🚀 How to Use</h2>
        <p>Add this MCP server to your AI client (Claude Desktop, Cursor, VS Code):</p>
        
        <div class="endpoint">
            <strong>MCP Endpoint:</strong><br>
            <code>http://localhost:8000/mcp</code> (if running locally)<br>
            Or connect via stdio transport
        </div>
        
        <h2>🎯 Available Tools</h2>
        <ul>
            <li><strong>clone_voice</strong> - Clone voice from audio sample (10-30s)</li>
            <li><strong>synthesize_speech</strong> - Generate speech with cloned voice</li>
            <li><strong>list_voices</strong> - List available voice models</li>
            <li><strong>get_supported_languages</strong> - Show supported languages</li>
        </ul>
        
        <h2>📊 MCP Configuration</h2>
        <pre>
{
  "mcpServers": {
    "ai-voice-clone": {
      "command": "python",
      "args": ["mcp_server.py"],
      "env": {}
    }
  }
}
        </pre>
        
        <p><a href="https://github.com/my-ai-stack/ai-voice-clone">View on GitHub</a> | 
           <a href="https://huggingface.co/spaces/my-ai-stack/ai-voice-clone">Hugging Face Space</a></p>
    </body>
    </html>
    """
    return HTMLResponse(content=html, media_type="text/html")

@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy", "service": "ai-voice-clone-mcp"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 7860))
    uvicorn.run(app, host="0.0.0.0", port=port)



from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
import json

app = FastAPI()

@app.post("/mcp")
async def mcp_handler(request: Request):
    payload = await request.json()

    user_input = payload.get("input", {}).get("body", "")
    bot_response = payload.get("output", {}).get("body", "")

    print("📥 User Prompt:", user_input)
    print("📤 Copilot Response:", bot_response)

    return JSONResponse({
        "status": "success",
        "message": "MCP server received and logged the interaction",
    })

if __name__ == "__main__":
    print("🚀 Starting MCP Server (HTTP)")
    uvicorn.run(app, host="0.0.0.0", port=8503)

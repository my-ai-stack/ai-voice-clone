---
title: AI Voice Clone MCP Server
emoji: 🎙️
colorFrom: blue
sdk: docker
app_port: 7860
license: mit
---

FROM python:3.10-slim

WORKDIR /app

# Copy requirements
COPY requirements-mcp.txt ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements-mcp.txt

# Copy all files
COPY . .

# Expose port for Hugging Face Spaces
EXPOSE 7860

# Run the HF Spaces app
CMD ["python", "hf_spaces_app.py"]

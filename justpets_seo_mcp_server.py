
from fastapi import FastAPI, Request
from fastmcp import FastMCP

app = FastAPI()
mcp = FastMCP(app)


# Tool: Add keywords to a list (simulate keyword tracking system)
@mcp.tool
def track_keyword(keyword: str, category: str = "general") -> dict:
    """Track a new keyword under a category."""
    return {"status": "tracked", "keyword": keyword, "category": category}

# Tool: Return dummy rankings for a keyword
@mcp.tool
def get_keyword_ranking(keyword: str) -> dict:
    """Return a fake SEO ranking for a keyword."""
    mock_rank = {
        "justpets": 3,
        "pet food": 7,
        "organic dog food": 1
    }
    rank = mock_rank.get(keyword.lower(), 99)
    return {"keyword": keyword, "rank": rank}

# Handle /mcp endpoint
@app.post("/mcp")
async def handle_mcp(request: Request):
    return await mcp.handle(await request.json())

@app.get("/")
def root():
    return {"message": "JustPets SEO MCP Server is live"}

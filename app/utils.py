import httpx
import os

async def search_stackoverflow(error_message: str):
    query = error_message.replace(" ", "+")
    url = f"https://api.stackexchange.com/2.3/search/advanced?order=desc&sort=relevance&q={query}&site=stackoverflow"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


# GitHub Issue Fetcher
async def search_github_issues(error_message: str):
    import httpx
    headers = {"Accept": "application/vnd.github+json"}
    query = error_message.replace(" ", "+")
    url = f"https://api.github.com/search/issues?q={query}+in:title+state:open"
    async with httpx.AsyncClient() as client:
        resp = await client.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.json()
        else:
            return {"error": "GitHub API rate limit or failure."}

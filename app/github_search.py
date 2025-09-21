import os
import requests

def search_github_issues(error_message: str):
    query = error_message.split("\n")[0][:100]
    headers = {}
    token = os.getenv("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"token {token}"

    url = f"https://api.github.com/search/issues?q={query}+type:issue"
    try:
        response = requests.get(url, headers=headers, timeout=8)
        data = response.json()
        return [
            {
                "title": item["title"],
                "url": item["html_url"]
            }
            for item in data.get("items", [])[:3]
        ]
    except Exception as e:
        return [{"error": f"GitHub search failed: {str(e)}"}]

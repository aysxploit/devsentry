import pytest
import asyncio
from app.utils import search_stackoverflow, search_github_issues

@pytest.mark.asyncio
async def test_stackoverflow_api():
    res = await search_stackoverflow("TypeError")
    assert "items" in res

@pytest.mark.asyncio
async def test_github_api():
    res = await search_github_issues("TypeError")
    assert "items" in res or "error" in res

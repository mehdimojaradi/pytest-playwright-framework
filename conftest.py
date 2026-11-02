import pytest
import json
from pathlib import Path
from playwright.async_api import async_playwright

@pytest.fixture(scope="function")
async def page(selector):
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(selector.get("base_url"))
        yield page
        await browser.close()
        
@pytest.fixture(scope="function")
async def selector():
    current_dir = Path(__file__).parent
    selectors_file = current_dir / "fixtures" / "selectors.json"
    
    with open(selectors_file) as f:
        selectors = json.load(f)
        
    return selectors

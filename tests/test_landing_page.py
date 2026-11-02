import pytest
from playwright.async_api import expect
from pages import Landing


class TestLandingPage:
    @pytest.fixture(autouse=True)
    async def setup_method(self, page, selector):
        self.page = page
        self.selector = selector
        self.landing_page = Landing(self.page, self.selector)

    async def test_verify_page_title(self):
        await expect(self.page).to_have_title(self.selector.get("title"))

    async def test_verify_logo(self):
        logo_element = self.landing_page.logo()
        await expect(logo_element).to_be_visible()
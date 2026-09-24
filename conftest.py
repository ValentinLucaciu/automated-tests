import pytest
from playwright.sync_api import Browser, Page, BrowserContext

@pytest.fixture(scope="function")
def context(browser: Browser):
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080},
        ignore_https_errors=True
    )
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context: BrowserContext):
    browser_page = context.new_page()
    yield browser_page
    browser_page.close()

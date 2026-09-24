from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_block_images_for_fast_execution(page: Page) -> None:
    """Verifies that the application functions properly even when image requests are blocked."""
    page.route("**/*.{png,jpg,jpeg,gif,svg}", lambda route: route.abort())

    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_mock_failed_api_response(page: Page) -> None:
    """Simulates a server HTTP 500 error on critical network calls."""
    def handle(route):
        route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error": "Internal Server Error"}'
        )

    page.route("**/service-worker.js", handle)

    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
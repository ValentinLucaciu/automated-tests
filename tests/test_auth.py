from playwright.sync_api import Page, expect
from pages.login_page import LoginPage

def test_successful_login(page: Page) -> None:
    """Verifies that a valid user can log in successfully."""
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_login_with_invalid_credentials(page: Page) -> None:
    """Verifies error message display on invalid login."""
    login_page = LoginPage(page)
    login_page.load()
    login_page.login("invalid_user", "wrong_password")

    expect(login_page.error_message).to_be_visible()
    expect(login_page.error_message).to_contain_text("Username and password do not match")
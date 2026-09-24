from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class LoginPage(BasePage):
    """Page Object for the SauceDemo Login Page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.username_input: Locator = page.locator("[data-test='username']")
        self.password_input: Locator = page.locator("[data-test='password']")
        self.login_button: Locator = page.locator("[data-test='login-button']")
        self.error_message: Locator = page.locator("[data-test='error']")

    def load(self) -> None:
        """Navigates to the login page."""
        self.navigate_to()

    def login(self, username: str, password: str) -> None:
        """Fills login credentials and submits the form."""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
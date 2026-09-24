from playwright.sync_api import Page

class BasePage:
    """Base Class representing shared actions and properties across all Page Objects."""

    def __init__(self, page: Page) -> None:
        self.page = page
        self.base_url = "https://www.saucedemo.com"

    def navigate_to(self, relative_path: str = "") -> None:
        """Navigates to a specific path relative to the base URL."""
        target_url = f"{self.base_url}/{relative_path}".rstrip("/")
        self.page.goto(target_url)

    def get_current_url(self) -> str:
        """Returns the current page URL."""
        return self.page.url

    def get_page_title(self) -> str:
        """Returns the title of the active browser page."""
        return self.page.title()
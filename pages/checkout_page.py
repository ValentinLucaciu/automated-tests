from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    """Page object for the checkout page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.first_name_input: Locator = page.locator("[data-test='firstName']")
        self.last_name_input: Locator = page.locator("[data-test='lastName']")
        self.postal_code_input: Locator = page.locator("[data-test='postalCode']")
        self.continue_button: Locator = page.locator("[data-test='continue']")

        self.finish_button: Locator = page.locator("[data-test='finish']")

        self.complete_header: Locator = page.locator("[data-test='complete-header']")

    def fill_information(self, first_name: str, last_name: str, postal_code: str) -> None:
        """Fills shipping information and proceeds to order summary."""
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.postal_code_input.fill(postal_code)
        self.continue_button.click()

    def finish_checkout(self) -> None:
        """Completes the checkout process."""
        self.finish_button.click()
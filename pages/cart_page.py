from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class CartPage(BasePage):
    """Page object for the cart page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.cart_item_name: Locator = page.locator("[data-test='inventory-item-name']")
        self.checkout_button: Locator = page.locator("[data-test='checkout']")

    def click_checkout(self) -> None:
        self.checkout_button.click()
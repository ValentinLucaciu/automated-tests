from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class InventoryPage(BasePage):
    """Page Object for the SauceDemo Inventory/Dashboard Page."""

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.title: Locator = page.locator("[data-test='title']")
        self.inventory_items: Locator = page.locator("[data-test='inventory-item']")
        self.add_backpack_button: Locator = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.cart_badge: Locator = page.locator("[data-test='shopping-cart-badge']")

    def add_backpack_to_cart(self) -> None:
        """Adds the Sauce Labs Backpack to the shopping cart."""
        self.add_backpack_button.click()

    def get_cart_badge_count(self) -> str:
        """Returns the current items count displayed on the cart badge."""
        return self.cart_badge.inner_text()
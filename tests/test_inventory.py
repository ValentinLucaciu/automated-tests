from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_add_item_to_cart(page: Page) -> None:
    """Verifies that adding an item updates the cart badge count."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()

    expect(inventory_page.cart_badge).to_have_text("1")
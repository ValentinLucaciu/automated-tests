from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def test_complete_checkout_flow(page: Page) -> None:
    """Verifies the complete checkout flow from login to order confirmation."""
    login_page = LoginPage(page)
    inventory_page = InventoryPage(page)
    cart_page = CartPage(page)
    checkout_page = CheckoutPage(page)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page.add_backpack_to_cart()
    inventory_page.cart_badge.click()

    expect(cart_page.cart_item_name).to_have_text("Sauce Labs Backpack")
    cart_page.click_checkout()

    checkout_page.fill_information("QA", "Tester", "12345")

    checkout_page.finish_checkout()

    expect(checkout_page.complete_header).to_have_text("Thank you for your order!")
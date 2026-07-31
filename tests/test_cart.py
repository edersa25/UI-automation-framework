import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.regression
@pytest.mark.cart
def test_add_backpack_to_cart(page: Page, website_url):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate(website_url)

    login_page.login(
        "standard_user",
        "secret_sauce",
    )

    products_page.add_backpack_to_cart()

    expect(products_page.cart_badge).to_have_text("1")

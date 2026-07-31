import pytest
from playwright.sync_api import Page, expect

from data.login_data import VALID_USER
from pages.login_page import LoginPage
from pages.products_page import ProductsPage


@pytest.mark.smoke
@pytest.mark.login
def test_successful_login(page: Page, website_url):
    login_page = LoginPage(page)
    products_page = ProductsPage(page)

    login_page.navigate(website_url)

    login_page.login(
        VALID_USER["username"],
        VALID_USER["password"],
    )

    expect(products_page.page_title).to_have_text("Products")
    expect(products_page.inventory_list).to_be_visible()

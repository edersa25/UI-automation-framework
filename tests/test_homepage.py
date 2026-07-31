import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.smoke
def test_homepage_title(page: Page, website_url):
    login_page = LoginPage(page)

    login_page.navigate(website_url)

    expect(page).to_have_title("Swag Labs")

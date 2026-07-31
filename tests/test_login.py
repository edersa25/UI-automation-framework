import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.login
def test_login_page_has_fields(page: Page, website_url):
    login_page = LoginPage(page)

    login_page.navigate(website_url)

    expect(login_page.username_input).to_be_visible()
    expect(login_page.password_input).to_be_visible()
    expect(login_page.login_button).to_be_visible()


@pytest.mark.login
def test_can_fill_login_form(page: Page, website_url):
    login_page = LoginPage(page)

    login_page.navigate(website_url)

    login_page.username_input.fill("standard_user")
    login_page.password_input.fill("secret_sauce")

    expect(login_page.username_input).to_have_value("standard_user")
    expect(login_page.password_input).to_have_value("secret_sauce")

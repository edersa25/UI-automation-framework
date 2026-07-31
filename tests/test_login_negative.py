import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "wrong_password"),
        ("wrong_user", "secret_sauce"),
        ("", ""),
    ],
)
def test_invalid_login(page: Page, website_url, username, password):
    login_page = LoginPage(page)

    login_page.navigate(website_url)

    login_page.login(username, password)

    expect(login_page.error_message).to_be_visible()

import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


@pytest.mark.login
@pytest.mark.parametrize(
    "username,password",
    [
        ("standard_user", "secret_sauce"),
        ("locked_out_user", "secret_sauce"),
        ("standard_user", "wrong_password"),
    ],
)
def test_login_attempts(page: Page, website_url, username, password):
    login_page = LoginPage(page)

    login_page.navigate(website_url)

    login_page.login(username, password)

    if username == "standard_user" and password == "secret_sauce":
        expect(page).to_have_url(lambda url: "inventory.html" in url)
    else:
        expect(login_page.error_message).to_be_visible()

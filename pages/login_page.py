from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def username_input(self):
        return self.page.locator("#user-name")

    @property
    def password_input(self):
        return self.page.locator("#password")

    @property
    def login_button(self):
        return self.page.locator("#login-button")

    @property
    def error_message(self):
        return self.page.locator("[data-test='error']")

    def navigate(self, website_url):
        self.page.goto(website_url)

    def login(self, username, password):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

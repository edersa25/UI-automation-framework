from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page

    @property
    def page_title(self):
        return self.page.locator(".title")

    @property
    def inventory_list(self):
        return self.page.locator(".inventory_list")

    @property
    def cart_badge(self):
        return self.page.locator(".shopping_cart_badge")

    def add_backpack_to_cart(self):
        self.page.locator("#add-to-cart-sauce-labs-backpack").click()

from pages.base_page import BasePage
from pages.locators import ShoppingCartPageLocators


class ShoppingCartPage(BasePage):
    page_url = ""
    page_locator = ""

    def visit_checkout(self):
        self.wait_until_clickable_and_click(ShoppingCartPageLocators.PROCEED_TO_CHECKOUT_BUTTON)

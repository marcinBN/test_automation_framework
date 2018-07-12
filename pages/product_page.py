from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    page_url = ""
    page_locator = ProductPageLocators.ITEM_DESCRIPTION_TEXT

    def add_to_cart(self):
        self.wait_until_clickable_and_click(ProductPageLocators.ADD_TO_CART_BUTTON)
        self.wait_until_clickable_and_click(ProductPageLocators.ADDED_TO_CART_CONFIRMATION_BOX_CLOSING_BUTTON)

    def view_cart(self):
        self.wait_until_clickable_and_click(ProductPageLocators.SHOPPING_CART_ICON)

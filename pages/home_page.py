from pages.base_page import BasePage
from pages.locators import HomePageLocators, CommonLocators


class HomePage(BasePage):
    page_url = ""
    page_locator = CommonLocators.MAIN_LOGO_PICTURE

    def search_for_item_with_filter(self, term="Kielbasa", buy_it_now=False, free_shipping=False):
        self.wait_until_clickable_and_click(HomePageLocators.ADVANCED_SEARCH_LINK)
        self.wait_until_visible_and_send_keys(HomePageLocators.ADVANCED_SEARCH_FIELD, term)

        if buy_it_now:
            self.wait_until_clickable_and_click(HomePageLocators.BUY_IT_NOW_CHECKBOX)
        if free_shipping:
            self.wait_until_clickable_and_click(HomePageLocators.FREE_SHIPPING_CHECKBOX)

        self.wait_until_clickable_and_click(HomePageLocators.ADVANCED_SEARCH_SUBMIT_BUTTON)

    def search_for_item_with_autocomplete(self, term, slice_size=10):
        self.wait_until_visible_and_send_keys(HomePageLocators.SEARCH_FIELD, term[:slice_size])
        self.wait_until_visible(HomePageLocators.SEARCH_AUTOCOMPLETE_LIST)
        self.wait_until_clickable_and_click(self.hardcode_parametrized_locator(locator=HomePageLocators.SEARCH_SUGGESTION_LINK, parameter_value=term))


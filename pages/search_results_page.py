from pages.base_page import BasePage
from pages.locators import SearchResultsPageLocators
from random import choice


class SearchResultsPage(BasePage):
    page_url = ""
    page_locator = SearchResultsPageLocators.FILTER_BUTTONS

    def get_list_of_found_items(self):
        return self.find_elements(SearchResultsPageLocators.FOUND_ITEM_LINK)

    def visit_random_item(self, items):
        choice(items).click()

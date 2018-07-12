import unittest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.shopping_cart_page import ShoppingCartPage
from pages.checkout_page import CheckoutPage
from base_test import BaseTest
from ddt import ddt, data, unpack


@ddt
class SmokeTests(BaseTest):

    @data(("vodka", ["US", "John", "Smith", "Baker Street", "Oklahoma"]),
          )
    @unpack
    def test_placing_order(self, product_name, customer_contact):
        home_page = HomePage(self.driver)
        home_page.visit_by_URL()
        home_page.search_for_item_with_filter(term=product_name, buy_it_now=True, free_shipping=False)

        search_results_page = SearchResultsPage(self.driver)
        found_items = search_results_page.get_list_of_found_items()
        search_results_page.visit_random_item(items=found_items)

        product_page = ProductPage(self.driver)
        product_page.wait_until_page_is_visible()
        product_page.add_to_cart()
        product_page.view_cart()

        shopping_cart_page = ShoppingCartPage(self.driver)
        shopping_cart_page.visit_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_as_guest()
        checkout_page.provide_contact_details(*customer_contact)


    @data(("sony handycam", 10),
          ("paco de lucia cd", 11),
          )
    @unpack
    def test_autocompletion_of_search(self, product_name, slice_size):
        home_page = HomePage(self.driver)
        home_page.visit_by_URL()
        home_page.search_for_item_with_autocomplete(term=product_name, slice_size=slice_size)


if __name__ == "__main__":
    unittest.main()
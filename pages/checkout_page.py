from pages.base_page import BasePage
from pages.locators import CheckoutPageLocators
from selenium.webdriver.support.ui import Select


class CheckoutPage(BasePage):
    page_url = ""
    page_locator = ""

    def enter_as_guest(self):
        self.wait_until_clickable_and_click(CheckoutPageLocators.CONTINUE_AS_GUEST_BUTTON)

    def provide_contact_details(self, country_code, first_name, last_name, street_address, city):
        country_list = Select(self.find_element(CheckoutPageLocators.COUNTRY_DROP_DOWN_LIST))
        country_list.select_by_value(country_code)

        self.wait_until_visible_and_send_keys(CheckoutPageLocators.FIRST_NAME_FIELD, first_name)
        self.wait_until_visible_and_send_keys(CheckoutPageLocators.LAST_NAME_FIELD, last_name)
        self.wait_until_visible_and_send_keys(CheckoutPageLocators.STREET_ADDRESS_FIELD, street_address)
        self.wait_until_visible_and_send_keys(CheckoutPageLocators.CITY_FIELD, city)


import time
from abc import abstractmethod
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.support.ui import Select
from framework_config import MyConfig
from pages.locators import CommonLocators


class BasePage(object):
    """ All page objects inherit from this """

    page_url = ""
    page_locator = CommonLocators.MAIN_LOGO_PICTURE

    def __init__(self, driver):
        self.driver = driver

    def visit_by_URL(self):
        running_env_url = MyConfig.environments_URLS[MyConfig.ENV_in_use][0]
        self.driver.get(running_env_url + self.page_url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    def wait_until_clickable(self, locator, timeout=MyConfig.wait_timeout):
        WebDriverWait(self.driver, timeout).until(ec.element_to_be_clickable(locator))

    def wait_until_visible(self, locator, timeout=MyConfig.wait_timeout):
        WebDriverWait(self.driver, timeout).until(ec.visibility_of_element_located(locator))

    def wait_until_visible_and_send_keys(self, locator, keys):
        self.wait_until_visible(locator)
        self.find_element(locator).clear()
        self.find_element(locator).send_keys(keys)

    def wait_until_clickable_and_click(self, locator):
        self.wait_until_clickable(locator)
        self.find_element(locator).click()

    def hardcode_parametrized_locator(self, locator, parameter_value):
        return (locator[0], locator[1] % parameter_value)

    def get_page_title(self):
        return self.driver.title

    def wait_until_page_is_visible(self):
        self.wait_until_visible(self.page_locator)


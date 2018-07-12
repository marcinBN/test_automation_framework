from selenium.webdriver.common.by import By


class CommonLocators(object):
    MAIN_LOGO_PICTURE = (By.ID, "gh-la")


class HomePageLocators(object):
    SEARCH_FIELD = (By.XPATH, "//input[@id='gh-ac']")
    SEARCH_SUBMIT_BUTTON = (By.XPATH, "//input[@id='gh-btn']")
    SEARCH_AUTOCOMPLETE_LIST = (By.XPATH, "//ul[@id='ui-id-1']")
    SEARCH_SUGGESTION_LINK = (By.XPATH, "//a[@class='ghAC_sugg ui-corner-all'][contains(@aria-label,'%s')]")
    ADVANCED_SEARCH_LINK = (By.XPATH, "//a[@id='gh-as-a']")
    ADVANCED_SEARCH_FIELD = (By.XPATH, "//input[@id='_nkw']")
    BUY_IT_NOW_CHECKBOX = (By.XPATH, "//input[@id='LH_BIN']")
    FREE_SHIPPING_CHECKBOX = (By.XPATH, "//input[@id='LH_FS']")
    ADVANCED_SEARCH_SUBMIT_BUTTON = (By.XPATH, "//div[@class='adv-s mb space-top']//button[@type='submit']")


class SearchResultsPageLocators(object):
    FILTER_BUTTONS = (By.XPATH, "//ul[@class='fake-tabs__items']")
    FOUND_ITEM_LINK = (By.CLASS_NAME, "vip")


class ProductPageLocators(object):
    ITEM_DESCRIPTION_TEXT = (By.XPATH, "//div[@id='desc_wrapper_ctr']")
    ADD_TO_CART_BUTTON = (By.XPATH, "//a[@id='atcRedesignId_btn']")
    ADDED_TO_CART_CONFIRMATION_BOX_CLOSING_BUTTON = (By.XPATH, "//div[@class='clzBtn viicon-close']")
    SHOPPING_CART_ICON = (By.XPATH, "//a[@id='gh-cart-1']")


class ShoppingCartPageLocators(object):
    PROCEED_TO_CHECKOUT_BUTTON = (By.XPATH, "//a[@id='ptcBtnRight']")


class CheckoutPageLocators(object):
    CONTINUE_AS_GUEST_BUTTON = (By.XPATH, "//button[@id='gtChk']")
    COUNTRY_DROP_DOWN_LIST = (By.XPATH, "//select[@id='af-country']")
    FIRST_NAME_FIELD = (By.XPATH, "//input[@id='af-first-name']")
    LAST_NAME_FIELD = (By.XPATH, "//input[@id='af-last-name']")
    STREET_ADDRESS_FIELD = (By.XPATH, "//input[@id='af-address1']")
    CITY_FIELD = (By.XPATH, "//input[@id='af-city']")

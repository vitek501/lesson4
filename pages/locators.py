from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, ".login_form")
    REGISTRATION_LINK = (By.CSS_SELECTOR, ".register_form")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    ALLERT_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")

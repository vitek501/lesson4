import math
from .base_page import BasePage
from selenium.common.exceptions import NoAlertPresentException
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def test_purchase_book(self):
        link = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        link.click()
         
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_purchase(self):
        product = self.browser.find_element(*ProductPageLocators.PRODUCT).text.lower()
        alert_product = self.browser.find_element(*ProductPageLocators.ALLERT_PRODUCT).text.lower()
        assert product == alert_product, 'Added the wrong product'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
           "Success message is presented, but should not be"

    def message_should_be_gone(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
                "Success message is not missing"

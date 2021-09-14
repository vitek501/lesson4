from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        """ проверка на корректный url адрес"""
        url = self.browser.current_url
        assert 'login' in url, 'No "login" in url' 

    def should_be_login_form(self):
        """ проверка, что есть форма логина""" 
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login form is not present"

    def should_be_register_form(self):
        """проверка, что есть форма регистрации на странице""" 
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LINK), "Registration form is not present"

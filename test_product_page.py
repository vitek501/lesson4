import pytest
from pages.product_page import ProductPage
import time

@pytest.mark.parametrize('num', [*range(7),
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  *range(8,10)])
def test_guest_can_add_product_to_basket(browser, num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser, link)   
    page.open()                      # открываем страницу
    page.test_purchase_book()
    page.solve_quiz_and_get_code()
    page.check_purchase()


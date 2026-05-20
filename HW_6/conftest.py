import pytest
from selenium import webdriver

from HW_6.pages.checkout_step_two_page import CheckoutStepTwo
from HW_6.pages.info_page import InfoPage
from HW_6.pages.login_page import LoginPage
from HW_6.pages.inventory_page import InventoryPage
from HW_6.pages.cart_page import CartPage


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.inventory_page = InventoryPage(driver)
    request.cls.cart_page = CartPage(driver)
    request.cls.info_page = InfoPage(driver)
    request.cls.checkout_step_two = CheckoutStepTwo(driver)

    yield
    driver.quit()

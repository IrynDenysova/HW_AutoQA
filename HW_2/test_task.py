# Написать скрипт, который:
# Открывает в браузере Firefox https://itcareerhub.de/ru
# Переходит в раздел “Способы оплаты”
# Делает скриншот этой секции страницы
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_about_page(driver):
    driver.get("https://itcareerhub.de/ru")
    sleep(2)
    about_link = driver.find_element(By.LINK_TEXT, "Способы оплаты")
    about_link.click()
    driver.save_screenshot("HW_2/ICH.png")
    sleep(2)


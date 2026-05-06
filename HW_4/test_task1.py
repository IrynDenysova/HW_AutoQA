# Тестируемый сайт:
# http://uitestingplayground.com/textinput
# Шаги теста:
# Перейдите на сайт Text Input.
# Введите в поле ввода текст "ITCH".
# Нажмите на синюю кнопку.
# Проверьте, что текст кнопки изменился на "ITCH".

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button(driver):
    driver.get("http://uitestingplayground.com/textinput")
    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.send_keys("ITCH")
    button = driver.find_element(By.ID, "updatingButton")
    button.click()
    assert button.text == "ITCH"
    print(f"The button bears the text: {button.text}")

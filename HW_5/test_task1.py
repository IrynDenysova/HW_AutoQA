# Задание 1: Проверка наличия текста в iframe
# Открыть страницу
# Перейти по ссылке: https://bonigarcia.dev/selenium-webdriver-java/iframes.html.
# Проверить наличие текста
# Найти фрейм (iframe), в котором содержится искомый текст.
# Переключиться в этот iframe.
# Найти элемент, содержащий текст "semper posuere integer et senectus justo curabitur.".
# Убедиться, что текст отображается на странице.


import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_iframe_text(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")
    wait = WebDriverWait(driver, 10)

    iframe_element = wait.until(EC.presence_of_element_located((By.ID, "my-iframe")))
    driver.switch_to.frame(iframe_element)

    target_text = "semper posuere integer et senectus justo curabitur."

    paragraphs = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p")))

    text_found = any(target_text in p.text and p.is_displayed() for p in paragraphs)

    assert text_found, f"Текст '{target_text}' не найден или скрыт!"

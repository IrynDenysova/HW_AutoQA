# Тестируемый сайт:
# https://bonigarcia.dev/selenium-webdriver-java/loading-images.html
# Шаги теста:
# Перейдите на сайт Loading Images.
# Дождитесь загрузки всех изображений.
# Получите значение атрибута alt у третьего изображения.
# Убедитесь, что значение атрибута alt равно "award".

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_atribute(driver):
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    wait = WebDriverWait(driver, 15)
    wait.until(EC.presence_of_element_located((By.ID, 'landscape')))
    images = driver.find_elements(By.CSS_SELECTOR, '#image-container')

    if len(images) >= 3:
        third_image = images[2]
        alt_text = third_image.get_attribute("alt")
        assert alt_text == "award"

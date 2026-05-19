# Задание 2: Тестирование Drag & Drop (Перетаскивание изображения в корзину)
# Открыть страницу Drag & Drop Demo.
# Перейти по ссылке: https://www.globalsqa.com/demo-site/draganddrop/.
# Выполнить следующие шаги:
# Захватить первую фотографию (верхний левый элемент).
# Перетащить её в область корзины (Trash).
# Проверить, что после перемещения:
# В корзине появилась одна фотография.
# В основной области осталось 3 фотографии.
# Ожидаемый результат:
# Фотография успешно перемещается в корзину.
# Вне корзины остаются 3 фотографии.


import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    browser = webdriver.Chrome()
    browser.maximize_window()
    yield browser
    browser.quit()


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    driver.execute_script("""
            var cookies = document.querySelector('.fc-consent-root, #cookie-law-info-bar');
            if (cookies) { cookies.remove(); }
        """)
    wait = WebDriverWait(driver, 10)

    demo_frame = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".demo-frame")))
    driver.switch_to.frame(demo_frame)

    gallery_items = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#gallery > li")))
    first_photo = gallery_items[0]
    trash = wait.until(EC.presence_of_element_located((By.ID, "trash")))

    actions = ActionChains(driver)
    actions.drag_and_drop(first_photo, trash).perform()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#trash ul > li")))

    remaining_photos = driver.find_elements(By.CSS_SELECTOR, "#gallery > li")
    trashed_photos = driver.find_elements(By.CSS_SELECTOR, "#trash ul > li")

    assert len(trashed_photos) == 1, "В корзине должно быть ровно 1 фото"
    assert len(remaining_photos) == 3, "В галерее должно остаться ровно 3 фото"

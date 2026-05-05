import pytest
from selenium import webdriver
from selenium.common import exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_itcareerhub_ui(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://itcareerhub.de/ru")

    logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='IT Career Hub']")))
    assert logo.is_displayed()

    links = ["Программы", "Способы оплаты", "О нас", "Отзывы", "Блог"]
    for link in links:
        assert wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link)))

    assert driver.find_element(By.CSS_SELECTOR, "a[href='/ru']").is_displayed()
    assert driver.find_element(By.CSS_SELECTOR, "a[href='/']").is_displayed()


def test_callback_only(driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://itcareerhub.de/ru")

    contact = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "О нас")))
    contact.click()

    find_contact = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Контакты")))
    find_contact.click()

    callback = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "ОБРАТНЫЙ ЗВОНОК")))
    driver.execute_script("arguments[0].click();", callback)

    elements = driver.find_elements(By.XPATH, "//div[not(child::div)]")
    saw_text = False
    text = "Запишитесь на бесплатную карьерную консультацию"
    for element in elements:
        try:
            if element.is_displayed() and text in element.text:
                saw_text = True
                break
        except exceptions.StaleElementReferenceException:
            pass

    assert saw_text

    # alternative solution

    # modal = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,
    #                                                      'div[id="molecule-175871291755985340"]')))
    # modal_text = modal.text
    # assert text in modal_text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class InfoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def fill_form(self, first_label, first_name, second_label, zip_code):
        first_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        first_name_field.clear()
        first_name_field.send_keys(first_name)

        last_name_field = self.wait.until(EC.presence_of_element_located((By.ID, "last-name")))
        last_name_field.clear()
        last_name_field.send_keys("Doe")

        zip_field = self.wait.until(EC.presence_of_element_located((By.ID, "postal-code")))
        zip_field.clear()
        zip_field.send_keys(zip_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()

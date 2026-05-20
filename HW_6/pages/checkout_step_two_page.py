from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutStepTwo:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_price(self):
        total_label = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        raw_text = total_label.text

        return raw_text.split("$")[1].strip()


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()

    def type(self, locator, txt):
        el = self.find(locator)
        el.clear()
        el.send_keys(txt)

    def text(self, locator):
        return self.find(locator).text

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def current_url(self):
        return self.driver.current_url

    def title(self):
        return self.driver.title

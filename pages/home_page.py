
from selenium.webdriver.common.by import By
from .base_page import BasePage

class HomePage(BasePage):
    SEARCH_INPUT = (By.ID, "twotabsearchtextbox")
    COOKIE_ACCEPT = (By.ID, "sp-cc-accept")
    SEARCH_SUBMIT = (By.ID, "nav-search-submit-button")

    def open(self, base_url):
        self.driver.get(base_url)

    def accept_cookies(self):
        # click if exists
        try:
            self.click(self.COOKIE_ACCEPT)
        except Exception:
            pass

    def search(self, term: str):
        self.type(self.SEARCH_INPUT, term)
        self.click(self.SEARCH_SUBMIT)

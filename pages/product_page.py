
from selenium.webdriver.common.by import By
from .base_page import BasePage

class ProductPage(BasePage):
    ADD_TO_CART = (By.ID, "submit.add-to-cart")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product-title-word-break")
    CART_COUNT = (By.ID, "nav-cart-count")

    def __init__(self, driver):
        super().__init__(driver)
        self.saved_title = None

    def add_to_cart(self):
        self.click(self.ADD_TO_CART)

    def get_title(self):
        return self.text(self.PRODUCT_TITLE)

    def save_title(self):
        self.saved_title = self.get_title()

    def cart_count_value(self):
        return self.text(self.CART_COUNT)

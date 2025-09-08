
from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    HEADER = (By.ID, "sc-active-items-header")
    PRODUCT_TITLE = (By.CLASS_NAME, "a-truncate-cut")
    DELETE_BTN = (By.CSS_SELECTOR, "input.a-color-link")
    LOGO = (By.ID, "nav-logo-sprites")
    CART_COUNT = (By.ID, "nav-cart-count")

    def header_text(self):
        return self.text(self.HEADER)

    def cart_product_title(self):
        return self.text(self.PRODUCT_TITLE)

    def delete_item(self):
        self.click(self.DELETE_BTN)

    def is_deleted_cart_count(self):
        return self.text(self.CART_COUNT)

    def click_logo(self):
        self.click(self.LOGO)

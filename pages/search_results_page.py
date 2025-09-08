from selenium.webdriver.common.by import By
from .base_page import BasePage

class SearchResultsPage(BasePage):
    # Amazon bazen breadcrumb için "a-color-state" veya "a-color-state a-text-bold" kullanıyor
    BREADCRUMB = (By.CSS_SELECTOR, ".a-color-state, .a-color-state.a-text-bold")
    PAGE2 = (By.XPATH, "//a[@aria-label='2 sayfasına git']")
    THIRD_PRODUCT = (By.XPATH, "(//img[@class='s-image'])[3]")
    CART_COUNT = (By.ID, "nav-cart-count")

    def breadcrumb_text(self):
        """Try to return breadcrumb text, if not found fallback to URL."""
        try:
            return self.text(self.BREADCRUMB)
        except Exception:
            return self.driver.current_url

    def go_to_second_page(self):
        self.click(self.PAGE2)

    def select_third_product(self):
        self.click(self.THIRD_PRODUCT)

    def cart_count(self):
        return self.text(self.CART_COUNT)


import pytest
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage

def test_add_to_cart_flow(driver, base_url):
    home = HomePage(driver)
    home.open(base_url)
    home.accept_cookies()
    home.search("samsung")

    results = SearchResultsPage(driver)
    assert "samsung" in results.breadcrumb_text().lower()

    results.go_to_second_page()
    assert "page=2" in driver.current_url

    results.select_third_product()

    product = ProductPage(driver)
    product.save_title()
    product.add_to_cart()

    # cart count should be 1
    assert product.cart_count_value() == "1"

    cart = CartPage(driver)
    # go to cart via clicking cart icon (nav-cart-count is already visible)
    driver.get(base_url + "gp/cart/view.html")

    # product title snippet should match
    assert product.saved_title is not None
    assert cart.cart_product_title().strip()[:10].lower() in product.saved_title.lower()

    # delete product and verify cart is empty
    cart.delete_item()
    assert cart.is_deleted_cart_count() == "0"

    # go back home via logo and check title contains Amazon
    cart.click_logo()
    assert "Amazon" in driver.title

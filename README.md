# Insider-Amazon_Test-Automation-Project
Automated testing framework for Amazon.com.tr built with Python, Selenium WebDriver, and Pytest. Covers search, pagination, add-to-cart, and cart management scenarios.

# QA Automation Project – Amazon.com.tr

This project is an **end-to-end QA automation framework** developed with **Python, Selenium WebDriver, and Pytest**.  
It automates an e-commerce workflow on [Amazon.com.tr](https://www.amazon.com.tr), covering product search, pagination, product selection, cart operations, and validations.

---

## 🚀 Features
- **Page Object Model (POM)** structure for maintainability
- **End-to-end test scenario** covering search, pagination, add-to-cart, and cart management
- Runs on **Google Chrome**, starts in **maximized mode**
- Assertions for every step to ensure accuracy

---

## 📝 Test Scenario

The automated test case performs the following steps:

1. Go to [Amazon.com.tr](https://www.amazon.com.tr/)  
2. Verify that you are on the home page  
3. Type **'samsung'** in the search field at the top of the screen and perform search  
4. Verify that there are results for Samsung on the page that appears  
5. Click on the **2nd page** from the search results and verify that the 2nd page is currently displayed  
6. Go to the **3rd product page** from the top  
7. Verify that you are on the product page  
8. Add the product to the cart  
9. Verify that the product has been added to the cart  
10. Go to the cart page  
11. Verify that you are on the cart page and that the correct product has been added to the cart  
12. Delete the product from the cart and verify that it has been deleted  
13. Return to the home page and verify that it is on the home page  

---

## 🛠️ Tech Stack
- **Language**: Python 3.10.11  
- **Framework**: Pytest  
- **Automation**: Selenium WebDriver  
- **Driver Management**: WebDriver Manager  

---

## 📂 Project Structure
├── conftest.py # Driver setup (Chrome, maximized)
├── requirements.txt # Dependencies
├── pages/ # Page Object Model classes
│ ├── base_page.py
│ ├── home_page.py
│ ├── search_results_page.py
│ ├── product_page.py
│ └── cart_page.py
└── tests/
└── test_amazon_add_to_cart.py

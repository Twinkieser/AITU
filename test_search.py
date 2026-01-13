import unittest
from selenium.webdriver.common.by import By
from utils.driver_setup import get_driver

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com")

    def test_search_products(self):
        # Логин
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Поиск товара по имени (CSS + XPath)
        product = self.driver.find_element(By.CSS_SELECTOR, ".inventory_item_name")
        assert "Sauce Labs Backpack" in product.text

        # XPath: найти кнопку "Add to cart"
        add_btn = self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']")
        add_btn.click()

        # Checkpoint: кнопка изменилась на "Remove"
        remove_btn = self.driver.find_element(By.XPATH, "//button[@data-test='remove-sauce-labs-backpack']")
        assert remove_btn.is_displayed()

    def tearDown(self):
        self.driver.quit()
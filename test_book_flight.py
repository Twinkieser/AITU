import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from utils.driver_setup import get_driver

class TestBookFlight(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com")

    def test_checkout_flow(self):
        wait = WebDriverWait(self.driver, 10)

        # Логин
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Добавить товар
        self.driver.find_element(By.CSS_SELECTOR, ".btn_inventory").click()

        # Перейти в корзину
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Checkout
        self.driver.find_element(By.ID, "checkout").click()

        # Заполнить форму
        self.driver.find_element(By.ID, "first-name").send_keys("Talgat")
        self.driver.find_element(By.ID, "last-name").send_keys("Gali")
        self.driver.find_element(By.ID, "postal-code").send_keys("050000")
        self.driver.find_element(By.ID, "continue").click()

        # Checkpoint: страница подтверждения
        assert "Checkout: Overview" in self.driver.page_source

    def tearDown(self):
        self.driver.quit()
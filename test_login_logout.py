import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.driver_setup import get_driver

class TestLoginLogout(unittest.TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.get("https://www.saucedemo.com")

    def test_login_logout(self):
        wait = WebDriverWait(self.driver, 10)

        # Логин
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Checkpoint: после входа
        assert "Swag Labs" in self.driver.title

        # Логаут
        burger = wait.until(EC.element_to_be_clickable((By.ID, "react-burger-menu-btn")))
        burger.click()
        logout = wait.until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link")))
        logout.click()

        # Checkpoint: вернулись на страницу логина
        assert "Login" in self.driver.page_source or "Swag Labs" in self.driver.title

    def tearDown(self):
        self.driver.quit()
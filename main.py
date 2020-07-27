from pages.page_register import MainPage
import unittest
import time

from selenium import webdriver


class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            '/home/jhonatanf/Documentos/Automation/chromedriver')
        self.driver.get("https://tms.liftit-sandbox.com/login")

    def test_successful_login(self):
        main = MainPage(self.driver)
        main.email_element = 'qa.automation.liftit@gmail.com'
        main.pwd_element = 'L12345678'
        main.login()
        self.driver.implicitly_wait(5)
        title = self.driver.find_element_by_tag_name("h2")
        assert title.text == "Servicios"
        self.driver.save_screenshot(
            '/home/jhonatanf/Imágenes/Test_aut_screeshots/test_successful_login.png')

    def test_fail_login_invalid_pwd(self):
        main = MainPage(self.driver)
        main.email_element = 'qa.automation.liftit@gmail.com'
        main.pwd_element = '$$L12345678'
        main.login()
        self.driver.implicitly_wait(10)
        message = self.driver.find_element_by_id("notification1")
        assert message.text == "Email o contraseña inválidas"
        time.sleep(1)
        self.driver.save_screenshot(
            '/home/jhonatanf/Imágenes/Test_aut_screeshots/test_fail_login_invalid_pwd.png')

    def test_fail_login_invalid_user(self):
        main = MainPage(self.driver)
        main.email_element = 'qa.automation$$$.liftit@gmail.com'
        main.pwd_element = 'L12345678'
        main.login()
        self.driver.implicitly_wait(10)
        message = self.driver.find_element_by_id("notification1")
        assert message.text == "Email o contraseña inválidas"
        time.sleep(1)
        self.driver.save_screenshot(
            '/home/jhonatanf/Imágenes/Test_aut_screeshots/test_fail_login_invalid_user.png')

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

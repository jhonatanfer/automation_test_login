from pages.page_register import MainPage
import unittest
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

    def test_fail_login_invalid_pwd(self):
        main = MainPage(self.driver)
        main.email_element = 'qa.automation.liftit@gmail.com'
        main.pwd_element = '$$L12345678'
        main.login()
        self.driver.implicitly_wait(5)
        message = self.driver.find_element_by_id("notification1")
        assert message.text == "Email o contraseña inválidas"

    def test_fail_login_invalid_user(self):
        main = MainPage(self.driver)
        main.email_element = 'qa.automation$$$.liftit@gmail.com'
        main.pwd_element = 'L12345678'
        main.login()
        self.driver.implicitly_wait(5)
        message = self.driver.find_element_by_id("notification1")
        assert message.text == "Email o contraseña inválidas"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

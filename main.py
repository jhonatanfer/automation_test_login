from pages.page_register import MainPage
# se importa el login de Mainpage
import unittest
from selenium import webdriver


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

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


'''
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.    
        
        print(self.driver.title)
        self.driver.implicitly_wait(5)
        user_field = self.driver.find_element_by_name ('email')
        pass_field = self.driver.find_element_by_name ('password')
        submit_button = self.driver.find_element_by_id('button')
        user_field.send_keys('qa.automation.liftit@gmail.com')
        pass_field.send_keys('L12345678')
        submit_button.click()
        print(self.driver.title)
        self.driver.implicitly_wait(5)
    
        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        #Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match."
        #Sets the text of search textbox to "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        #Verifies that the results page is not empty
        assert search_results_page.is_results_found(), "No results found."
        '''

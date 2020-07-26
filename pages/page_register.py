from pages.objects.objects import EmailElement, PasswordElement


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    email_element = EmailElement()
    pwd_element = PasswordElement()

    def login(self):
        submit_button = self.driver.find_element_by_id('button')
        submit_button.click()

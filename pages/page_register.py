from pages.objects.objects import EmailElement, PasswordElement


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    email_element = EmailElement()
    pwd_element = PasswordElement()

    def login(self):
        submit_button = self.driver.find_element_by_id('button')
        submit_button.click()

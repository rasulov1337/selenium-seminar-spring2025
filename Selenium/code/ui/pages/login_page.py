from ui.pages.base_page import BasePage
from selenium.webdriver.support.expected_conditions import url_to_be
from ui.locators.login_locators import LoginPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from ui.pages.main_page import MainPage
class LoginPage(BasePage):
    url = 'https://education.vk.company/'
    authorize = False

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(self.url)
        self.is_opened()
        self.driver.set_page_load_timeout(15)


    def login(self, email, password):
        try:
            self.click(LoginPageLocators.LOGIN_BUTTON)
        except:
            # Some fucking error displays. I've wasted a lot of nerves and time trying to solve this crappy shit and this was the best solution I've found.
            pass

        self.click(LoginPageLocators.CONTINUE_WITH_PASSWORD_BUTTON)
        self.find(LoginPageLocators.EMAIL_INPUT).send_keys(email)
        self.find(LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(LoginPageLocators.SEND_CREDENTIALS_BUTTON)

        # return MainPage(self.driver)

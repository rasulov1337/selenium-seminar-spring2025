from ui.pages.base_page import BasePage
from ui.locators.login_locators import LoginPageLocators

class LoginPage(BasePage):
    url = 'https://education.vk.company/'
    authorize = False
    locators = LoginPageLocators()

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

        self.click(self.locators.CONTINUE_WITH_PASSWORD_BUTTON)
        self.find(self.locators.EMAIL_INPUT).send_keys(email)
        self.find(self.locators.PASSWORD_INPUT).send_keys(password)
        self.click(self.locators.SEND_CREDENTIALS_BUTTON)

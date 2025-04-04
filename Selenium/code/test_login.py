import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import url_to_be
from ui.pages.base_page import BasePage

import os

load_dotenv()


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(self.url)
        self.is_opened()

    def login(self, email, password):
        login_button = self.find((By.XPATH, "//a[text()='вход / регистрация']"))
        login_button.click()

        self.find((By.XPATH, "//button[text()='Продолжить с помощью почты и пароля']")).click()

        email_input = self.find((By.ID, 'email'))
        email_input.send_keys(email)

        password_input = self.find((By.ID, 'password'))
        password_input.send_keys(password)

        self.find((By.XPATH, "//button[text()='Войти с паролем']")).click()

        return MainPage(self.driver)


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.login_page.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))

# class TestLK(BaseCase):

#     def test_lk1(self):
#         pass

#     def test_lk2(self):
#         pass

#     def test_lk3(self):
#         pass

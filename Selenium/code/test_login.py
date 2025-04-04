import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv

from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC

import os

load_dotenv()


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        if self.authorize:
            self.login_page.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))


@pytest.fixture(scope='session')
def credentials():
        pass


@pytest.fixture(scope='session')
def cookies(credentials, config):
        pass


class TestLogin(BaseCase):
    authorize = True

    def test_login(self, credentials):
        self.login_page.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
        assert self.driver.title == 'Лента - VK Education'

# class TestLK(BaseCase):
#     authorize = True

#     def test_lk1(self):
#         pass

#     def test_lk2(self):
#         pass

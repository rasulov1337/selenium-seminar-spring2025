import pytest
from _pytest.fixtures import FixtureRequest
from dotenv import load_dotenv

from selenium.webdriver.common.by import By
from ui.pages.login_page import LoginPage
from ui.pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from ui.locators.basic_locators import BasePageLocators

import os
from ui.locators.main_locators import MainPageLocators
from ui.locators.search_locators import SearchPageLocators

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
    authorize = False

    def test_login(self, credentials):
        self.login_page.login(os.getenv('EMAIL'), os.getenv('PASSWORD'))
        WebDriverWait(self.driver, 10).until(EC.title_is('Моё обучение'))

class TestLK(BaseCase):
    authorize = True

    def test_search_classmate(self):
        search_query = os.getenv('SEARCH_QUERY')
        assert search_query, 'Search query is empty!'
        self.main_page.search(search_query)
        assert self.main_page.find(SearchPageLocators.PAGE_HEADER).text == 'Результаты поиска'

    def test_info_about_current_seminar(self):
        self.main_page.open_info_about_lesson_at_day_of_week(os.getenv('SCHEDULE_SELECT_DAY_OF_WEEK'))
        WebDriverWait(self.driver, 10).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[1])
        assert "Дата проведения" in self.driver.find_element(*BasePageLocators.BODY).text, 'Дата проведения not found on the page'

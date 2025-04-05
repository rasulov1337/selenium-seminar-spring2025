import time
from selenium.common.exceptions import TimeoutException

import allure
from selenium.webdriver.remote.webelement import WebElement
from ui.locators import basic_locators
from ui.locators import main_locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PageNotOpenedExeption(Exception):
    pass


class BasePage(object):

    locators = basic_locators.BasePageLocators()
    locators_main = main_locators.MainPageLocators()
    url = 'https://www.python.org/'

    def is_opened(self, timeout=4):
        started = time.time()
        while time.time() - started < timeout:
            if self.driver.current_url == self.url:
                return True
        raise PageNotOpenedExeption(f'{self.url} did not open in {timeout} sec, current url {self.driver.current_url}')

    def __init__(self, driver):
        self.driver = driver
        self.driver.set_page_load_timeout(5)
        try:
            self.driver.get(self.url)  # Fucking open base url immediately
        except TimeoutException:
            driver.execute_script("window.stop();")
        # self.is_opened()

    def wait(self, timeout=None):
        if timeout is None:
            timeout = 5
        return WebDriverWait(self.driver, timeout=timeout)

    def find(self, locator, timeout=None):
        return self.wait(timeout).until(EC.presence_of_element_located(locator))

    @allure.step('Search')
    def search(self, query):
        elem = self.find(self.locators.QUERY_LOCATOR_ID)
        elem.send_keys(query)
        go_button = self.find(self.locators.GO_BUTTON_LOCATOR)
        go_button.click()
        self.my_assert()

    @allure.step("Step 1")
    def my_assert(self):
        assert 1 == 1


    @allure.step('Click')
    def click(self, locator, timeout=None) -> WebElement:
        self.find(locator, timeout=timeout)
        elem = self.wait(timeout).until(EC.element_to_be_clickable(locator))
        elem.click()

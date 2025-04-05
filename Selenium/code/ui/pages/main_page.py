from selenium.webdriver.common.by import By

import allure
from selenium.webdriver.common.keys import Keys
from ui.locators import main_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    locators = main_locators.MainPageLocators()

    @allure.step("Step 2")
    def go_to_events_page(self):
        events_button = self.find(self.locators.EVENTS)
        # self.click(events_button)
        self.click((By.ID, 'events'))
        return EventsPage(self.driver)

    def search(self, query: str):
        self.click(self.locators.SHOW_SEARCH_INPUT_BUTTON)
        search_input = self.find(self.locators.SEARCH_INPUT)
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def open_info_about_lesson_at_day_of_week(self, day_of_week):
        self.click(self.locators.day_of_week_button(day_of_week))
        self.click(self.locators.MORE_INFO_ABOUT_CURRENT_LESSON_BUTTON)

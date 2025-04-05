from selenium.webdriver.common.by import By

import allure
from selenium.webdriver.common.keys import Keys
from ui.locators import basic_locators
from ui.pages.base_page import BasePage
from ui.pages.events_page import EventsPage
from ui.locators.main_locators import MainPageLocators
from ui.locators.schedule_locators import ScheduleLocators


class MainPage(BasePage):
    url = 'https://education.vk.company/feed/'

    locators = basic_locators.MainPageLocators()

    @allure.step("Step 2")
    def go_to_events_page(self):
        events_button = self.find(self.locators.EVENTS)
        # self.click(events_button)
        self.click((By.ID, 'events'))
        return EventsPage(self.driver)

    def search(self, query: str):
        self.click(MainPageLocators.SHOW_SEARCH_INPUT_BUTTON)
        search_input = self.find(MainPageLocators.SEARCH_INPUT)
        search_input.send_keys(query)
        search_input.send_keys(Keys.RETURN)

    def open_info_about_lesson_at_day_of_week(self, day_of_week):
        self.click(ScheduleLocators.day_of_week_button(day_of_week))
        self.click(ScheduleLocators.MORE_INFO_ABOUT_CURRENT_LESSON_BUTTON)

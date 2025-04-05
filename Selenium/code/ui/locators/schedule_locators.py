from selenium.webdriver.common.by import By


class ScheduleLocators():
    @staticmethod
    def day_of_week_button(day_of_week):
        return (By.XPATH, '//aside//span[contains(text(), "{}")]'.format(day_of_week))
    MORE_INFO_ABOUT_CURRENT_LESSON_BUTTON = (By.XPATH, '//aside//div/a[contains(@class, "title")]')

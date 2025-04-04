from selenium.webdriver.common.by import By


class MainPageLocators():
    SHOW_SEARCH_INPUT_BUTTON = (By.XPATH, r"//div[@aria-label='Открыть поиск']")
    SEARCH_INPUT = (By.XPATH, '//form/input')

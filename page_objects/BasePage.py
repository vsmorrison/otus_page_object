from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def _click_element(self, element):
        element.click()

    def _check_element_presence(self, element):
        WebDriverWait(self.browser, 2).until(
            EC.visibility_of_element_located(element))

    def _check_page_title(self, title):
        WebDriverWait(self.browser, 2).until(
            EC.title_is(title))

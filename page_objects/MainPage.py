from .BasePage import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    LOGO = (By.CSS_SELECTOR, "#logo")
    MENU = (By.CSS_SELECTOR, ".container #menu")
    SLIDER = (By.CSS_SELECTOR, "div.slideshow")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "[alt='Canon EOS 5D']")
    PAGE_TITLE = "Your store"

    def verify_logo_presence(self):
        self._check_element_presence(*self.LOGO)

    def verify_menu_presence(self):
        self._check_element_presence(*self.MENU)

    def verify_slider_presence(self):
        self._check_element_presence(*self.SLIDER)

    def verify_product_image_presence(self):
        self._check_element_presence(*self.PRODUCT_IMAGE)

    def verify_page_title(self):
        self._check_page_title(self.PAGE_TITLE)


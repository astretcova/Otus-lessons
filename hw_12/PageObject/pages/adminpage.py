from selenium.webdriver.common.by import By
from .base import BasePage


class AdminLoginPage(BasePage):

    username = (By.ID, 'input-username')
    password = (By.ID, 'input-password')
    submit_button = (By.CSS_SELECTOR, 'button')
    logout = (By.CSS_SELECTOR, 'li:nth-child(2) a')
    forgotten_pass = (By.CSS_SELECTOR, 'span a')
    footer = (By.CSS_SELECTOR, 'footer a')
    catalog = (By.XPATH, '//*[@id="menu-catalog"]/a')
    products = (By.XPATH, '//*[@id="collapse1"]/li[2]/a')
    product_name = (By.XPATH, '//*[@id="input-name"]')
    filter_button = (By.XPATH, '//*[@id="button-filter"]')
    reviews = (By.XPATH, '//*[@id="collapse1"]/li[9]/a')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def _set_username_(self, name):
        self.find_element(locator=self.username).clear()
        self.find_element(locator=self.username).send_keys(name)

    def _set_password_(self, password):
        self.find_element(locator=self.password).clear()
        self.find_element(locator=self.password).send_keys(password)

    def login(self, username, password):
        self._set_username_(username)
        self._set_password_(password)
        self.find_element(locator=self.submit_button).click()

    def _forgotten_pass(self):
        self.find_element(locator=self.forgotten_pass).click()

    def go_to_home_page(self):
        self.find_element(locator=self.footer).click()

    def expand_catalog(self):
        self.find_element(locator=self.catalog).click()

    def expand_products(self):
        self.find_element(locator=self.products).click()

    def fill_product_name(self,name):
        self.find_element(locator=self.product_name).send_keys(name)

    def click_filter_button(self):
        self.find_element(locator=self.filter_button).click()

    def click_logout(self):
        self.find_element(locator=self.logout).click()

    def click_reviews(self):
        self.find_element(locator=self.reviews).click()

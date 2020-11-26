from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from urllib.parse import urljoin

import pytest


@pytest.fixture
def sumsung_url(baseurl_option):
    return urljoin(baseurl_option, '/index.php?route=product/product&path=57&product_id=49')


def test_login(sumsung_url, browser):
    browser.get(sumsung_url)
    assert browser.current_url == sumsung_url


def test_carts_img(sumsung_url, browser):
    browser.get(sumsung_url)
    buttons = browser.find_elements_by_css_selector('a.thumbnail')
    for button in buttons:
        button.click()

        butt = browser.find_element_by_xpath('//div/button')
        butt.click()


@pytest.mark.parametrize(
    'xpath, expected_text',
    [
        ('//div[2]/h1', 'Samsung Galaxy Tab 10.1'),
        ('//li[1]/h2', '$241.99')
    ]
)
def test_items(sumsung_url, browser, xpath, expected_text):
    browser.get(sumsung_url)
    items = browser.find_element_by_xpath(xpath)
    assert items.text == expected_text


def test_add_to_cart(sumsung_url, browser):
    browser.get(sumsung_url)
    button = browser.find_element_by_xpath('//div[2]/div[2]/div/button')
    button.click()

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from urllib.parse import urljoin

import pytest


def test_login(login_url, browser):
    browser.get(login_url)
    assert browser.current_url == login_url


@pytest.mark.parametrize(
    'xpath, expected_text',
    [
        ('//h2[contains(text(),"New")]', 'New Customer'),
        ('//h2[contains(text(),"Returning")]', 'Returning Customer')
    ]
)
def test_label_text(xpath, expected_text, login_url, browser):
    browser.get(login_url)
    assert browser.current_url == login_url
    browser.implicitly_wait(15)
    label = browser.find_element_by_xpath(xpath)
    assert label.text == expected_text


def test_new_customer_continue_click(login_url, browser):
    browser.get(login_url)
    assert browser.current_url == login_url
    browser.implicitly_wait(15)
    button = browser.find_element_by_xpath("//div[1]/div/a")
    button.click()
    WebDriverWait(browser, 5).until(EC.url_changes(login_url))


def test_customer_login_click(login_url, browser):
    browser.get(login_url)
    assert browser.current_url == login_url
    browser.implicitly_wait(15)
    button = browser.find_element_by_xpath("//div[2]/div/form/input")
    button.click()


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pytest


def test_login_admin(admin_url, browser):
    browser.get(admin_url)
    assert browser.current_url == admin_url
    browser.implicitly_wait(15)
    login_button = browser.find_element_by_css_selector('.btn.btn-primary')
    login_button.click()
    WebDriverWait(browser, 5).until(EC.url_changes(admin_url))


def test_forgot_login_admin(admin_url, browser):
    browser.get(admin_url)
    assert browser.current_url == admin_url
    browser.implicitly_wait(15)
    forgot_link = browser.find_element(By.LINK_TEXT, 'Forgotten Password')
    forgot_link.click()
    WebDriverWait(browser, 5).until(EC.url_changes(admin_url))


@pytest.mark.parametrize(
    'xpath, expected_text',
    [
        ('.//h1[1]', 'Please enter your login details.'),
        ('.//div[1]/label', 'Username'),
        ('.//div[2]/label', 'Password'),
    ]
)
def test_label_text(xpath, expected_text, admin_url, browser):
    browser.get(admin_url)
    assert browser.current_url == admin_url
    browser.implicitly_wait(15)
    label = browser.find_element_by_xpath(xpath)
    assert label.text == expected_text


def test_inputs(admin_url, browser):
    browser.get(admin_url)
    assert browser.current_url == admin_url
    browser.implicitly_wait(15)
    username = browser.find_element_by_id('input-username')
    password = browser.find_element_by_id('input-password')

    assert username.get_attribute('value') == 'demo'
    assert password.get_attribute('value') == 'demo'

    username.clear()
    password.clear()

    username.send_keys('123')
    password.send_keys('---')

    assert username.get_attribute('value') == '123'
    assert password.get_attribute('value') == '---'


def test_login_admin(admin_url, browser):
    browser.get(admin_url)
    assert browser.current_url == admin_url
    browser.implicitly_wait(15)
    login_button = browser.find_element_by_css_selector('.btn.btn-primary')
    login_button.click()
    WebDriverWait(browser, 5).until(EC.url_changes(admin_url))

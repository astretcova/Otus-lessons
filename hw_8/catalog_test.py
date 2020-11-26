from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urljoin
import time
import pytest


@pytest.fixture
def catalog_url(baseurl_option):
    return urljoin(baseurl_option, '/index.php?route=product/category&path=20')


def test_login_catalog(catalog_url, browser):
    browser.get(catalog_url)
    assert browser.current_url == catalog_url


@pytest.mark.parametrize(
    'xpath, expected_text',
    [
        ('//div/h2', 'Desktops'),
        ('//div/h3', 'Refine Search')
    ]
)
def test_text_main_page(xpath, expected_text, catalog_url, browser):
    browser.get(catalog_url)
    label = browser.find_element_by_xpath(xpath)
    assert label.text == expected_text


@pytest.mark.parametrize(
    'xpath, expected_text',
    [
        ('//a[text()="MacBook"]', 'MacBook'),
        ('//a[text()="iPhone"]', 'iPhone'),
        ('//a[contains(text(), "Apple Cinema 30")]', 'Apple Cinema 30"'),
        ('//a[text()="Canon EOS 5D"]', "Canon EOS 5D")
    ]
)
def test_label_text_main_page(xpath, expected_text, catalog_url, browser):
    browser.get(catalog_url)
    label = browser.find_element_by_xpath(xpath)
    assert label.text == expected_text


def test_add_to_wish_list(catalog_url, browser):
    browser.get(catalog_url)
    buttons = browser.find_elements_by_xpath('//div[2]/div[2]/button[2]')
    for button in buttons:
        actions = ActionChains(browser)
        actions.move_to_element(button).perform()
        button.click()
        time.sleep(5)

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from html import escape


def test_first(baseurl_option, browser):
    browser.get(baseurl_option)
    assert browser.current_url == baseurl_option
    browser.find_element_by_id("cart")


def test_items(baseurl_option, browser):
    browser.get(baseurl_option)
    button = browser.find_element_by_css_selector('#cart>button')
    button.click()
    message = browser.find_element_by_css_selector('p.text-center')
    assert "Your shopping cart is empty!" == message.text


@pytest.mark.parametrize(
    'xpath, expected_text',
    [
        ('//a[text()="MacBook"]', 'MacBook'),
        ('//a[text()="iPhone"]', 'iPhone'),
        ('//a[contains(text(), "Apple Cinema 30")]', 'Apple Cinema 30"'),
        ('//a[text()="Canon EOS 5D"]', "Canon EOS 5D")
    ]
)
def test_label_text_main_page(xpath, expected_text, baseurl_option, browser):
    browser.get(baseurl_option)
    label = browser.find_element_by_xpath(xpath)
    assert label.text == expected_text


def test_carts_add(baseurl_option, browser):
    browser.get(baseurl_option)
    buttons = browser.find_elements_by_xpath('//div[3]/button[1]')
    for button in buttons:
        button.click()
    WebDriverWait(browser, 5).until(EC.url_changes(baseurl_option))



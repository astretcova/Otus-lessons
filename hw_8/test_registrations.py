from urllib.parse import urljoin
import pytest
import time
import random
import string


def get_random_string(length = 6):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@pytest.fixture
def register_url(baseurl_option):
    return urljoin(baseurl_option, '/index.php?route=account/register')


@pytest.fixture
def login_url(baseurl_option):
    return urljoin(baseurl_option, '/index.php?route=account/login')


def test_login_register(register_url, browser):
    browser.get(register_url)
    assert browser.current_url == register_url
    browser.implicitly_wait(15)

    input1 = browser.find_element_by_css_selector("[name='firstname']")
    input1.send_keys(get_random_string())
    input2 = browser.find_element_by_css_selector("[name='lastname']")
    input2.send_keys(get_random_string())
    input3 = browser.find_element_by_css_selector("[name='email']")
    input3.send_keys(f"{get_random_string()}@{get_random_string()}.ru")
    input4 = browser.find_element_by_css_selector("[name='telephone']")
    input4.send_keys("123123")
    input4 = browser.find_element_by_css_selector("[name='password']")
    input4.send_keys("123123")
    input4 = browser.find_element_by_css_selector("[name='confirm']")
    input4.send_keys("123123")
    click = browser.find_element_by_css_selector('[name="agree"]')
    click.click()
    button = browser.find_element_by_css_selector("[value='Continue']")
    button.click()
    browser.implicitly_wait(5)
    lable = browser.find_element_by_xpath('//*[@id="content"]/h1')
    assert lable.text == "Your Account Has Been Created!"
    time.sleep(5)
    button = browser.find_element_by_xpath("/html/body/div[2]/div/div/div/div/a")
    button.click()


def test_logout_register(login_url, browser):
    browser.get(login_url)
    email = browser.find_element_by_css_selector("[id=input-email]")
    email.send_keys('ivan@mail.ru')
    password = browser.find_element_by_css_selector("[id=input-password]")
    password.send_keys('123123')
    button = browser.find_element_by_xpath("//div[2]/div/form/input")
    button.click()
    browser.implicitly_wait(5)


    button3 = browser.find_element_by_xpath('//div/a[text()="Logout"]')
    button3.click()


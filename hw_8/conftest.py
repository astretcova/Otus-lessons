import pytest
from selenium import webdriver

from urllib.parse import urljoin


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome', choices=['chrome', 'firefox'],
                     help='run specific browser (chrome, firefox)')
    parser.addoption('--baseurl', action='store', default='https://demo.opencart.com/',
                     help='base url to opencart')


@pytest.fixture
def browser_option(request):
    return request.config.getoption("--browser")


@pytest.fixture
def baseurl_option(request):
    return request.config.getoption("--baseurl")


@pytest.fixture
def browser(browser_option):
    TIMEOUT = 5

    if browser_option == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('start-fullscreen')
        #options.add_argument("--headless")
        browser = webdriver.Chrome(chrome_options=options)
        browser.implicitly_wait(TIMEOUT)
        yield browser
        browser.quit()

    if browser_option == 'firefox':
        options = webdriver.FirefoxOptions()
        options.add_argument('start-fullscreen')
        #options.add_argument("--headless")
        browser = webdriver.Firefox(firefox_options=options)
        browser.implicitly_wait(TIMEOUT)
        yield browser
        browser.quit()


@pytest.fixture
def admin_url(baseurl_option):
    return urljoin(baseurl_option, '/admin/')


@pytest.fixture
def register_url(baseurl_option):
    return urljoin(baseurl_option, '/index.php?route=account/register')


@pytest.fixture
def login_url(baseurl_option):
    return urljoin(baseurl_option, '/index.php?route=account/login')

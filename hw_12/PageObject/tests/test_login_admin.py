import pytest


def test_success_login(admin_page):
    admin_page.login('demo', 'demo')
    assert admin_page.driver.title == 'Dashboard'


def test_forgotten_password(admin_page):
    admin_page._forgotten_pass()
    assert admin_page.driver.title == 'Forgot Your Password?'


def test_from_footer_to_home(admin_page):
    admin_page.go_to_home_page()
    assert admin_page.driver.title == 'OpenCart - Open Source Shopping Cart Solution'


def test_check_product(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.expand_catalog()
    admin_page.expand_products()
    admin_page.fill_product_name('Canon')
    admin_page.click_filter_button()
    assert admin_page.driver.title == 'Products'


def test_check_logout(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.click_logout()
    assert admin_page.driver.title == 'Administration'


def test_check_reviews(admin_page):
    admin_page.login('demo', 'demo')
    admin_page.expand_catalog()
    admin_page.click_reviews()
    assert admin_page.driver.title == 'Reviews'

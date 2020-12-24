from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def test_login_admin_and_check_cards(admin_url, browser):
    browser.get(admin_url)
    assert browser.current_url == admin_url
    browser.implicitly_wait(15)
    login_button = browser.find_element_by_css_selector('.btn.btn-primary')
    login_button.click()
    WebDriverWait(browser, 5).until(EC.url_changes(admin_url))
    catalog_menu = browser.find_element_by_xpath('//*[@id="menu-catalog"]/a')
    product_item = browser.find_element_by_xpath('//*[@id="collapse1"]/li[2]/a')

    ActionChains(browser).click(catalog_menu).pause(2).click(product_item).perform()

    WebDriverWait(browser, 5).until(EC.url_contains('/admin/index.php?route=catalog/product'))
    assert browser.find_element_by_xpath('//*[@id="content"]/div[2]/div/div[2]/div/div[1]/h3').text \
           == 'Product List'

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By

BASE_URL = 'https://gcore.com'
PATH = '/hosting'


@pytest.fixture(scope='session')
def open_browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    chrome_browser.get(BASE_URL + PATH)
    chrome_browser.maximize_window()
    chrome_browser.execute_script("window.scrollTo(0, 700)")
    return chrome_browser


@pytest.fixture(scope='session')
def click_price_button(open_browser):
    price_button = open_browser.find_element(By.XPATH, '//*[@class="gc-button gc-button_large"]')
    price_button.click()



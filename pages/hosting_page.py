import allure
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re


class HostingPage(BasePage):
    CURRENCY_USD_BUTTON = '//*[@id="right"]'
    CURRENCY_EUR_BUTTON = '//*[@id="left"]'
    PRICE_BUTTON = '//*[@class="gc-button gc-button_large"]'
    PRICE_RIGHT_SLIDER = '//*[@class="multi-range-slider__thumb multi-range-slider__thumb_right"]'
    MIN_PRICE_INPUT_FIELD = '//*[@type="number"]'
    MAX_PRICE_INPUT_FIELD = '(//*[@type="number"])[2]'
    SHOW_MORE_BUTTON = "//button[contains(@class, 'gc-button') and contains(text(), 'Show more')]"

    def __init__(self, open_browser):
        super().__init__(open_browser)

    @allure.feature('Verifying that the Dedicated and Virtual Servers tab is clickable')
    def click_server_tab(self, open_browser, server_type):
        with allure.step('Find server tab'):
            server_tab = open_browser.find_element(By.XPATH, f'//*[@value="{server_type}"]')
        with allure.step('Click server tab'):
            server_tab.click()
        with allure.step('Verify that server tab is selected'):
            assert server_tab.is_selected(), f"{server_type} servers tab is not active"

    @allure.feature('Verifying that the currency switching radiobutton is clickable')
    def switch_to_currency(self, open_browser):
        with allure.step('Find and click usd currency button'):
            usd_currency_button = open_browser.find_element(By.XPATH, self.CURRENCY_USD_BUTTON)
            usd_currency_button.click()
        with allure.step('Verify that button is selected'):
            assert usd_currency_button.is_selected(), f"{usd_currency_button} servers tab is not active"
        with allure.step('Find and click euro currency button'):
            eur_currency_button = open_browser.find_element(By.XPATH, self.CURRENCY_EUR_BUTTON)
            eur_currency_button.click()
        with allure.step('Verify that button is selected'):
            assert eur_currency_button.is_selected(), f"{eur_currency_button} servers tab is not active"

    @allure.feature('Verifying that the price change slider is clickable')
    def switch_max_price_by_slider(self, open_browser):
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        right_slider_price_change = open_browser.find_element(By.XPATH, self.PRICE_RIGHT_SLIDER)
        actions = ActionChains(open_browser)
        actions.click_and_hold(right_slider_price_change).move_by_offset(-150, 0).release().perform()
        actions.click_and_hold(right_slider_price_change).move_by_offset(150, 0).release().perform()

    @allure.feature('Verifying that the minimum price entry field can be filled in')
    def set_min_price_by_field(self, open_browser, price):
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        price_input_field_min.clear()
        price_input_field_min.send_keys((str(price)))

    @allure.feature('Verifying that the price in minimum price entry field is entered correctly')
    def get_min_price_by_field(self, open_browser, expected_price):
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        actual_price = price_input_field_min.get_attribute('value')
        assert actual_price == str(expected_price), f"Expected price {expected_price}, but got {actual_price}"

    @allure.feature('Verifying that the maximum price entry field can be filled in')
    def set_max_price_by_field(self, open_browser, price):
        price_input_field_max = open_browser.find_element(By.XPATH, self.MAX_PRICE_INPUT_FIELD)
        price_input_field_max.clear()
        price_input_field_max.send_keys((str(price)))

    @allure.feature('Verifying that the price in maximum price entry field is entered correctly')
    def get_max_price_by_field(self, open_browser, expected_price):
        price_input_field_max = open_browser.find_element(By.XPATH, self.MAX_PRICE_INPUT_FIELD)
        actual_price = price_input_field_max.get_attribute('value')
        assert actual_price == str(expected_price), f"Expected price {expected_price}, but got {actual_price}"

    @allure.feature('Verifying Virtual servers minimum euro price')
    def virtual_servers_min_euro_price(self, open_browser):
        open_browser.refresh()
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        assert price_input_field_min.get_attribute('value') == '3', 'Invalid Virtual servers minimum euro price'

    @allure.feature('Verifying Virtual servers minimum usd price')
    def virtual_servers_min_usd_price(self, open_browser):
        switch_to_currency_usd = open_browser.find_element(By.XPATH, self.CURRENCY_USD_BUTTON)
        switch_to_currency_usd.click()
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        assert price_input_field_min.get_attribute('value') == '3', 'Invalid Virtual servers minimum usd price'

    @allure.feature('Verifying Virtual servers maximum usd price')
    def virtual_servers_max_usd_price(self, open_browser):
        price_input_field_max = open_browser.find_element(By.XPATH, self.MAX_PRICE_INPUT_FIELD)
        assert price_input_field_max.get_attribute('value') == '117', 'Invalid Virtual servers maximum usd price'

    @allure.feature('Verifying Virtual servers maximum euro price')
    def virtual_servers_max_euro_price(self, open_browser):
        switch_to_currency_eur = open_browser.find_element(By.XPATH, '//*[@id="left"]')
        switch_to_currency_eur.click()
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_max = open_browser.find_element(By.XPATH, self.MAX_PRICE_INPUT_FIELD)
        assert price_input_field_max.get_attribute('value') == '97', 'Invalid Virtual servers maximum euro price'

    @allure.feature('Verifying Dedicated servers minimum euro price')
    def dedicated_servers_min_euro_price(self, open_browser):
        open_browser.refresh()
        dedicated_server_tab = open_browser.find_element(By.XPATH, f'//*[@value="dedicated"]')
        dedicated_server_tab.click()
        WebDriverWait(open_browser, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.price-card span.gc-text_36"))
        )
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        assert price_input_field_min.get_attribute('value') == '89', 'Invalid Dedicated servers minimum euro price'

    @allure.feature('Verifying Dedicated servers minimum usd price')
    def dedicated_servers_min_usd_price(self, open_browser):
        switch_to_currency_usd = open_browser.find_element(By.XPATH, self.CURRENCY_USD_BUTTON)
        switch_to_currency_usd.click()
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        assert price_input_field_min.get_attribute('value') == '93', 'Invalid Dedicated servers minimum usd price'

    @allure.feature('Verifying Dedicated servers maximum usd price')
    def dedicated_servers_max_usd_price(self, open_browser):
        price_input_field_max = open_browser.find_element(By.XPATH, self.MAX_PRICE_INPUT_FIELD)
        assert price_input_field_max.get_attribute('value') == '1724', 'Invalid Dedicated servers maximum usd price'

    @allure.feature('Verifying Dedicated servers maximum euro price')
    def dedicated_servers_max_euro_price(self, open_browser):
        switch_to_currency_eur = open_browser.find_element(By.XPATH, '//*[@id="left"]')
        switch_to_currency_eur.click()
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_max = open_browser.find_element(By.XPATH, self.MAX_PRICE_INPUT_FIELD)
        assert price_input_field_max.get_attribute('value') == '1482', 'Invalid Dedicated servers maximum euro price'

    @allure.feature('Verifying cards in certain range')
    def price_card(self, open_browser):
        open_browser.refresh()
        price_button = open_browser.find_element(By.XPATH, self.PRICE_BUTTON)
        price_button.click()
        price_input_field_min = open_browser.find_element(By.XPATH, self.MIN_PRICE_INPUT_FIELD)
        price_input_field_min.clear()
        price_input_field_min.send_keys((str(85)))
        show_more_button = open_browser.find_element(By.XPATH, self.SHOW_MORE_BUTTON)
        show_more_button.click()
        price_elements = open_browser.find_elements(By.CSS_SELECTOR, "div.price-card span.gc-text_36")

        all_prices_in_range = True
        for price_element in price_elements:
            price_text = price_element.text.strip()
            price_match = re.search(r'€(\d+)', price_text)
            if price_match:
                price = int(price_match.group(1))
                if not (85 <= price <= 97):
                    all_prices_in_range = False
                    print(f"Price {price} not in the range 85-97 euro.")
            else:
                all_prices_in_range = False
                print("Failed to extract the price from the text:", price_text)

        if all_prices_in_range:
            print("All prices are in the range of 85 to 97 euro.")
        else:
            print("Some prices are not in the range of 85 to 97 euro.")









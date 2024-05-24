import pytest
from pages.hosting_page import HostingPage


@pytest.mark.parametrize("server_type", ["dedicated", "vps"])
def test_server_tab_currency_price_slider(open_browser, server_type):
    server = HostingPage(open_browser)
    server.click_server_tab(open_browser, server_type)
    server.switch_to_currency(open_browser)
    server.switch_max_price_by_slider(open_browser)


@pytest.mark.parametrize("price", [5, 10, 15])
def test_set_min_price_by_field(open_browser, price):
    set_price = HostingPage(open_browser)
    set_price.set_min_price_by_field(open_browser, price=price)
    set_price.get_min_price_by_field(open_browser, expected_price=price)


@pytest.mark.parametrize("price", [50, 60, 70])
def test_set_max_price_by_field(open_browser, price):
    set_price = HostingPage(open_browser)
    set_price.set_max_price_by_field(open_browser, price=price)
    set_price.get_max_price_by_field(open_browser, expected_price=price)


def test_virtual_servers_min_max_euro_usd_price(open_browser):
    set_price = HostingPage(open_browser)
    set_price.virtual_servers_min_euro_price(open_browser)
    set_price.virtual_servers_min_usd_price(open_browser)
    set_price.virtual_servers_max_usd_price(open_browser)
    set_price.virtual_servers_max_euro_price(open_browser)


def test_dedicated_servers_min_max_euro_usd_price(open_browser):
    set_price = HostingPage(open_browser)
    set_price.dedicated_servers_min_euro_price(open_browser)
    set_price.dedicated_servers_min_usd_price(open_browser)
    set_price.dedicated_servers_max_usd_price(open_browser)
    set_price.dedicated_servers_max_euro_price(open_browser)


def test_price_card(open_browser):
    set_price = HostingPage(open_browser)
    set_price.price_card(open_browser)







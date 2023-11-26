from hw5.pages.main import *
from hw5.pages.elements.product import *


def test_main_page_title(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_title_contain(MainPage.TITLE)


def test_main_page_logo(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.LOGO)


def test_main_page_goods(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.SLIDE_SHOW)


def test_main_page_cart(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.CART)


def test_main_page_search(driver, base_url):
    driver.get(base_url)
    MainPage(driver).wait_element(MainPage.SEARCH)


def test_add_product_to_cat(driver, base_url):
    driver.get(base_url)
    selected_product = ProductPage(driver).add_to_cart()
    item_product = ProductPage(driver).check_item_name()
    assert selected_product == item_product

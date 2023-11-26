from hw5.pages.catalog import *


def test_catalog_page_title(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    CatalogPage(driver).wait_title_contain(CatalogPage.TITLE)


def test_catalog_page_description(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    CatalogPage(driver).wait_element(CatalogPage.DESCRIPTION_FIELD)


def test_catalog_page_image(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    CatalogPage(driver).wait_element(CatalogPage.IMAGE_FIELD)


def test_catalog_page_shop_logo(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    CatalogPage(driver).wait_element(CatalogPage.LOGO)


def test_catalog_page_goods_groups(driver, base_url):
    driver.get(f'{base_url}{CatalogPage.ADD_URL}')
    CatalogPage(driver).wait_element(CatalogPage.GOODS_GROUPS)

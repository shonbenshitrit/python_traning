import time
import unittest

from selenium.webdriver.common.by import By

from projectEbay.pages.productPage import productPage
from projectEbay.pages.searchPage import searchPage
from projectEbay.tests.baseProjectSelenium import baseProjectSelenium
from projectEbay.tests.globals import url, searchTerm, key_word, url_page_product


class test_priceProduct(unittest.TestCase):
    def test_priceProduct(self):
        base = baseProjectSelenium()
        driver = base.selenium_start(url)
        search_page = searchPage(driver)
        product_page = productPage(driver)
        search_page.searchItem(searchTerm)
        time.sleep(3)

        product_link = driver.find_element(By.PARTIAL_LINK_TEXT, "New GPS Smart Watch Men Pro HD Screen")
        url_page_product = product_link.get_attribute("href")
        product_link.click()
        driver.get(url_page_product)

        price_watch = product_page.check_product_price()
        assert  price_watch == "292.25", "not the right price"

        base.selenium_end(driver)
import time
import unittest

from projectEbay.pages.searchPage import searchPage
from projectEbay.tests.baseProjectSelenium import baseProjectSelenium
from projectEbay.tests.globals import url, searchTerm, key_word


class test_sortingFreeShipment(unittest.TestCase):
    def test_sorting(self):
        base = baseProjectSelenium()
        driver = base.selenium_start(url)
        search_page = searchPage(driver)
        search_page.searchItem(searchTerm)
        time.sleep(3)
        search_page.sorting()
        text_to_check = search_page.check_sorting()
        assert text_to_check == "Free International Shipping", "not showing - Free International Shipping"

        base.selenium_end(driver)
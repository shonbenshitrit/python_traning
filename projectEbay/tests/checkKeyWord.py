import time
import unittest

from projectEbay.pages.searchPage import searchPage
from projectEbay.tests.baseProjectSelenium import baseProjectSelenium
from projectEbay.tests.globals import url, searchTerm, key_word, ref


class test_checkKeyWord(unittest.TestCase):
    def test_KeyWord(self):
        base = baseProjectSelenium()
        driver = base.selenium_start(url)
        search_page = searchPage(driver)
        search_page.searchItem(searchTerm)
        time.sleep(3)
        search_page.find_key_word(key_word, ref)

        base.selenium_end(driver)
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

from pages.base import Base

# CSS LOCATORS
btn_search_data = ".search-input button[type='submit']"
btn_sitewide_search = ".site-search .field .btn-search"
option_selected = "#field-order-by option[selected='selected']"


# ELEMENT ID'S
site_wide_search = "field-sitewide-search"


class Home(Base):

    def __init__(self, logger, directory, base_url=r'http://localhost/',
                 driver=None, driver_wait=10, delay_secs=0):
        super(Home, self).__init__(logger, directory, base_url,
                                   driver, driver_wait, delay_secs)

    def enter_search_term(self, search_term):
        xpath = "//input[@name='q' and @class='search']"
        element = self.driver.find_element_by_xpath(xpath)

        element.send_keys(search_term)

    def enter_site_search_term(self, search_term):
        element = self.driver.find_element_by_id(site_wide_search)

        element.send_keys(search_term)

    def click_btn_search_data(self):
        element = self.driver.find_element_by_css_selector(btn_search_data)
        element.click()

    def click_btn_site_wide_search(self):
        element = self.driver.find_element_by_css_selector(btn_sitewide_search)
        element.click()

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from pages.base import Base

# CSS LOCATORS
btn_search_data = ".search-input button[type='submit']"
option_selected = "#field-order-by option[selected='selected']"

# ELEMENT ID'S
ddl_order_by = "field-order-by"


class Groups(Base):

    def __init__(self, logger, directory, base_url=r'http://localhost/',
                 driver=None, driver_wait=10, delay_secs=0):
        super(Groups, self).__init__(logger, directory, base_url,
                                     driver, driver_wait, delay_secs)

    def enter_search_term(self, search_term):
        xpath = "//input[@name='q' and @class='search']"
        element = self.driver.find_element_by_xpath(xpath)

        element.send_keys(search_term)

    def click_btn_search_datasets(self):
        element = self.driver.find_element_by_css_selector(btn_search_data)
        element.click()

    def set_sort_order(self, sort_order):

        select = Select(self.driver.find_element_by_id(ddl_order_by))
        select.select_by_visible_text(sort_order)

    def get_sort_order(self):
        element = self.driver.find_element_by_css_selector(option_selected)
        return element.text

import time

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class VenueListPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _click_venue_list = "//span[normalize-space()='Venue List']"

    def open_venue_list(self):
        self.elementClick(self._click_venue_list, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()
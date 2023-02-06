import time

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class GuidesPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _click_guides = "//span[normalize-space()='Guides']"

    _click_download_icons = '//button[@class="btn btn-primary btn-sm btn-icon"]'

    _toggle_view = "//button[@class='btn btn-sm btn-primary view-control']"

    _double_click_to_download_guide = '//div[@class="file-container ng-star-inserted"]'

    # def open_guide(self):
    #     self.elementClick(self._click_guides, locatorType="xpath")
    #     self.hold_wait()
    #     # self.getElements(self._click_download_icons, locatorType="xpath")
    #
    #     self.elementClick(self._click_download_icons, locatorType="xpath")
    #     self.hold_wait()
    #     self.hold_wait()

    def open_guide(self):
        print("Open All Guides")
        self.elementClick(self._click_guides, locatorType="xpath")
        self.hold_wait()
        for dn in self.getElements(self._click_download_icons, locatorType="xpath"):
            dn.click()
            self.hold_wait()


    def toggle_btn(self):
        self.elementClick(self._toggle_view, locatorType="xpath")

    def double_click(self):
        # self.elementClick(self._double_click_to_download_guide, locatorType="xpath")
        self.double_clicks(self._double_click_to_download_guide, locatorType="xpath")

    def double_click_pdf_file_thubmnail(self):
        self.elementClick(self._click_guides, locatorType="xpath")
        self.toggle_btn()
        self.hold_wait()
        self.double_click()
        self.hold_wait()
        self.hold_wait()



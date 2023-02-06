import time

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path


class GroupsPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _left_panel_click_groups = "//span[normalize-space()='Groups']"
    _click_create_group = "//button[normalize-space()='Create group']"
    _group_name_field = "//input[@id='mat-input-2']"
    _group_description_field = "//input[@id='mat-input-3']"

    _customer_search_place_holder = "//input[@placeholder='Search']"
    _cus_click_drop = "//mat-select[@role='combobox']"
    _select_customer = "//span[@class='mat-option-text']"
    # _select_customer = "//span[@class='mat-option-text'][normalize-space()='InvenSense-PowerUserGroup']"

    # _select_parent_group = "//span[normalize-space()='Automation_Test_Group']"
    _parent_search_place_holder = "//input[@placeholder='Search']"
    _parent_click_drop = "(//mat-select[@role='combobox'])[2]"
    _select_parent = "//span[@class='mat-option-text'][normalize-space()='Admin-InvenSense-PowerUserGroup']"

    _select_parent_group = "//span[@class='mat-option-text' and contains(text(), 'test grp')]"

    _select_click = '//mat-select[@role="combobox"][2]'
    # _select_click = "//mat-select[@id='mat-select-4']"

    # "//span[@class='mat-select-placeholder ng-tns-c62-126 ng-star-inserted']"
    # _select_parent_group = "//input[@placeholder='Search']"
    # _select_parent_group = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'
    # _select_parent_group = "//div[@class='cdk-overlay-container']"
    # _select_parent_group = '("mat-option[id="mat-option-8"] span[class="mat-option-text"]"))'
    # _click = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'
    _click = "//input[@placeholder='Search']"

    _click_out = "//body"

    _save_grp = "//button[normalize-space()='Save']"

    # def all_grp(self, grp_name, grp_des, parent_name):

    def all_grp(self, grp_name, grp_des, cus_name, dt):
        self.click_left_panel_groups()
        self.click_create_group()
        self.enter_grp_name(grp_name)
        self.enter_grp_description_name(grp_des)

        self.select_customer(cus_name)
        self.click_out()

        self.select_parent_grp(dt)
        # self.click_parent(dt)
        self.click_out()
        # self.scroll_down()
        self.hold_wait()
        self.checkboxes()
        self.hold_wait()
        self.elementClick(self._save_grp, locatorType="xpath")
        self.hold_wait()



    def click_left_panel_groups(self):
        self.elementClick(self._left_panel_click_groups, locatorType="xpath")
        self.hold_wait()

    def click_create_group(self):
        self.elementClick(self._click_create_group, locatorType="xpath")
        self.hold_wait()

    def enter_grp_name(self, grp_name):
        self.sendKeys(grp_name, self._group_name_field, locatorType="xpath")

    def enter_grp_description_name(self, grp_des):
        self.sendKeys(grp_des, self._group_description_field, locatorType="xpath")

    def select_customer(self, cus_name):
        self.elementClick(self._cus_click_drop, locatorType="xpath")
        self.elementClick(self._customer_search_place_holder, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(cus_name, self._customer_search_place_holder, locatorType="xpath")
        self.elementClick(self._select_customer, locatorType="xpath")
        self.hold_wait()

    # def select_parent_grp(self, dt):
    #     # self.sendKeys(self._select_parent_group, locatorType="xpath")
    #     self.hold_wait()
    #     self.elementClick(self._select_click, locatorType="xpath")
    #     self.hold_wait()
    #     # self.elementClick(self._select_parent_group, locatorType="xpath")
    #     self.sendKeys(dt, self._click, locatorType="xpath")
    #     self.hold_wait()

    def select_parent_grp(self, dt):
        self.elementClick(self._parent_click_drop, locatorType="xpath")
        self.elementClick(self._parent_search_place_holder, locatorType="xpath")
        self.hold_wait()
        self.sendKeys(dt, self._parent_search_place_holder, locatorType="xpath")
        self.elementClick(self._select_parent, locatorType="xpath")
        self.hold_wait()

    # def click_parent(self, dt):
    #     # self.elementClick(self._click, locatorType="xpath")
    #     self.sendKeys(dt, self._click, locatorType="xpath")

    def click_out(self):
        self.elementClick(self._click_out, locatorType="xpath")

    _download_grp_csv_file = "//button[normalize-space()='Download csv']"

    def download_grp_csv(self):
        self.click_left_panel_groups()
        self.elementClick(self._download_grp_csv_file, locatorType="xpath")
        self.hold_wait()

    def clear_field(self):
        search_box = self.getElement(locator=self._find_grp, locatorType="xpath")
        search_box.clear()

    _find_grp = "//input[@placeholder='Group Name']"
    _delete_grp = '//button[@class="btn btn-danger btn-sm btn-icon"]'
    _click_delete_pop_up = '//button[@class="btn btn-sm btn-danger"]'

    def delete_group(self, grp_name):
        self.hold_wait()
        self.click_left_panel_groups()
        # self.clear_field()
        self.sendKeys(grp_name, self._find_grp, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._delete_grp, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._click_delete_pop_up, locatorType="xpath")
        self.hold_wait()

    _click_edit_grp = '//button[@class="btn btn-primary btn-sm btn-icon"]'

    def edit_group(self, grp_name):
        # self.clear_field()
        self.sendKeys(grp_name, self._find_grp, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._click_edit_grp, locatorType="xpath")
        self.scroll_down()
        self.hold_wait()
        self.hold_wait()
        self.elementClick(self._save_grp, locatorType="xpath")
        self.hold_wait()
        self.hold_wait()
        self.hold_wait()

    # _checkbox_venue_list = "(//div[@class='mat-checkbox-inner-container'])[6]"
    # _checkbox_coursa_survey_app = "(//div[@class='mat-checkbox-inner-container'])[13]"
    # _checkbox_coursa_venue_app = "(//div[@class='mat-checkbox-inner-container'])[18]"
    # _checkbox_coursa_venue_dashboard = "(//div[@class='mat-checkbox-inner-container'])[19]"
    # _checkbox_positioning_analytics_dashboard = "(//div[@class='mat-checkbox-inner-container'])[31]"

    _checkbox_venue_list = "//span[@class='mat-checkbox-label']/div[@class='checkbox-label' and contains(text(), 'Venue List')]"
    _checkbox_coursa_survey_app = "//span[@class='mat-checkbox-label']/div[@class='checkbox-label' and contains(text(), 'Coursa Survey App')]"
    _checkbox_coursa_venue_app = "//span[@class='mat-checkbox-label']/div[@class='checkbox-label' and contains(text(), 'Coursa Venue App')]"
    _checkbox_coursa_venue_dashboard = "//span[@class='mat-checkbox-label']/div[@class='checkbox-label' and contains(text(), 'Coursa Venue Dashboard')]"
    _checkbox_positioning_analytics_dashboard = "//span[@class='mat-checkbox-label']/div[@class='checkbox-label' and contains(text(), 'Positioning/Analytics Dashboard')]"




    def checkboxes(self):
        self.scroll_to_element(self._checkbox_venue_list, locatorType="xpath")
        self.elementClick(self._checkbox_venue_list, locatorType="xpath")

        self.scroll_to_element(self._checkbox_coursa_survey_app, locatorType="xpath")
        self.elementClick(self._checkbox_coursa_survey_app, locatorType="xpath")

        self.scroll_to_element(self._checkbox_coursa_venue_app, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._checkbox_coursa_venue_app, locatorType="xpath")

        self.scroll_to_element(self._checkbox_coursa_venue_dashboard, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._checkbox_coursa_venue_dashboard, locatorType="xpath")
        self.hold_wait()

        self.scroll_to_element(self._checkbox_positioning_analytics_dashboard, locatorType="xpath")
        self.elementClick(self._checkbox_positioning_analytics_dashboard, locatorType="xpath")
        self.hold_wait()



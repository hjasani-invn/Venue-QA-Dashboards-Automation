import time

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging
import os.path



class UserHomePage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _download_bulk_csv = "//button[normalize-space()='Download csv']"

    _groups_field = "//input[@placeholder='Group']"
    _edit_english_user_btn = "//tbody/tr[2]/td[6]/button[1]"
    #_edit_box_first_name_field = "//input[@id='mat-input-8']"
    #_edit_box_first_name_field = "//input[@id='mat-input-0']" # xpath
    #_edit_box_first_name_field = "mat-input-0"  # id
    _edit_box_first_name_field = '//input[@name="first-name"]'  # xpath
    _save_updated_uder = "//button[normalize-space()='Save']"

    # delete users
    _click_delete_icon = '//button[@class="btn btn-danger btn-sm btn-icon"]'
    _pop_up_choose_delete_user = "//button[normalize-space()='Delete user']"

    def download_bulk_csv_btn(self):
        self.elementClick(self._download_bulk_csv, locatorType="xpath")
        self.waitForElement(locator=self._download_bulk_csv, locatorType="xpath")

    def verify_download(self):
        # check if file downloaded file path exists
        while not os.path.exists('C:\\Users\\hjasani\\Downloads'):
            print("path is not valid")
            time.sleep(2)
        # check file
        #file_name = "users_2022-10-14T16_51_42.266Z.csv"
        file_name = "users_2022-10-14T16_51_42.266Z.csv"
        if os.path.isfile(f'C:\\Users\\hjasani\\users_2022-10-14T16_51_42.266Z.csv'):
            print("File download is completed")
        else:
            print("File download is not completed")
        self.hold_wait()

    def filter_grp(self, grp_name):
        self.sendKeys(grp_name, self._groups_field, locatorType="xpath")
        self.hold_wait()

    def edit_user_btn(self):
        self.elementClick(self._edit_english_user_btn, locatorType="xpath")

    def clear_fileds(self):
        first_name = self.getElement(locator=self._edit_box_first_name_field, locatorType="xpath")
        first_name.clear()
        self.hold_wait()

    def first_name_new_data(self, first_name_new):
        self.sendKeys(first_name_new, self._edit_box_first_name_field, locatorType="xpath")
        self.hold_wait()

    def save(self):
        self.elementClick(self._save_updated_uder, locatorType="xpath")

    def edit_user(self, first_name_new):
        self.edit_user_btn()
        # self.clear_fileds()
        self.backspace_clear(self._groups_field, locatorType="xpath")
        self.first_name_new_data(first_name_new)
        self.save()
        self.hold_wait()

    def click_bin_icon(self):
        self.elementClick(self._click_delete_icon, locatorType="xpath")

    def choose_delete_btn(self):
        self.elementClick(self._pop_up_choose_delete_user, locatorType="xpath")

    _number_users = "//tbody[@role='rowgroup']//tr"
    _page_size_click = "//div[@id='mat-select-value-1']"
    _page_size_set = "//span[@class='mat-option-text'][normalize-space()='50']"

    def delete_user(self):
        self.move_to_element(self._page_size_set, locatorType="xpath")
        self.elementClick(self._page_size_set, locatorType="xpath")
        self.hold_wait()
        self.move_to_element(self._groups_field, locatorType="xpath")
        self.hold_wait()

        self.filter_grp("Automation_Test_Group")
        self.hold_wait()
        counte = []
        counte = self.getElements(self._number_users, locatorType="xpath")
        for cou in counte:
            print(cou)
            print(f"Number of Users: {len(counte)}")

        i = 0
        while i < len(counte):
            self.backspace_clear(self._groups_field, locatorType="xpath")
            self.filter_grp("Automation_Test_Group")
            self.hold_wait()
            self.click_bin_icon()
            self.choose_delete_btn()
            self.hold_wait()
            i += 1

    _find_range = "//div[@class='paginator-range-label']"
    def del_user_new(self):
        self.filter_grp("Automation_Test_Group")

        self.move_to_element(self._find_range, locatorType="xpath")
        number_of_users_xpath = self.getElement(self._find_range, locatorType="xpath")
        number_of_users_text = number_of_users_xpath.text
        if number_of_users_text == "0 of 0":
            str_number_of_users = number_of_users_text.split(" ")[2]
            int_number_of_users = int(str_number_of_users)
            print(f"----number_of_users: {number_of_users_text}")
            print(f"----str_number_of_users: {str_number_of_users}")
            print(f"----int_number_of_users: {int_number_of_users}")
            print(type(int_number_of_users))
        else:
            str_number_of_users = number_of_users_text.split(" ")[4]
            int_number_of_users = int(str_number_of_users)
            print(f"----number_of_users: {number_of_users_text}")
            print(f"----str_number_of_users: {str_number_of_users}")
            print(f"----int_number_of_users: {int_number_of_users}")
            print(type(int_number_of_users))


        # while int_number_of_users > 0:
        #     self.move_to_element(self._groups_field, locatorType="xpath")
        #     self.backspace_clear(self._groups_field, locatorType="xpath")
        #     self.filter_grp("Automation_Test_Group")
        #     self.hold_wait()
        #     self.click_bin_icon()
        #     self.choose_delete_btn()
        #     self.hold_wait()
        #     int_number_of_users -= 1

        if int_number_of_users > 0:
            for i in range(int_number_of_users+1):
                self.move_to_element(self._groups_field, locatorType="xpath")
                self.backspace_clear(self._groups_field, locatorType="xpath")
                self.filter_grp("Automation_Test_Group")
                self.hold_wait()
                self.click_bin_icon()
                self.choose_delete_btn()
                self.hold_wait()
        else:
            print("No existing users are available")
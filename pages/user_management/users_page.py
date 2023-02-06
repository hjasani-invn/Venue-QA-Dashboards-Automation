import time

import autoit
import pyautogui

import selenium.common.exceptions

from base.selenium_driver import SeleniumDriver

import utilities.custom_logger as cl
import logging


class UserPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _click_create_user_ = "//button[@routerlink='/home/users/create']"  # xpath

    # _user_id_filed = "input[placeholder='User Id']"
    _user_id_filed = "//input[@placeholder='User Id']"
    _first_name_filed = '//input[@placeholder="First Name"]'
    _last_name_filed = '//input[@placeholder="Last Name"]'
    _password_filed = '//input[@placeholder="Password"]'
    _email_filed = '//input[@placeholder="Email"]'

    _cutomer_search_box = "//input[@placeholder='Search']"
    _select_click = '//mat-select[@role="combobox"]'
    _select_customer = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    #_select_customer = "//span[@class='mat-option-text' and contains(text(), ' InvenSense-PowerUserGroup ')]"

    _click_Groups_dropdown = "//ns-filter-select[@label='Groups']"
    # _click_Groups_dropdown = '//ns-filter-select'
    #_check_checkbox = '//span[@class="mat-option-text" and contains(text(), "Admin-Test_Auto-External")]'
    _check_checkbox = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'
    # //mat-select[@id='mat-select-2']
    #  Admin-Test_Auto-External
    # //span[normalize-space()='Admin-Test_Auto-External']
    # _check_checkbox = "//span[normalize-space()='Admin-Test_Auto-External']" # working
    _click_out = "//body"  # xpath, clicked out of all active elements of page
    _click_on_create_users_button = "//button[normalize-space()='Create Users']"

    _click_users_for_new_iteration = "//span[normalize-space()='Users']"

    _snackbar_message = '//snack-bar-container[@role="alert"]'

    _bulk_user_addition_btn = "//button[@class='btn btn-success btn-sm btn-icon ng-star-inserted']"

    _upload_csv_btn = "//button[normalize-space()='Upload .csv']"

    def click_create_user_button(self):
        # self.hold_wait()
        self.elementClick(self._click_create_user_, locatorType="xpath")
        self.hold_wait()

    def add_user_information(self, user_id, first_name, last_name, password, email):
        self.enter_user_id(user_id)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_password(password)
        self.enter_email(email)

        self.customer_selection()

        # self.is_checkbox_selected()

        self.click_group_dropdown()
        self.check_checkbox()
        self.click_out()
        self.final_click_to_add_users()
        # self.wait_for_snackbar_message()
        # self.clear_fields()
        self.click_new_iteration_user()
        self.click_create_user_button()
        # try:
        #     message_text = self.wait_for_snackbar_message()
        #     if 'USERS SUCCESSFULLY CREATED' not in message_text:
        #         return 0, message_text
        #     else:
        #         return 1, message_text
        # except selenium.common.exceptions.TimeoutException:
        #     return 0, 'No User Creation confirmation message raised.'

    def add_user_information_only_without_grp(self, user_id, first_name, last_name, password, email):
        self.enter_user_id(user_id)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_password(password)
        self.enter_email(email)

        self.customer_selection()

        self.final_click_to_add_users()

        self.click_new_iteration_user()
        self.click_create_user_button()


    def bulk_user_addition(self, user_id, first_name, last_name, password, email):
        self.enter_user_id(user_id)
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_password(password)
        self.enter_email(email)
        self.click_group_dropdown()
        self.check_checkbox()
        self.click_out()
        self.click_add_bulk_user_btn()

        self.click_new_iteration_user()
        self.click_create_user_button()

    # def upload_csv(self, csv_file):
    #     # self.click_create_user_button()
    #     self.upload_csv_file(csv_file)
    #     self.hold_wait()
    #     self.final_click_to_add_users()

    def upload_csv(self, csv_file):
        self.upload_csv_file()
        self.hold_wait()
        self.sendcsv(csv_file)
        self.hold_wait()
        self.final_click_to_add_users()

    def enter_user_id(self, user_id):
        # self.hold_wait()
        # self.elementClick(self._user_id_filed, locatorType="css")
        self.sendKeys(user_id, self._user_id_filed, locatorType="xpath")

    def enter_first_name(self, first_name):
        self.sendKeys(first_name, self._first_name_filed, locatorType="xpath")

    def enter_last_name(self, last_name):
        self.sendKeys(last_name, self._last_name_filed, locatorType="xpath")

    def enter_password(self, password):
        self.sendKeys(password, self._password_filed, locatorType="xpath")

    def enter_email(self, email):
        self.sendKeys(email, self._email_filed, locatorType="xpath")

    def customer_selection(self):
        #self.elementClick(self._select_customer, locatorType="xpath")
        self.elementClick(self._select_click, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer, locatorType="xpath")
        self.click_out()

    def click_group_dropdown(self):
        self.elementClick(self._click_Groups_dropdown, locatorType="xpath")

    def check_checkbox(self):
        self.elementClick(self._check_checkbox, locatorType="xpath")
        self.hold_wait()

    # def is_checkbox_selected(self):
    #     verify = self.is_selected(self._check_checkbox, locatorType="xpath")
    #     if not verify == False:
    #         self.check_checkbox()

    def selected(self):
        self.is_select(self._check_checkbox, locatorType="xpath")

    def click_out(self):
        txt = self.elementClick(self._click_out, locatorType="xpath")
        self.hold_wait()

    def final_click_to_add_users(self):
        self.elementClick(self._click_on_create_users_button, locatorType="xpath")
        self.hold_wait()

    def clear_fields(self):
        user_id = self.getElement(locator=self._user_id_filed, locatorType="xpath")
        user_id.clear()

        first_name = self.getElement(locator=self._first_name_filed, locatorType="xpath")
        first_name.clear()

        last_name = self.getElement(locator=self._last_name_filed, locatorType="xpath")
        last_name.clear()

        password = self.getElement(locator=self._password_filed, locatorType="xpath")
        password.clear()

        email = self.getElement(locator=self._email_filed, locatorType="xpath")
        email.clear()

    """
    if user information in not accepeted, then must have to clear all filed - 
    otherwise it will add new user details in same filed
    for now: removed clear filed, instead applied new logic: start new user from scractch-so each filed including 
    checkbox is also brand new instance
    """

    # def wait_for_snackbar_message(self):
    #     self.get_text(locator=self._snackbar_message, locatorType="xpath")

    def click_new_iteration_user(self):
        self.elementClick(self._click_users_for_new_iteration, locatorType="xpath")

    def click_add_bulk_user_btn(self):
        self.elementClick(self._bulk_user_addition_btn, locatorType="xpath")
        self.waitForElement(locator=self._bulk_user_addition_btn, locatorType="xpath")

    # def upload_csv_file(self):
    #     self.hold_wait()
    #     #self.elementClick(self._upload_csv_btn, locatorType="xpath")
    #     self.hold_wait()

    # def sendcsv(self, csv_file):
    #     self.sendKeys(csv_file, self._upload_csv_btn, locatorType="xpath")
    #     self.hold_wait()
    #     # self.final_click_to_add_users()
    #     self.hold_wait()

    def send_data(self):
        try:
            ele_present = self.elementPresenceCheck(self._upload_csv_btn, locatorType="xpath")
            self.elementClick(self._upload_csv_btn, locatorType="xpath")
            self.hold_wait()

            #pyautogui.write("C:\\Users\\hjasani\\PycharmProjects\work\\Admin_Dashboard\\tests\\user_management\\users_template_final.csv")
            #pyautogui.write("C:/Users/hjasani/PycharmProjects/work/Admin_Dashboard/pages/user_management/users_template.csv", interval=0.30)
            # pyautogui.write("C:/Users/hjasani/Downloads/users_template.csv", interval=0.15)
            pyautogui.typewrite("C:\\Users\\hjasani\\OneDrive - tdkgroup\\Desktop\\work\\work\\Admin_Dashboard\\tests\\user_management\\users_template.csv", interval=0.10)
            pyautogui.press('return')
            self.hold_wait()
            self.hold_wait()
            self.final_click_to_add_users()
            self.hold_wait()

        except:
            print("nothing")

    # def over_py(self):
    #     autoit.win_active("Open")
    #     autoit.control_send("Open", "C:\\Users\\hjasani\\PycharmProjects\work\\Admin_Dashboard\\tests\\user_management\\users_template_final.csv")
    #     autoit.control_send("Open", "Edit1", "{ENTER}")
    #     self.hold_wait()
    #     self.hold_wait()
    #     ele = self.elementClick(self._upload_csv_btn, locatorType="xpath")


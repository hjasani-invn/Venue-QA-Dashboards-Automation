import os
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
    # _select_customer = "//span[@class='mat-option-text' and contains(text(), ' InvenSense-PowerUserGroup ')]"

    _click_Groups_dropdown = "//ns-filter-select[@label='Groups']"
    # _click_Groups_dropdown = '//ns-filter-select'
    # _check_checkbox = '//span[@class="mat-option-text" and contains(text(), "Admin-Test_Auto-External")]'
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

        self.customer_selection()

        self.click_group_dropdown()
        self.check_checkbox()
        self.click_out()
        self.click_add_bulk_user_btn()
        self.click_new_iteration_user()
        self.click_create_user_button()


    _user_id_1 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[2]//input[@placeholder='User Id']"
    _first_name_1 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[3]//input[@placeholder='First Name']"
    _last_name_1 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[4]//input[@placeholder='Last Name']"
    _password_1 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[5]//input[@placeholder='Password']"
    _email_1 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[6]//input[@placeholder='Email']"
    _select_click_1 = "(//mat-select[@role='combobox'])[1]"
    _select_customer_1 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_1 = "(//ns-filter-select[@label='Groups'])[1]"
    _check_checkbox_1 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'



    _user_id_2 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[11]//input[@placeholder='User Id']"
    _first_name_2 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[12]//input[@placeholder='First Name']"
    _last_name_2 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[13]//input[@placeholder='Last Name']"
    _password_2 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[14]//input[@placeholder='Password']"
    _email_2 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[15]//input[@placeholder='Email']"
    _select_click_2 = "(//mat-select[@role='combobox'])[3]"
    _select_customer_2 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_2 = "(//ns-filter-select[@label='Groups'])[2]"
    _check_checkbox_2 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'

    def add_bulk_user_english_1(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_1, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_1, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_1, locatorType="xpath")
        self.sendKeys(password, self._password_1, locatorType="xpath")
        self.sendKeys(email, self._email_1, locatorType="xpath")

        self.elementClick(self._select_click_1, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_1, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_1, locatorType="xpath")

        self.elementClick(self._check_checkbox_1, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()

    def add_bulk_user_english_2(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_2, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_2, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_2, locatorType="xpath")
        self.sendKeys(password, self._password_2, locatorType="xpath")
        self.sendKeys(email, self._email_2, locatorType="xpath")

        self.elementClick(self._select_click_2, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_2, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_2, locatorType="xpath")

        self.elementClick(self._check_checkbox_2, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()

    _user_id_3 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[20]//input[@placeholder='User Id']"
    _first_name_3 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[21]//input[@placeholder='First Name']"
    _last_name_3 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[22]//input[@placeholder='Last Name']"
    _password_3 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[23]//input[@placeholder='Password']"
    _email_3 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[24]//input[@placeholder='Email']"
    _select_click_3 = "(//mat-select[@role='combobox'])[5]"
    _select_customer_3 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_3 = "(//ns-filter-select[@label='Groups'])[3]"
    _check_checkbox_3 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'

    _user_id_4 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[29]//input[@placeholder='User Id']"
    _first_name_4 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[30]//input[@placeholder='First Name']"
    _last_name_4 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[31]//input[@placeholder='Last Name']"
    _password_4 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[32]//input[@placeholder='Password']"
    _email_4 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[33]//input[@placeholder='Email']"
    _select_click_4 = "(//mat-select[@role='combobox'])[7]"
    _select_customer_4 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_4 = "(//ns-filter-select[@label='Groups'])[4]"
    _check_checkbox_4 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'

    def add_bulk_user_japanese_1(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_3, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_3, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_3, locatorType="xpath")
        self.sendKeys(password, self._password_3, locatorType="xpath")
        self.sendKeys(email, self._email_3, locatorType="xpath")

        self.elementClick(self._select_click_3, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_3, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_3, locatorType="xpath")

        self.elementClick(self._check_checkbox_3, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()

    def add_bulk_user_japanese_2(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_4, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_4, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_4, locatorType="xpath")
        self.sendKeys(password, self._password_4, locatorType="xpath")
        self.sendKeys(email, self._email_4, locatorType="xpath")

        self.elementClick(self._select_click_4, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_4, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_4, locatorType="xpath")

        self.elementClick(self._check_checkbox_4, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()
        self.hold_wait()


    _user_id_5 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[38]//input[@placeholder='User Id']"
    _first_name_5 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[39]//input[@placeholder='First Name']"
    _last_name_5 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[40]//input[@placeholder='Last Name']"
    _password_5 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[41]//input[@placeholder='Password']"
    _email_5 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[42]//input[@placeholder='Email']"
    _select_click_5 = "(//mat-select[@role='combobox'])[9]"
    _select_customer_5 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_5 = "(//ns-filter-select[@label='Groups'])[5]"
    _check_checkbox_5 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'

    _user_id_6 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[47]//input[@placeholder='User Id']"
    _first_name_6 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[48]//input[@placeholder='First Name']"
    _last_name_6 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[49]//input[@placeholder='Last Name']"
    _password_6 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[50]//input[@placeholder='Password']"
    _email_6 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[51]//input[@placeholder='Email']"
    _select_click_6 = "(//mat-select[@role='combobox'])[11]"
    _select_customer_6 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_6 = "(//ns-filter-select[@label='Groups'])[6]"
    _check_checkbox_6 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'

    def add_bulk_user_korean_1(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_5, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_5, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_5, locatorType="xpath")
        self.sendKeys(password, self._password_5, locatorType="xpath")
        self.sendKeys(email, self._email_5, locatorType="xpath")

        self.elementClick(self._select_click_5, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_5, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_5, locatorType="xpath")

        self.elementClick(self._check_checkbox_5, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()

    def add_bulk_user_korean_2(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_6, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_6, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_6, locatorType="xpath")
        self.sendKeys(password, self._password_6, locatorType="xpath")
        self.sendKeys(email, self._email_6, locatorType="xpath")

        self.elementClick(self._select_click_6, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_6, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_6, locatorType="xpath")

        self.elementClick(self._check_checkbox_6, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()

    _user_id_7 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[56]//input[@placeholder='User Id']"
    _first_name_7 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[57]//input[@placeholder='First Name']"
    _last_name_7 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[58]//input[@placeholder='Last Name']"
    _password_7 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[59]//input[@placeholder='Password']"
    _email_7 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[60]//input[@placeholder='Email']"
    _select_click_7 = "(//mat-select[@role='combobox'])[13]"
    _select_customer_7 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_7 = "(//ns-filter-select[@label='Groups'])[7]"
    _check_checkbox_7 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'


    _user_id_8 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[65]//input[@placeholder='User Id']"
    _first_name_8 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[66]//input[@placeholder='First Name']"
    _last_name_8 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[67]//input[@placeholder='Last Name']"
    _password_8 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[68]//input[@placeholder='Password']"
    _email_8 = "(//table[@aria-describedby='createNewUsersTable']//tbody//tr//th)[69]//input[@placeholder='Email']"
    _select_click_8 = "(//mat-select[@role='combobox'])[15]"
    _select_customer_8 = "//span[@class='mat-option-text' and contains(text(), 'test')]"
    _click_Groups_dropdown_8 = "(//ns-filter-select[@label='Groups'])[8]"
    _check_checkbox_8 = '//span[@class="mat-option-text" and contains(text(), "Automation_Test_Group")]'

    _create_click_user_btn = "//button[contains(text(),'Create Users')]"

    def add_bulk_user_chinese_1(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_7, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_7, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_7, locatorType="xpath")
        self.sendKeys(password, self._password_7, locatorType="xpath")
        self.sendKeys(email, self._email_7, locatorType="xpath")

        self.elementClick(self._select_click_7, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_7, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_7, locatorType="xpath")

        self.elementClick(self._check_checkbox_7, locatorType="xpath")
        self.click_out()
        self.click_add_bulk_user_btn()

    def add_bulk_user_chinese_2(self, user_id, first_name, last_name, password, email):
        self.sendKeys(user_id, self._user_id_8, locatorType="xpath")
        self.sendKeys(first_name, self._first_name_8, locatorType="xpath")
        self.sendKeys(last_name, self._last_name_8, locatorType="xpath")
        self.sendKeys(password, self._password_8, locatorType="xpath")
        self.sendKeys(email, self._email_8, locatorType="xpath")

        self.elementClick(self._select_click_8, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._select_customer_8, locatorType="xpath")
        self.click_out()

        self.elementClick(self._click_Groups_dropdown_8, locatorType="xpath")

        self.elementClick(self._check_checkbox_8, locatorType="xpath")
        self.click_out()
        self.move_to_element(self._create_click_user_btn, locatorType="xpath")
        self.hold_wait()
        self.elementClick(self._create_click_user_btn, locatorType="xpath")
        self.hold_wait()

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
        # self.elementClick(self._select_customer, locatorType="xpath")
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

            # pyautogui.write("C:\\Users\\hjasani\\PycharmProjects\work\\Admin_Dashboard\\tests\\user_management\\users_template_final.csv")
            # pyautogui.write("C:/Users/hjasani/PycharmProjects/work/Admin_Dashboard/pages/user_management/users_template-1.csv", interval=0.30)
            # pyautogui.write("C:/Users/hjasani/Downloads/users_template-1.csv", interval=0.15)
            # pyautogui.typewrite("C:\\Users\\hjasani\\OneDrive - tdkgroup\\Desktop\\work\\work\\Admin_Dashboard\\tests\\user_management\\users_template-1.csv", interval=0.10)
            # file_name = "users_template-1.csv"
            # current_dir_path = os.path.abspath(os.curdir)
            # join_path = os.path.join(current_dir_path, file_name)
            # path_to_go = join_path
            # print(f"--------{path_to_go}---------")
            # pyautogui.typewrite(path_to_go, interval=0.10)

            ROOT_DIR = os.path.dirname(os.path.abspath(__file__))  # This is your Project Root
            print(ROOT_DIR)
            CONFIG_PATH = os.path.join(ROOT_DIR, 'users_template.csv')
            print(CONFIG_PATH)
            pyautogui.typewrite(CONFIG_PATH, interval=0.10)

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

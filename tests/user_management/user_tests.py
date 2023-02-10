import os
import unittest

import pytest

from base.selenium_driver import SeleniumDriver
from pages.user_management.user_home_page import UserHomePage
from pages.user_management.users_page import UserPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class UserTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.userpage = UserPage(self.driver)
        self.loginpage = LoginPage(self.driver)
        self.userhomepage = UserHomePage(self.driver)
        self.seleniumdriverpage = SeleniumDriver(self.driver)

    @pytest.mark.order(4)
    def test_3_2_7_delete_users_if_available(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        # self.userhomepage.delete_user()
        self.userhomepage.del_user_new()

    @pytest.mark.order(5)
    def test_3_2_1_click_new_user(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.userpage.click_create_user_button()

    @pytest.mark.order(6)
    def test_3_2_1_1_add_user_english(self):
        self.userpage.add_user_information("new_englishTest", "new_Test", "new_Test", "new_tdka",
                                           "new_english01@tdk.com")

    @pytest.mark.order(7)
    def test_3_2_1_2_add_user_japanese(self):
        self.userpage.add_user_information("new_JapaneseUser001", "new_日本語", "new_名前", "new_password123",
                                           "new_日本語.名前@tdk.com")

    @pytest.mark.order(8)
    def test_3_2_1_3_add_user_korean(self):
        self.userpage.add_user_information("new_KoreanUser011", "new_한국", "new_이름", "new_password123",
                                           "new_한국.이름@tdk.com")

    @pytest.mark.order(9)
    def test_3_2_1_4_add_user_chinese(self):
        self.userpage.add_user_information("new_ChineseUser001", "new_中文", "new_名", "new_password123",
                                           "new_中文.名@tdk.com")

    @pytest.mark.order(10)
    def test_3_2_2_manually_add_user_error_checks(self):
        "3.2.2. Manually Add User – Error Checks"

        "missing user-id"
        self.userpage.add_user_information("", "new_Test", "new_Test", "new_tdka",
                                           "new_english01@tdk.com")

        "missing first-name"
        self.userpage.add_user_information("new_englishTest", "", "new_Test", "new_tdka",
                                           "new_english01@tdk.com")

        "missing last-name"
        self.userpage.add_user_information("new_englishTest", "new_Test", "", "new_tdka",
                                           "new_english01@tdk.com")

        "missing password"
        self.userpage.add_user_information("new_englishTest", "new_Test", "new_Test", "",
                                           "new_english01@tdk.com")

        "missing email"
        self.userpage.add_user_information("new_englishTest", "new_Test", "new_Test", "new_tdka",
                                           "")

        "missing groups"
        self.userpage.add_user_information_only_without_grp("new_englishTest", "new_Test", "new_Test", "new_tdka",
                                                            "new_english01@tdk.com")

    # @pytest.mark.order(11)
    # def test_3_2_3_manually_add_user_bulk_addition(self):
    #     " after adding user information, click on + btn to enable new empty row "
    #
    #     self.userpage.bulk_user_addition("new_englishTest_1", "new_Test_1", "new_Test_1", "new_tdka_1",
    #                                      "new_english01@tdk.com")
    #     self.userpage.bulk_user_addition("new_englishTest_2", "new_Test_2", "new_Test_2", "new_tdka_2",
    #                                      "new_english02@tdk.com")
    #
    #     self.userpage.bulk_user_addition("new_JapaneseUser001", "new_日本語", "new_名前", "new_password123",
    #                                      "new_日本語.名前@tdk.com")
    #
    #     self.userpage.bulk_user_addition("new_KoreanUser011", "new_한국", "new_이름", "new_password123",
    #                                      "new_한국.이름@tdk.com")
    #
    #     self.userpage.bulk_user_addition("new_ChineseUser001", "new_中文", "new_名", "new_password123",
    #                                      "new_中文.名@tdk.com")

    @pytest.mark.order(11)
    def test_3_2_3_manually_add_user_bulk_addition(self):
        self.userpage.add_bulk_user_english_1("bulk_englishTest_1", "bulk_Test_1", "bulk_Test_1", "bulk_tdka_1",
                                          "bulk_english01@tdk.com")
        self.userpage.add_bulk_user_english_2("bulk_englishTest_2", "bulk_Test_2", "bulk_Test_2", "bulk_tdka_2",
                                          "bulk_english02@tdk.com")

        self.userpage.add_bulk_user_japanese_1("bulk_JapaneseUser001", "bulk_日本語_1", "bulk_名前_1", "bulk_password123",
                                         "bulk_日本語.名前1@tdk.com")
        self.userpage.add_bulk_user_japanese_2("bulk_JapaneseUser002", "bulk_日本語_2", "bulk_名前_2", "bulk_password123",
                                         "bulk_日本語.名前2@tdk.com")
        self.userpage.add_bulk_user_korean_1("bulk_KoreanUser011", "bulk_한국_1", "bulk_이름_1", "bulk_password123",
                                         "bulk_한국.이름1@tdk.com")
        self.userpage.add_bulk_user_korean_2("bulk_KoreanUser0112", "bulk_한국_2", "bulk_이름_2", "bulk_password123",
                                         "bulk_한국.이름2@tdk.com")
        self.userpage.add_bulk_user_chinese_1("bulk_ChineseUser001", "bulk_中文_1", "bulk_名_1", "bulk_password123",
                                         "bulk_中文.名1@tdk.com")
        self.userpage.add_bulk_user_chinese_2("bulk_ChineseUser0012", "bulk_中文_2", "bulk_名_2", "bulk_password123",
                                         "bulk_中文.名2@tdk.com")

    @pytest.mark.order(12)
    def test_3_2_5_bulk_user_csv_upload(self):
        # self.userpage.upload_csv(csv_file="./pages/user_management/users_template-1.csv")
        # self.userpage.sendcsv(csv_file="C:/Users/hjasani/PycharmProjects/work/Admin_Dashboard/pages/user_management/users_template-1.csv")
        # self.userpage.upload_csv()
        # self.userpage.sendcsv(os.getcwd()+"/users_template_final.csv")
        self.userpage.send_data()
        # self.userpage.over_py()

    # @pytest.mark.order(9)
    # def test_3_3_2_verifying_permissions_add_user(self):
    #     self.loginpage.sign_out()
    #     self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
    #     self.userpage.click_create_user_button()
    #     self.userpage.add_user_information("PermissionTestUser101", "first", "last", "PermissionTestUser101",
    #                                        "PermissionTestUser101@tdk.com")
    #     self.loginpage.sign_out()
    #     self.loginpage.login("PermissionTestUser101", "PermissionTestUser101")
    #     self.seleniumdriverpage.hold_wait()

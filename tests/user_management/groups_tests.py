import unittest

import pytest

from pages.user_management.groups_page import GroupsPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class GroupsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.grouppage = GroupsPage(self.driver)
        self.loginpage = LoginPage(self.driver)


    @pytest.mark.order(16)
    def test_3_3_4_delete_group_if_available(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.grouppage.delete_group("abc")

    @pytest.mark.order(17)
    def test_3_3_1_adding_groups(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.grouppage.all_grp("abc", "automation test group - this group will be deleted upon complete suite execution", "InvenSense-PowerUserGroup","Admin-InvenSense-PowerUserGroup")

    @pytest.mark.order(18)
    def test_3_3_3_edit_group(self):
        self.grouppage.edit_group("abc")

    @pytest.mark.order(19)
    def test_3_3_4_delete_group(self):
        self.grouppage.delete_group("abc")

    @pytest.mark.order(20)
    def test_3_3_5_download_all_groups_csv(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.grouppage.download_grp_csv()

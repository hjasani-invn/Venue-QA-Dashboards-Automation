import unittest

import pytest

from pages.user_management.user_home_page import UserHomePage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class UserHomeTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.userhomepage = UserHomePage(self.driver)
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.order(13)
    def test_3_2_4_bulk_user_csv_download(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.userhomepage.download_bulk_csv_btn()
        # self.userhomepage.verify_download()

    @pytest.mark.order(14)
    def test_3_2_6_edit_user(self):
        self.userhomepage.filter_grp("Automation_Test_Group")
        self.userhomepage.edit_user("Demo_1")

# this test case we are executing first of every iteration to make environment clean
    @pytest.mark.order(15)
    def test_3_2_7_delete_user(self):
        self.userhomepage.delete_user()

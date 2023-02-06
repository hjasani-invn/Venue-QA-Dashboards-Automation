import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
from tests import conftest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.loginpage = LoginPage(self.driver)
        self.teststatus = TestStatus(self.driver)

    # @pytest.mark.login
    # @pytest.mark.run(1)
    @pytest.mark.order(1)
    def test_3_1_1_login_nominal(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        # result_1 = self.loginpage.verifyTitle()
        # assert result_1 == True
        self.loginpage.sign_out()

    # @pytest.mark.order(order=2)
    # def test_3_1_1_1sign_out(self):
    #     self.loginpage.sign_out()

    # @pytest.mark.login
    # @pytest.mark.run(2)
    @pytest.mark.order(2)
    def test_3_1_2_login_bad_password(self):
        self.loginpage.login("AutomationTestUser001", "justWrongPassword")
        # result = self.loginpage.verifyTitle()
        # assert result == True

    # @pytest.mark.login
    # @pytest.mark.run(3)
    @pytest.mark.order(3)
    def test_3_1_3_login_bad_user(self):
        self.loginpage.login("BadUser", "BadPassword")
        # result = self.loginpage.verifyTitle()
        # assert result == True
        # result = self.loginpage.verifyLoginFailed()
        # assert result == True

# ff = LoginTests()
# ff.test_valid_login()

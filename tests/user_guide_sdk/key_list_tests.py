import unittest

import pytest

from pages.user_guide_sdk.key_list_page import KeyListPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class KeyListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.keylistpage = KeyListPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.order(22)
    def test_3_4_2_open_key_list(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.keylistpage.open_key_list()

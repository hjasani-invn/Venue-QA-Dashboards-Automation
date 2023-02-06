import unittest

import pytest

from pages.user_guide_sdk.guides_page import GuidesPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class GuideListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.guidepage = GuidesPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.order(23)
    def test_3_4_3_download_user_guides(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.guidepage.open_guide()

    @pytest.mark.order(24)
    def test_3_4_3_1_open_guides_in_toggle_view_mode(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.guidepage.double_click_pdf_file_thubmnail()
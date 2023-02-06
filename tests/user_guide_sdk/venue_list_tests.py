import unittest

import pytest

from pages.user_guide_sdk.venue_list_page import VenueListPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class VenueListTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.venuelistpage = VenueListPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.order(21)
    def test_3_4_1_open_venue_list(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.venuelistpage.open_venue_list()

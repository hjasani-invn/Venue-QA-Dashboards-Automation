import unittest

import pytest

from pages.contact_tracing.contact_analytics_page import ContactAnalyticsPage
from pages.home.login_page import LoginPage


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ContactAnalyticsTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.contactanalyticspage = ContactAnalyticsPage(self.driver)
        self.loginpage = LoginPage(self.driver)

    @pytest.mark.order(25)
    def test_3_5_1_1_contact_tracing_queries(self):
        self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        self.contactanalyticspage.enter_venue(v_n='ICA_2021')
        self.contactanalyticspage.chose_start_date(s_date="1/1/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/3/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="2")
        self.contactanalyticspage.click_search_btn()

    @pytest.mark.order(26)
    def test_3_5_1_2_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="3/3/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="1/1/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="2")
        self.contactanalyticspage.click_search_btn()

    @pytest.mark.order(27)
    def test_3_5_1_3_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="1/1/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/3/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="25")
        self.contactanalyticspage.click_search_btn()

    @pytest.mark.order(28)
    def test_3_5_1_4_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="1/1/2021")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="3/3/2021")
        self.contactanalyticspage.select_max_distance(enter_max_distance="twenty-five")
        self.contactanalyticspage.click_search_btn()

    @pytest.mark.order(29)
    def test_3_5_1_5_contact_tracing_queries(self):
        # self.loginpage.login("AutomationTestUser001", "TP1M4St3R_p4ssw0rd")
        self.contactanalyticspage.open_contact_analytics_tab()
        # self.contactanalyticspage.get_list_before_search()
        # self.contactanalyticspage.enter_venue(v_n='ICA Calgary')
        self.contactanalyticspage.chose_start_date(s_date="2/11/2022")  # DD/MM/YYYY, D/M/YYYY
        self.contactanalyticspage.choose_end_date(e_date="2/19/2022")
        self.contactanalyticspage.select_max_distance(enter_max_distance="2")
        self.contactanalyticspage.click_search_btn()
        # self.contactanalyticspage.get_list_after_search()
        # self.contactanalyticspage.print_list()
        # self.contactanalyticspage.is_popup()



    @pytest.mark.order(30) # if query created then only rename the latest query
    def test_3_5_2_contact_tracing_rename_queries(self):
        # self.loginpage.login("TestUser001", "TP1M4St3R_p4ssw0rd")
        # self.contactanalyticspage.update_query_name("renaming query")
        self.contactanalyticspage.is_popup(query_name="renamed")
import unittest
unittest.TestLoader.sortTestMethodsUsing = None
from tests.home.login_tests import LoginTests
from tests.user_management.user_tests import UserTests
from tests.user_management.user_home_tests import UserHomeTests
from tests.user_management.groups_tests import GroupsTests
from tests.user_guide_sdk.venue_list_tests import VenueListTests
from tests.user_guide_sdk.key_list_tests import KeyListTests
from tests.user_guide_sdk.guides_tests import GuideListTests
from tests.contact_tracing.contact_analytics_tests import ContactAnalyticsTests


tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)
tc2 = unittest.TestLoader().loadTestsFromTestCase(UserTests)
tc3 = unittest.TestLoader().loadTestsFromTestCase(UserHomeTests)
tc4 = unittest.TestLoader().loadTestsFromTestCase(GroupsTests)
tc5 = unittest.TestLoader().loadTestsFromTestCase(VenueListTests)
tc6 = unittest.TestLoader().loadTestsFromTestCase(KeyListTests)
tc7 = unittest.TestLoader().loadTestsFromTestCase(GuideListTests)
tc8 = unittest.TestLoader().loadTestsFromTestCase(ContactAnalyticsTests)

smoke_test = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5, tc6, tc7, tc8])

unittest.TextTestRunner(verbosity=2).run(smoke_test)

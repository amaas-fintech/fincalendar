import unittest
from datetime import date

from fincalendar.holidays import holidays_set


class HolidaysTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_Overrides(self):
        print(holidays_set(alpha_3_country_code='SGP', year=2015))

    def test_NoOverrides(self):
        holidays_set(alpha_3_country_code='MYS', year=2015)

    def test_MissingCountryCode(self):
        holidays_set(alpha_3_country_code='XXX', year=2015)

    def test_OverridesOnlyAdd(self):
        print(holidays_set(alpha_3_country_code='HKG', year=2015))

    def test_OverridesOnlySubtract(self):
        holidays_set(alpha_3_country_code='GBR', year=2015)

if __name__ == '__main__':
    unittest.main()

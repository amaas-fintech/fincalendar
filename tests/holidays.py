from datetime import date
from mock import patch
import unittest

import fincalendar.holidays
from fincalendar.holidays import holidays_set


DUMMY_OVERRIDES = {"SGP": {"add": {date(2015, 5, 27), date(2016, 5, 27)},
                           "subtract": {date(2015, 12, 25)}
                          },
                   "HKG": {"add": {date(2015, 5, 27), date(2016, 5, 27)}
                          },
                   "GBR": {"subtract": {date(2015, 12, 25)}
                          }
                  }

class HolidaysTest(unittest.TestCase):

    def setUp(self):
        pass

    @patch("fincalendar.holidays.OVERRIDES", DUMMY_OVERRIDES)
    def test_Overrides(self):
        holidays = holidays_set(alpha_3_country_code='SGP', year=2015)
        self.assertIn(date(2015, 5, 27), holidays)

    @patch("fincalendar.holidays.OVERRIDES", DUMMY_OVERRIDES)
    def test_NoOverrides(self):
        holidays = holidays_set(alpha_3_country_code='MYS', year=2015)
        self.assertIn(date(2015, 12, 25), holidays)

    @patch("fincalendar.holidays.OVERRIDES", DUMMY_OVERRIDES)
    def test_MissingCountryCode(self):
        # The default calendar in workalendar has the 1st Jan as a holiday
        holidays = holidays_set(alpha_3_country_code='XXX', year=2015)
        self.assertEqual(holidays, {date(2015, 1, 1)})

    @patch("fincalendar.holidays.OVERRIDES", DUMMY_OVERRIDES)
    def test_OverridesOnlyAdd(self):
        holidays = holidays_set(alpha_3_country_code='HKG', year=2015)
        self.assertIn(date(2015, 5, 27), holidays)

    @patch("fincalendar.holidays.OVERRIDES", DUMMY_OVERRIDES)
    def test_OverridesOnlySubtract(self):
        holidays = holidays_set(alpha_3_country_code='GBR', year=2015)
        self.assertNotIn(date(2015, 12, 25), holidays)

if __name__ == '__main__':
    unittest.main()

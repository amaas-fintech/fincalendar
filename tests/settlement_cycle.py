from __future__ import absolute_import, division, print_function, unicode_literals

from mock import patch
import random
import unittest

from fincalendar.settlement_cycle import get_settlement_cycles, get_country_settlement_cycle


class SettlementCycleTest(unittest.TestCase):

    def test_GetSettlementCycles(self):
        results = get_settlement_cycles('Equity')
        self.assertIsNotNone(results.get("settlement_cycle"))

    def test_GetMissingSettlementCycles(self):
         with self.assertRaisesRegexp(NotImplementedError, "This asset class is not yet configured"):
             get_settlement_cycles('XXX')

    def test_GetCountrySettlementCycle(self):
        cycle = get_country_settlement_cycle(asset_class='Equity', country_code='SGP')
        self.assertEqual(cycle, 3)

    def test_GetMissingCountrySettlementCycle(self):
        error = "This country/asset class combination is not yet configured"
        with self.assertRaisesRegexp(NotImplementedError, error):
            get_country_settlement_cycle(asset_class='Equity', country_code='XXX')

    def test_GetMissingAssetClassCountrySettlementCycle(self):
        error = "This asset class is not yet configured"
        with self.assertRaisesRegexp(NotImplementedError, error):
            get_country_settlement_cycle(asset_class='XXX', country_code='SGP')

if __name__ == '__main__':
    unittest.main()

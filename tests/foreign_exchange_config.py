import unittest
from datetime import date

from fincalendar.foreign_exchange_config import get_settlement_day_convention


class FxSettlementDateConvention(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_t_plus_2 (self):
        basecurrency = 'SGD'
        pricingcurrency = 'USD'
        self.assertEqual(get_settlement_day_convention(basecurrency,pricingcurrency),2)

    def test_t_plus_0 (self):
        basecurrency = 'KZT'
        pricingcurrency = 'USD'
        self.assertEqual(get_settlement_day_convention(basecurrency,pricingcurrency),0)

    def test_t_plus_1 (self):
        basecurrency = 'PHP'
        pricingcurrency = 'CAD'
        self.assertEqual(get_settlement_day_convention(basecurrency,pricingcurrency),1)

    def test_ruble_exception(self):
        basecurrency = 'GBP'
        pricingcurrency = 'RUB'
        self.assertEqual(get_settlement_day_convention(basecurrency,pricingcurrency),2)
        basecurrency = 'CNY'
        self.assertEqual(get_settlement_day_convention(basecurrency,pricingcurrency),1)
        
if __name__ == '__main__':
    unittest.main()

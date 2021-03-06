import unittest
from datetime import date

from fincalendar.fx_settlement_date import get_fxforward_valuedate, get_fxspot_valuedate, \
            calc_tenor_value_date, calc_fixing_date, get_date_info


class FxValueDateTest(unittest.TestCase):

    def setUp(self):
        pass
    
    def tearDown(self):
        pass

    def test_Spot0(self):
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'USA'
        pricing_date = date(2017,8,1)  #Ordinary within week test
        valuedate = date(2017,8,3)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_Spot1(self):
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'USA'
        pricing_date = date(2017,1,27)  #Friday, next working Monday Jan 30th is SG holiday. Value date should be Feb 1st
        valuedate = date(2017,2,1)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))
        
    def test_Spot2(self): 
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'USA'
        pricing_date = date(2017,6,30)  #Friday, next working Tuesday Jul 4th is US holiday, value date should be Jul 5th
        valuedate = date(2017,7,5)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_Spot3(self): 
        assetcurrencycountry = 'KOR'
        pricingcurrencycountry = 'USA'
        pricing_date = date(2017,6,22)  #Ordinary cross weekend test, this is Thursday, expect next Monday
        valuedate = date(2017,6,26)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_spot_t_plus_1(self):
        assetcurrencycountry = 'CAN'
        pricingcurrencycountry = "USA"
        pricing_date = date(2017,8,1)  #Ordinary within week test
        valuedate = date(2017,8,2)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_SpotCross1(self):        
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'KOR'
        pricing_date = date(2017,11,8)  #Wednesday, Nov 10th is  US thanksgiving holiday and it is Friday, has to roll to the next working Monday
        valuedate = date(2017,11,13)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))
    
    def test_SpotCross2(self):        
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'KOR'
        pricing_date = date(2017,6,30)  #Friday, next Tuesday Jul 4th is US holiday, Tuesday, should be rolled to Wednesday
        valuedate = date(2017,7,5)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_SpotCross3(self):        
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'KOR'
        pricing_date = date(2017,8,1)  #ordinary within week
        valuedate = date(2017,8,3)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_SpotCross4(self):        
        assetcurrencycountry = 'SGP'
        pricingcurrencycountry = 'KOR'
        pricing_date = date(2017,8,4)  #ordinary within week
        valuedate = date(2017,8,8)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))

    def test_EuroSpecialCase(self):
        assetcurrencycountry = 'EUR'
        pricingcurrencycountry = 'USA'
        pricing_date = date(2017,4,12)  #ordinary within week
        valuedate = date(2017,4,18)
        self.assertEqual(valuedate,get_fxspot_valuedate(pricing_date,assetcurrencycountry,pricingcurrencycountry))
        
    
    def test_InvalideCurrency(self):
        price_date = date(2017,8,4)
        currency = 'ABCDEF'
        tenor = '100M'        
        self.assertRaises(ValueError, calc_tenor_value_date, price_date, currency, tenor)
    
    def test_InvalidPriceDate(self):
        price_date = None
        currency = 'CNYEUR'
        tenor = '10M'
        self.assertRaises(ValueError, calc_tenor_value_date, price_date, currency, tenor)

    def test_InvalidTenor(self):
        price_date = date(2017,8,4)
        currency = 'SGDKRW'
        tenor = '100M'
        self.assertRaises(ValueError, calc_tenor_value_date, price_date, currency, tenor)

    def test_CalcFixingDate(self):
        currency = 'USDKRW'
        value_date = date(2017, 9, 7)
        self.assertEqual(date(2017, 9, 5) , calc_fixing_date(currency = currency, value_date = value_date)) 

    def test_CalcFixingDate(self):
        currency = 'USDKRW'
        value_date = date(2017, 8, 22)
        self.assertEqual(date(2017, 8, 18) , calc_fixing_date(currency = currency, value_date = value_date)) 

    def test_CalcFixingDate(self):
        currency = 'USDMYR'
        value_date = date(2017, 2, 10)
        self.assertEqual(date(2017, 2, 7) , calc_fixing_date(currency = currency, value_date = value_date)) 

    def test_CalcFixingDate(self):
        currency = 'USDMYR'
        value_date = date(2017, 1, 31)
        self.assertEqual(date(2017, 1, 26) , calc_fixing_date(currency = currency, value_date = value_date)) 

    def test_CalcFixingDate(self):
        currency = 'USDMYR'
        value_date = date(2017, 4, 17)
        self.assertEqual(date(2017, 4, 13) , calc_fixing_date(currency = currency, value_date = value_date)) 

    def test_CalcFixingDate(self):
        currency = 'USDMYR'
        value_date = date(2017, 9, 14)
        self.assertEqual(date(2017, 9, 12) , calc_fixing_date(currency = currency, value_date = value_date))

    def test_IslamicHolidayErrorSuppression(self):
        working_day = get_date_info(date(2020, 4, 28), ['SGP'])['SGP']['working_day']
        self.assertTrue(working_day in [True, False], True)

if __name__ == '__main__':
    unittest.main()

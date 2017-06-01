import unittest
from CurrencyRatesCatalog import CurrencyRatesCatalog

class CurrencyRatesTest(unittest.TestCase):

    def setUp(self):
        print ("Before the Test")

        self.testCurrency = CurrencyRatesCatalog("input files/currencyrates.csv")
        self.currency_code_for_Japanese_Yen = "JPY"
        self.currency_code_for_UK ="GBP"
        self.currency_code_for_Cameroon = "XOF"

        
    def test_get_currency_rates_details(self):
        code = self.currency_code_for_Japanese_Yen
          
        result = self.testCurrency.get_currency_rates_details(code).currency_to_euro
        self.assertEqual(0.007822, result)  ######exchange rate for Japanese Yen to euro = 0.007822


        code2 = self.currency_code_for_UK

        result = self.testCurrency.get_currency_rates_details(code2).currency_to_euro
        self.assertEqual(1.4029, result)  ######exchange rate for Japanese Yen to euro = 1.4029


        code3 = self.currency_code_for_Cameroon
        
        result = self.testCurrency.get_currency_rates_details(code3).currency_to_euro
        self.assertEqual(0.001524, result)  ######exchange rate for Japanese Yen to euro = 0.001524

    def tearDown(self):
        print ("After the Test")

if __name__ == '__main__':
    unittest.main()

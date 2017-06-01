#CurrencyRatesCatalog
import csv
from CurrencyRates import CurrencyRates

class CurrencyRatesCatalog:

    __currencyRatesDict = {}

    def __init__(self, currency_rate_file):
        self.loadData(currency_rate_file)

    def loadData(self, currency_rate_file):
        try:
            with open(currency_rate_file) as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        self.__currencyRatesDict[row['currencyCode']] = CurrencyRates(row['currencyName'], row['currencyCode'],
                                                                    row['euro_to_currency'], row['currency_to_euro'])
                except KeyError:
                    pass
        except FileNotFoundError:
                print("No csv file for currency rates found!")

    def get_currency_rates_details(self, currencyCode):
        return self.__currencyRatesDict[currencyCode]
               


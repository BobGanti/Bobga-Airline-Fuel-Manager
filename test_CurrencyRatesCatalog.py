#test CurrencyRatesCatalog
import csv

from CurrencyRatesCatalog import CurrencyRatesCatalog

def main():
    currencyRatesModel = CurrencyRatesCatalog('input files/currencyrates.csv')
    print()
    print(currencyRatesModel.get_currency_rates_details('EUR'))
    print(currencyRatesModel.get_currency_rates_details('CZK'))
    print('\n',currencyRatesModel.get_currency_rates_details('EUR').euro_to_currency)
    print('\n',currencyRatesModel.get_currency_rates_details('CZK').currency_to_euro)
    print('\n',currencyRatesModel.get_currency_rates_details('XAF').euro_to_currency)

main()
                                         

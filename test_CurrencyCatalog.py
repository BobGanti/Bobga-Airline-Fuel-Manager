#testCurrencyCatalog

from CurrencyCatalog import CurrencyCatalog

def main():
    currencyModel = CurrencyCatalog("input files/countrycurrency.csv")
    print()
    print(currencyModel.get_currency_details('Ireland'))
    print()
    print(currencyModel.get_currency_details('Japan'))
    print()
    print(currencyModel.get_currency_details('Botswana'))
    print()
    print("\nThe British currency name is ", currencyModel.get_currency_details('United Kingdom').currencyName)
    print("\nThe Cameroonian currency name is ", currencyModel.get_currency_details('Cameroon').currencyName)
    print("\nThe Chinese currency code is ", currencyModel.get_currency_details('China').currencyCode)

main()

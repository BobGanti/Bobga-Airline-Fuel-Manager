#CurrencyRates Class

class CurrencyRates:
    
    def __init__(self, currencyName, currencyCode, euro_to_currency, currency_to_euro):
        self.currencyName = currencyName
        self.currencyCode = currencyCode
        self.euro_to_currency = float(euro_to_currency)
        self.currency_to_euro = float(currency_to_euro)

    def __str__(self):
        return ("\n%s:%s \n%s:%s \n%s:%.3f \n%s:%.3f" % ('Currency Name',self.currencyName,
                    'Curency Code',self.currencyCode, 'ConvFrmEuro',self.euro_to_currency,
                        'ConvToEuro',self.currency_to_euro))
    

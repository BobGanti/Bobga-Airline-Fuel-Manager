#Currency Class

class Currency:
    
    def __init__(self, countryName, currencyName, currencyCode):
        self.countryName = countryName
        self.currencyName = currencyName
        self.currencyCode = currencyCode

    def __str__(self):
        currencystr=""
        return ("\n%s:%s \n%s:%s \n%s:%s" % ('Country',self.countryName, 'Currency',self.currencyName, 'Code',self.currencyCode))
    


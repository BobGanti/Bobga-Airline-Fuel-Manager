#IMPORT MODULES
import os,csv
from Currency import Currency

#Create CurrencyCatalog Class
class CurrencyCatalog:
    
    __currencyDict = {}

    def __init__(self, currencyFile):
        self.loadData(currencyFile)

    def  loadData(self, currencyFile):
        try:
            with open(currencyFile) as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                        self.__currencyDict[row['CountryName']] = Currency(row['CountryName'], row['currency_name'],
                                                                           row['currency_alphabetic_code'])
                except KeyError:
                    pass
        except FileNotFoundError:
            print("No csv file for Currency found!")
        
    def checkCode(self, CountryName):
            if CountryName in self.__currencyDict:
                return True
            else:
                print("Error! Check your code and enter again", CountryName, " not found")
                return False

    def get_currency_details(self, CountryName):
        return self.__currencyDict[CountryName]

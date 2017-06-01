# AirportAtlas

from tkinter.messagebox import *
import math
import csv
from Airport import Airport

class AirportAtlas: # class to generate dictionary of all Airports
    __airportDict = {}

    def __init__(self, csvFileName):
        self.loadData(csvFileName)
        
    def loadData(self, filename):
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)
                try:
                    for row in reader:
                                
                        self.__airportDict[row['Code']] = Airport(row['Code'], row['AirportID'], row['AirportName'], row['CityName'],
                                    row['Country'], row['Lat'], row['Long'])
                        
                except Exception:
                    pass
        except FileNotFoundError:
            showinfo('DIT-Error!',"No csv file found. Error code: D16126842")
            exit()
        
            
    def checkCode_airportDict(self, airportCode):
        if airportCode in self.__airportDict:
            return True
        else:
            if airportCode == "":
                message = "You must fill in all the boxes"
            else:
                message = airportCode, " is not found"
            showinfo('Error', message)
    
    def getAirport(self, Code):
        return self.__airportDict[Code]

    def getCountry(self, code):
        return self.__airportDict[code].getCountry()

    def distance_on_unit_sphere(self, lat1, long1, lat2, long2):
        # convert latitude and longitude to spherical coordinates in radians
        deg2Rad = math.pi/180.0
        radiusEarth = 6371

        #phi = 90 - latitude
        phi1 = (90 - lat1) * deg2Rad
        phi2 = (90 - lat2) * deg2Rad

        #theta = longitude
        theta1 = long1 * deg2Rad
        theta2 = long2 * deg2Rad

        # Compute spherical distance from sperical coodinates
        cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) +
                math.cos(phi1)*math.cos(phi2))
        arc = math.acos(cos)
        return arc*6371

    def get_dist_between_airports(self, code1,code2):
        airport1 = self.getAirport(code1)
        airport2 = self.getAirport(code2)
        return int (self.distance_on_unit_sphere(airport1.lat, airport1.long,
                airport2.lat, airport2.long))           
            









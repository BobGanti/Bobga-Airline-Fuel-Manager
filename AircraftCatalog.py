from Aircraft import Aircraft
import csv

class AircraftCatalog:
    """
    AircraftCatalog class: holds information about types of aircraft_code.
    The information is stored in a dictionary, the key to which is the aircraft code.
    Input: a csv file with five columns:
    Column 1: Airplane code.
    Column 2: Aircraft type.
    Column 3: Units (metric or imperial).
    Column 4: Manufacturer.
    Column 5: Range (in km or miles).
    """
    __aircraftDict = {}
    
    def __init__(self, csvFileName):
        self.loadData(csvFileName)
        
    def loadData(self, filename): # populating the aircraft dictionary
        try:
            with open(filename) as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    self.__aircraftDict[row['code']] = Aircraft(row['code'], row['type'],
                        row['units'], row['manufacturer'], row['range'])
                    
        except FileNotFoundError:
            print("No csv file found")
            
    """
    The checkCode_aircraftDict function ensures that any aircraft code entered
    is checked if it is in the aircraft csv file.
    If not found, an error message is dispayed
    """
    def checkCode_aircraftDict(self, aircraftCode):
        if aircraftCode in self.__aircraftDict:
            return True
        else:
             print("Error! Check your code and enter again", aircraftCode, " not found")
        return False
        
    def get_aircraft_details(self, planeCode):
        return self.__aircraftDict[planeCode]

    def get_aircraft_range(self, planeCode):
        aircraftRange ="%.2f" % (self.__aircraftDict[planeCode].range)
        return aircraftRange

    def get_aircraft_units(self, planeCode):
        return self.__aircraftDict[planeCode].units

    def get_aircraft_type(self, planeCode):
        return self.__aircraftDict[planeCode].planeType

    def get_fuel_capacity(self, planeCode):
        fuelCapacity = "%.2f" % (self.__aircraftDict[planeCode].range)
        return fuelCapacity

    def addFuel(self, volumeToAdd):
        unusedFuel = 0
        if volumeToAdd < 0:
            print("No syphoning fuel!")
        elif self.__currentFuel + volumeToAdd <= self.maxFuel:
            self.__currentFuel = self.__currentFuel + volumeToAdd
        elif self.__currentFuel + volumeToAdd > self.maxFuel:
            self.__currentFuel = self.maxFuel
            #unusedFuel = volume - self.__fuel
            unusedFuel = volumeToAdd - (self.maxFuel - self.__currentFuel)
        return unusedFuel


    def get_currentFuel(self):
        return self.__currentFuel
    
    def fuelCheck(self):
        if self.__currentFuel < self.MIN_FUEL:
            print("Fuel Check Failed: Current fuel below safe limit:", self.__currentFuel,
                  " less than ", self.MIN_FUEL)
            self.__fuelCheck = False
        else:
            print("Fuel Check Complete:", self.__currentFuel)
            self.__fuelCheck = True

    def takeOff(self):
        if self.__fuelCheck == True:
            print("Cleared for Takeoff! Fasten your seat-belt!")
        else:
            print("Take-off Failed: Please complte pre-flight check first")
            print(self.fuelCheck())

    def printStatus(self):
        print("Current fuel:", self.__currentFuel)

    def preFlightCheck(self):
        if self.__fuelCheck == True and self.__FlightClearance == True:
            print("PreFlightCheck Cleared for Takeoff! Fasten your seat-belt!")
        else:
            print("Take off Failed: Please complete pre-flight check first")

##    def __str__(self):
##        return ("%s:%s \n%s:%s \n%s:%s \n%s:%s \n%s:%.2f" %
##                ("Code",self.planeCode, "Type",self.planeType, "Units",self.units,
##                 "Manufacturer",self.manufacturer, "Range",self.range))
##
##

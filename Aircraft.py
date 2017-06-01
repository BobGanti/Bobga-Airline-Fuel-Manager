# Aircraft.py
nautical_miles_to_km = 1.852
import csv

class Aircraft:
    """
    Aircraft class holds information about an aircraft.  
    An Airplane has to be fuelled before it can take off
    """
    
    def __init__(self, planeCode, type, units, manufacturer, nonstandardised_range):
        self.planeCode = planeCode
        self.planeType = type
        self.manufacturer = manufacturer
        self.units = units.lower()
        self.nonstandardised_range = float(nonstandardised_range)
        self.range = self.get_aircraft_range()

    def calc_range_in_metric(self):
        if self.units == "imperial":
            return self.nonstandardised_range * nautical_miles_to_km
        else:                                                                       # assume metric if no units given
            return self.nonstandardised_range

    def get_aircraft_range(self):
        if self.units == "imperial":
            return self.nonstandardised_range * nautical_miles_to_km
        else:                                                                       # assume metric if no units given
            return self.nonstandardised_range

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

    def __str__(self):
        return ("%s:%s \n%s:%s \n%s:%s \n%s:%s \n%s:%.2f" %
                ("Code",self.planeCode, "Type",self.planeType, "Units",self.units,
                 "Manufacturer",self.manufacturer, "Range",self.range))

def main():
    aircraft1 = Aircraft('A319', 'Jet', 'metric', 'Airbus', 3750)
    aircraft2 = Aircraft('737', 'Jet', 'imperial', 'Huges', 5510)
    
    print("\nAircraft1 details: \n", aircraft1)
    print()
    print("Aircraft2 details: \n", aircraft2)
    print()
    print("Aircraft2 has range of: ", aircraft2.range, " km.")

if __name__ == '__main__':
    main()
    

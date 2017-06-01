## testCatalog

from AircraftCatalog import AircraftCatalog

def main():
    planeModel = AircraftCatalog("input files/aircraft.csv")
    print()
    print(planeModel.get_aircraft_details('767'))
    print()
    
    print(planeModel.get_aircraft_details('A319')) #retrieving aircraft details
    print()
    
    """Testing the checkCode function"""
    print("This Aircraft code is in the dict: ", planeModel.checkCode_aircraftDict('737'))

    print("\nAircraft Range: ", planeModel.get_aircraft_range('747'))
    print("\nFuel Capacity: ", planeModel.get_fuel_capacity('747'))
    print("\nUnit: ", planeModel.get_aircraft_units('747'))
    print("\nUnit: ", planeModel.get_aircraft_details('A319').units)

        
    def aircraft_from_user_aircraftCode():
        """ getting input from the user """
        while 1:
            planeCode = str(input("\nEnter the aircraft code: ")).upper()
            isValidCode = planeModel.checkCode_aircraftDict(planeCode)
            print("This Aircraft code is in the dict: ", isValidCode)
            if isValidCode == False:
                pass
            else:
                break

        if isValidCode:
            print(planeModel.get_aircraft_details(planeCode))
            print("\nThe", planeModel.get_aircraft_details(planeCode).manufacturer, planeCode,
                  planeModel.get_aircraft_type(planeCode), "has a fuel capacity of ",
                  planeModel.get_fuel_capacity(planeCode))
        
    aircraft_from_user_aircraftCode()
    
main()




#Test_drive_program(testAircraft.py)

from Aircraft import Aircraft
from Tower import Tower
from AircraftCatalog import AircraftCatalog 

# Create an Aircraft object
jumbo = AircraftCatalog("input files/aircraft.csv")
print(jumbo.get_aircraft_details('747'))
print()
print("About to start prparing a ", jumbo.get_aircraft_details('A320'), " for take-off")
jumbo = Aircraft('A319', 'Jet', 'metric', 'Airbus', 3750)
jumbo.addFuel(30)
jumbo.printStatus()
jumbo.fuelCheck()
jumbo.takeOff()
print()

# Create an Aircraft object
airbus = AircraftCatalog("input files/aircraft.csv")
print("About to start prparing a ", airbus.get_aircraft_details('A319'), " for take-off")
airbus = Aircraft("type", "manufacturer", "units", "range")
airbus.addFuel(2000)
airbus.printStatus()
airbus.fuelCheck()
airbus.takeOff()
print()

# Create an Aircraft object
boeing = AircraftCatalog("input files/aircraft.csv")
print("About to start prparing a ", boeing.get_aircraft_details('A321'), " for take-off")
boeing = Aircraft("type", "manufacturer", "units", "range")
fuelInTruck = 50000
fuelInTruck = boeing.addFuel(fuelInTruck)
boeing.printStatus()
boeing.fuelCheck()
boeing.takeOff()
print("Fuel Truck still has: ", fuelInTruck)

#create a tower object
tower = Tower()
aFlightList = ["FR901", "EI841", "KL3171", "EY7985", "UA7641"]
tower.updateFlightList(aFlightList)
tower.printFlightList()
print()

# Aircraft object
airbus2 = AircraftCatalog("input files/aircraft.csv")
print("Airbus to start prparing a ", airbus2.get_aircraft('A321'), " for take-off")
airbus2.flightNumber = "FR901"
tower.requestFlightClearance(airbus2)
airbus2 = Aircraft("type", "manufacturer", "units", "range")
airbus2.addFuel(2000)
airbus2.printStatus()
airbus2.fuelCheck()
airbus2.preFlightCheck()






























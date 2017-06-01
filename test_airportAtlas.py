## testAtlas

from AirportAtlas import AirportAtlas

def main():
    airportModel = AirportAtlas("input files/airport.csv")
    print()
    print(airportModel.getAirport('ORK'),"\n")
    print(airportModel.getAirport('DLA'),"\n")
    print(airportModel.get_dist_between_airports('DUB', 'SYD'),"\n") # Dublin to Australia
    print(airportModel.get_dist_between_airports('DUB', 'DUB')) # Dublin to Dublin. Result should be 0
    print("\nDouala airport Latitude: ", airportModel.getAirport('DLA').lat)
    print("\nDublin airport Longitude: ", airportModel.getAirport('DUB').long)
        
    def distance_from_user_airportCode():
        """airportCode1, airportCode2: departure and destination airport codes, respectively."""
        while 1:
            airportCode1 = input("\nEnter the Departure airport code: ").upper()
            isValidCode1 = airportModel.checkCode_airportDict(airportCode1)
            if isValidCode1 == False:
                pass
            else:
                break;
            
        while 1:
            airportCode2 = input("Enter the Destination airport code: ").upper()
            isValidCode2 = airportModel.checkCode_airportDict(airportCode2)
            if isValidCode2 == False:
                pass
            else:
                break;
            
        if isValidCode1 and isValidCode2:
            dist = (airportModel.get_dist_between_airports(airportCode1, airportCode2))
        
            print("\nThe distance between ",
                  airportModel.getAirport(airportCode1).name,"airport(",
                  airportModel.getAirport(airportCode1).country,") and ",
                  airportModel.getAirport(airportCode2).name,"airport(",
                  airportModel.getAirport(airportCode2).country,") is ",
                  airportModel.get_dist_between_airports(airportCode1, airportCode2), "km")

    distance_from_user_airportCode()
    
main()




## Airport Class
# class for airport objects

class Airport:

    def __init__(self, code, id, name, city, country, lat, long):
        self.code = code
        self.id = int (id)
        self.name = name
        self.city = city
        self.country = country
        self.lat = float(lat)
        self.long = float(long)

    def getCountry(self):
        return self.country
    
    def __str__(self):
        return ("\n%s:%s \n%s:%d \n%s:%s \n%s:%s \n%s:%s \n%s:%f \n%s:%f" %
                ("Airport Code",self.code, "Airport ID",self.id, "Airport Name",self.name, "Airport City",self.city,
                    "Airport Country",self.country, "Latitude",self.lat,
                        "Longitude",self.long))

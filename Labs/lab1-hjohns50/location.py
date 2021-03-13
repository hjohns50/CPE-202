# CPE 202 Lab 0
import math
# represents a location using name, latitude and longitude
# name is a str, lat is a float, lon is a float
class Location:
    def __init__(self, name, lat, lon):
        self.name = name    # string for name of location
        self.lat = lat      # latitude in degrees (-90 to 90)
        self.lon = lon      # longitude in degrees (-180 to 180)

# ADD BOILERPLATE HERE (__eq__ and __repr__ functions)
    #location object -> str
    #allow python to print an object
    def __repr__(self):  
        return "Location('%s', %s, %s)" % (self.name, self.lat, self.lon)

    #location object -> boolean
    #compares equality between location objects
    def __eq__(self, a):
        return math.isclose(self.lat, a.lat) and math.isclose(self.lon, a.lon)
    #main function given to all of us
def main():
    loc1 = Location("SLO", 35.3, -120.7)
    loc2 = Location("Paris", 48.9, 2.4)
    loc3 = Location("SLO", 35.3, -120.7)
    loc4 = loc1

    print("Location 1:",loc1)
    print("Location 2:",loc2)
    print("Location 3:",loc3)
    print("Location 4:",loc4)

    print("\nLocation 1 equals Location 2:",loc1==loc2)
    print("Location 1 equals Location 3:",loc1==loc3)
    print("Location 1 equals Location 4:",loc1==loc4)

    locations = [loc1, loc2]
    print(loc1 in locations)
    print(loc2 in locations)
    print(loc3 in locations)
    print(loc4 in locations)

if __name__ == "__main__":
    main()
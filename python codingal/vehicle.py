class bmw:
    def fueltype(self):
        print("BMW fuel type is premium unleaded gasoline with an octane rating of 91 or higher.")
    
    def maxspeed(self):
        print("BMW max speed is 250 kmph (155 mph).")

class ferrari:
    def fueltype(self):
        print("Ferrari fuel type is high-octane premium unleaded gasoline, commonly 91-94 A.K.I. (95-98 RON).")
    
    def maxspeed(self):
        print("Ferrari max speed is over 350 kmph (217+ mph).")

bmw1=bmw()
ferrari1=ferrari()

for vehicle in (bmw1,ferrari1):
    vehicle.fueltype
    vehicle.maxspeed
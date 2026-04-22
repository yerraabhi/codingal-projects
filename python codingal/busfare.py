class Vehicle:
    def __init__(self,seating):
        self.seating=seating


    def fare(self):
        return self.seating*110

class Bus(Vehicle):
    pass

bus1=Bus(50)

bus1.fare()
class planet:
    name="Platen"
    def __init__(self,size,moons,revolution):
        self.size=size
        self.moons=moons
        self.revolution=revolution

pt=planet("10239.76km",2,3)

print(pt.name,"is a planet with",pt.moons,"moons.","It is",pt.size+"in diameter","and takes",pt.revolution,"earth years to revolve.")
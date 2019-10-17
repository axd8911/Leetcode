
class ParkingLot:
    def __init__(self):
        self.spot = []

    def addSpot(self,newSpot):
        self.spot.append(newSpot)

class Vehicle:
    def __init__(self, license, size):
        self.license = license
        self.size = size
        self.spot = None

    def park(self,LotA):
        for item in LotA.spot:
            if not item.occupied:
                item.occupied = self.license
                self.spot = item
                break

    def leave(self,LotA):
        if self.spot:
            self.spot.occupied = ''
            self.spot = None


class ParkingSpots:
    def __init__(self,id):
        self.id = id
        self.occupied = ''

    def park(self,vehicle):
        self.occupied = vehicle.license

    def leave(self):
        self.occupied = ''

sa = ParkingSpots(1)
sb = ParkingSpots(2)
sc = ParkingSpots(3)
p = ParkingLot()
p.addSpot(sa)
p.addSpot(sb)
p.addSpot(sc)

va = Vehicle('TX0685',2)
vb = Vehicle('TX0709',1)
va.park(p)
print (va.spot,vb.spot)
print (sa.occupied,sb.occupied)
vb.park(p)
print (va.spot,vb.spot)
print (sa.occupied,sb.occupied)
va.leave(p)
print(va.spot,vb.spot)
print (sa.occupied,sb.occupied)


# class ParkingSpots:
#     def __init__(self,size):
#         self.size = size
#         self.vehicle = None
#     def isOccupied(self):
#         return self.vehicle != None

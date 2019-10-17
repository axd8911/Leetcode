- What types of vehicles it can support
- whether the parking lot has multiple levels, etc.

- Assumptions:
    - The parking lot has multiple levels
    - The parking lot can park motorcycles, cars and buses
    - The parking lot has motorcycle spots, compact spots and large spots
    - Motorcycle can park in any spot
    - A car can park in either a single compact spot or a single large spot
    - A bus can park in five large spots that are consecutive and within the same row

```python
class Vehicle:
    def __init__(self, license, size):
        self.license = license
        self.size = size

    def park(self,spot):
        parkingSpots.add(spot)


    def leave(self):


class ParkingSpot:
    def __init__(self,size):
        self.size = size
        self.vehicle
    def is






```

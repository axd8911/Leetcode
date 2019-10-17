class Restaurant:
    def __init__(self):
        self.tables = []
        self.reservations = {}

    def add(self,table):
        self.tables.append(table)
        print ('add ',table.id)

    def reserve(self,guest):
        for table in self.tables:
            if not table.occupied:
                table.reservation()
                self.reservations[guest.name] = table
                break

    def cancel(self,guest):
        self.reservations[guest.name].cancellation()
        del self.reservations[guest.name]

class Table:
    def __init__(self,id,size):
        self.id = id
        self.size = size
        self.occupied = False
        self.waitor = None

    def reservation(self):
        self.occupied = True
        print (self.id)
    def cancellation(self):
        self.occupied = False


class Guest:
    def __init__(self,name,phone,count):
        self.name = name
        self.phone = phone
        self.count = count

t1 = Table(1,1)
t2 = Table(2,1)
t3 = Table(3,1)
r = Restaurant()
r.add(t1)
r.add(t2)
r.add(t3)

g1 = Guest('Xudong','0689','5')
g2 = Guest('Qionglin','1492','5')
print (t1.occupied,t2.occupied)
r.reserve(g1)
print (t1.occupied,t2.occupied)
r.reserve(g2)
print (t1.occupied,t2.occupied)
r.cancel(g1)
print (t1.occupied,t2.occupied)

from math import acos,sin,cos,radians,floor
RADIUS_MILES = 3963

class DestinationCalculator:
    def __init__(self):
        self.dic = {}

    def process(self,line):
        a,b,c,d = line.split(':')
        if a == 'LOC':
            self.dic[b] = (float(c),float(d))
            return b

        else:
            a1,b1 = self.dic[c]
            a2,b2 = self.dic[d]
            diff = abs(b1-b2)
            print (diff)
            angle = acos(sin(a1*3.14159/180)*sin(a2*3.14159/180)+cos(a1*3.14159/180)*cos(a2*3.14159/180)*cos(diff*3.14159/180))
            print (angle)
            dist = int(angle * RADIUS_MILES)
            return b + ':' + c + ':' + d + ':' + str(dist)


if __name__ == "__main__":
    dest_calc = DestinationCalculator()
    lines = ['LOC:CHI:41.836944:-87.684722','LOC:NYC:40.7127:-74.0059','TRIP:C0FFEE1C:CHI:NYC']
    for line in lines:
        print(dest_calc.process(line))

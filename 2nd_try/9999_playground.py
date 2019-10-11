alldata = set()
for n in range(101):
    x = (195 + 2**n)%256
    alldata.add(x)

print (alldata)

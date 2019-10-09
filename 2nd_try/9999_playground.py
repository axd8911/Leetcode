# each number, print its 4 hash numbers

e = set()
for i in range(2016,3000):
    h1 = (i+i**1)%32
    h2 = (i+i**2)%32
    h3 = (i+i**3)%32
    h4 = (i+i**4)%32
    print (i, ' ',h1, ' ',h2,' ',h3,' ',h4)
    if {h1,h2,h3,h4}.issubset(e):
        break
    e.update([h1,h2,h3,h4])

my = [2010,2013,2007,2004,3200]
idx = [1,2,3]
res = []
for item1 in my:
    for item2 in idx:
        print (((item1**2+item1**3)*item2)%32)
    print (' ')
print (sorted(res))

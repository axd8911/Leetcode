my = [1975,1985,1995,2005,2015]
idx = [1,2]
res = []
for item1 in my:
    for item2 in idx:
        print ((item1*item2)%64)
    print (' ')
print (sorted(res))

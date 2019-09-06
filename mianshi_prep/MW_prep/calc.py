total = 0
for i in range(1000,10000):
    if i%11==0 and str(i) != str(i)[::-1]:
        total+=1
print (total)

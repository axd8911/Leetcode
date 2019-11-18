res1 = [[-1 for i in range(5)] for j in range(5)]

res2 = [[-1]*5][:] *5
res1[0][0] = 3
res2[0][0] = 3
print (res1)
print (res2)

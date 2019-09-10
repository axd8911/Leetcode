
val =  65536

print ((val or (val+1)) == val)
print ((val and (val+1)) == val)
print ((val and (val-1)) == 0)
print ((val or (val-1)) == 0)
print ((val >>1) == (val / 2))
print (((val>>1)<<1)==val)

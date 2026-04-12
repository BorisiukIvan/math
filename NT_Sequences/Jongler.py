import math

m = int(input("Enter an odd exponent m: "))
for i0 in range(1,10000,2):
    i = i0
    for j in range(100):
       if (i % 2):
           i = math.isqrt(int(i**m))
       else: i = math.isqrt(i)
       print(i,end=' ')
       if (i > 100**1000): break
       if (i == i0): print(i0, '!!')
    print()

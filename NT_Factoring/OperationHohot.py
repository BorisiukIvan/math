def digsum(x):
    c = 0
    for d in str(x): c += int(d)
    return c

x0 = 3*71456*803
for t in range(1,100000):
 a = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
 i = 1
 x = x0 * t
 if (x % 9 == 0): continue
 if (x % 5 == 0): continue
 while (i*i <= x):
     while ((x%i) and (i*i<x)): i += 1
     if (i*i > x): break
     n1 = digsum(i)
     n2 = digsum(x//i)
     if (n1 <= 6): a[n1] += 1
     if (n2 <= 6): a[n2] += 1
     i += 1
 if (a[2]==2) and (a[3]==3) and (a[4]==4) and (a[5]==5) and (a[6]<=6): print(x0,x,t,a)
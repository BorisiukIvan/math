def f(a, b):
    c = 0
    for el in a:
        if el in b: return 1
    return c

def DiofEq(x, T):
  a3 = [0,1]
  if (x % 2):
    a2 = []
    i = 2
    z = 1
    while (i % x != 1):
      if (z % 3) and (i%x not in a2): a2.append(i%x)
      i *= 2
      z += 1
  else: a2 = [0]
  a17 = [(17**T)%x]
  a = 2
  while (a < x):
      if ((a*a*a)%x not in a3): a3.append((a*a*a)%x)
      a += 1
  Atot = []
  for a in a2:
      for b in a17:
          if ((a+b)%x not in Atot): Atot.append((a+b)%x)
  r = f(Atot, a3)
#  if (r <= 3): print(a2, a17, Atot, a3)
  return r

x0 = 1
print("Let k E {0} U N. Then, we have")
while (x0 <= 1008):
 m = 0
 for x in [171, 5461, 6223, 16513, 18963]:
    d = DiofEq(x, x0)
    if (d==0):
       print("y = 1008k +",(x0%1008),"=> n =",x)
       m = 1
       break
 x0 += 1

def prostoe(x, cof):
    if (x == cof): return 1
    s = x - 1
    k = 1
    while s > 0:
        r = cof
        a = 1
        t = 0
        while a <= s:
              a = a * cof
              t = t + 1
        t = t - 1
        a = a // cof
        s = s - a
        for c in range(1, t+1): 
              r = r ** cof
              r = r%x
        k = (k * r) % x
    return k 

def getBestDivisor(x):
    global primes
    if (prostoe(x, 2) == 1) and (prostoe(x, 3) == 1) and (prostoe(x, 5)==1): return 1
    r = x**0.5
    for i in primes:
        if (x % i == 0): return x//i
        if (i > r): return 1
    return 0

def gDBB(x):
    for i in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]:
        if (x % i == 0) and (x != i): return x//i
        if (i*i > x): return 1
    return getBestDivisor(x)

print("Loading prime database..")
data = open("primes").read().split("\n")
primes = []
for prime in data: primes.append(int(prime))
print("Loaded! Starting the work.")

b = []
i0 = 2
while 1:
    i = i0
    a = []
    k = 0
    output = str(i) + ' : '
#    print(i, ':', end='')
    while 1:
        c = int(str(i)[0])+1
        if (c == 10): c = 1
        a.append(i)
        bestdiv = gDBB(i)
        if (not bestdiv):
          output += ("=> Terminating")
          break
        if (bestdiv == -1):
          output += ("=> Already considered")
          break
        i = int(str(c)+str(bestdiv))
#        i = bestdiv*10+c
        output += (str(i) + ' ')
#        print(i, end=' ')
        k += 1
        if (i < i0):
           output += ("=> Already considered")
           break
        if (i == i0): output += (" ! k ="+str(k)+" mina = "+str(min(a))+" maxa ="+str(max(a))+" lenmaxa = "+str(len(str(max(a)))))
        if (i in a):
           output += ("=> Cycle")
           break
    print(output)
    i0 += 1

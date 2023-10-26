
def stF(x, i):
    s = 0
    while (x % i == 0):
          s = s + 1
          x = x / i
    return (i**(s+1) - 1) / (i - 1)

def sigma(x):
   global prime
   if (x == 1): return 1
   s = 1
   y = int(x**0.5)
   for n in prime:
      if (n > y): return s*(x+1)
      if (x % n): continue
      s = s * stF(x, n)
      while (x % n == 0): x = x / n
      y = int(x**0.5)
      if (x == 1): return s
   raise Exception

def deliteli(x):
   global prime
   s = 1
   m = []
   y = int(x**0.5)
   for n in prime:
      if (n > y): return m+[[x, 1]]
      if (x % n): continue
      i = 0
      while (x % n == 0):
           i = i + 1
           x = x / n
      m.append([n, i])
      y = int(x**0.5)
      if (x == 1): return m
   return m+[[x, 1]]

def ncd(x, y):
    if (y > x):
        c = x
        x = y
        y = c
    n = y
    while (x%y):
        c = x
        x = y
        y = c % y
    return y

def pr(y):
    if (y == 1): return 0
    if (y < 4): return 1
    if (y % 2 == 0): return 0
    if (y % 3 == 0): return 0
    k = 1
    i = 5
    while y > 1:
         while (y % i):
             if (k):
                i = i + 2
             else: i = i + 4
             k = (k + 1) % 2
             if (i * i > y): return 1
         if (i == y): return 1
         return 0

def argD(x):
    global table
    if (pr(x-1)): return x-1
    s = int((4*x - 3)**0.5)
    if (s * s == 4*x-3) and (pr((s-1)/2)): return (s-1)*(s-1)/4
    if (x in table): return table[x]
    return 0

def check(x):
    res = 1
    for i in x:
        s = argD(i)
        if (not s): return
        if (ncd(res, s) != 1): return
        res = res * s
    return res

def d(x, path, l):
    global arr
    if (x == 1):
       i = check(path)
       if (i): arr.append(i)
       return
    if (x < l): return
    for i in range(l, int(x**0.5)+1):
        if (x % i): continue
        if (not argD(i)): continue
        path2 = path[:]
        path2.append(i)
        d(x/i, path2, i)
    if (argD(x)):
        path3 = path[:]
        path3.append(x)
        d(1, path3, x)

def mk_d(ch, z, arr2, s):
    global arr3
    arr = arr2[:]
    if (z == ch):
        arr3.append(s)
        return
    p = ncd(ch, z)
    if (s > 1):
       z = z / p
       ch = ch / p
    for i in arr:
        if (z % i == 0): return
    if (z > 10**8): return
    if (sigma(z) > ch): return
    t = deliteli(z)
    for i in t: arr.append(i[0])
    for i in t:
        k = i[1]
        sigma_tmp = sigma(z/i[0]**i[1])
        while (i[0]**k < 10**5) or (k == i[1]):
              x = i[0]**(k - i[1]) * z
              dr = (i[0]**(k+1)-1)/(i[0]-1) * sigma_tmp
              mk_d(ch*x, z*dr, arr, s*x)
              k = k + 1

def main():
  global arr, arr3
  i = 1
  while 1:
    i = i + 1
    arr = []
    d(i, [], 2)
    for j in range(len(arr)):
        for k in range(j+1, len(arr)):
            x = arr[j] + arr[k]
            if (2*i <= x): continue
            s = ncd(x, i)
            ch = x/s 
            z = i/s
            a = deliteli(arr[j]) + deliteli(arr[k])
            for l in range(len(a)): a[l] = a[l][0]
            arr3 = []
            try:
                mk_d(ch, z, a, 1)
                for l in arr3: print l, i, arr[j], arr[k], arr[j]*l, arr[k]*l
            except:
                print "Something went wrong!!!!"

prime = open("prime_nums").read().split("\n")
for i in range(len(prime)): prime[i] = int(prime[i])

arr = []
arr3 = []

table = {15:8, 31:16, 40:27, 63:32, 121:81, 127:64, 156:125, 255:128, 364:243, 400:343, 511:256, 781:625, 1093:729, 2047:1024, 1464:1331}
main()

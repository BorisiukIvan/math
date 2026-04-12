'''
    This program finds some x such that sum of proper divisors of x is equal to the given parameter a.
    Of course, the program doesn't find all such x, but it can find MOST of them.
    To use this program, you will have to install MSIEVE and get a base of small x and their sum of divisors.
'''

import os, random

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

def prostoe(x, i):
    if (x < 2): return 0
    s = x - 1
    k = 1
    while s > 0:
        r = i
        a = 1
        t = 0
        while a <= s:
              a = a * i
              t = t + 1
        t = t - 1
        a = a // i
        s = s - a
        for c in range(1, t+1): 
              r = r ** i
              r = r%x
        k = (k * r) % x
    return k 

def prostoe_gid(y):
    return (prostoe(y,2))

def finddivs(i, c=0):
 open("factors", "w").write("")
 os.system("./msieve "+str(i)+" -e -q > factors")

 f = open("factors").read().split("\n")
 n = ""
 if (len(f) > 1):
    arr = []
    for j in f:
        if (j.find(": ") > -1): arr.append(int(j.split(": ")[1]))

 if (c): print(arr)

 a = [1]
 for k in arr:
     b = a.copy()
     for t in a:
         if ((k*t not in b) and (k*t*k*t<i)): b.append(k*t)
     a = b.copy()

 return a

base = [0, 0]
#for i in open("/home/vanya/amicable/sociable/d_BIG"): base.append(int(i.split(" ")[0]))
for i in open("/home/vanya/amicable/sociable/base"): base.append(int(i.split(" ")[0]) + int(i.split(" ")[1]))

#x = 19298681539552699237261830834781317896242358534970233229446025747515796756692
x = random.randint(10**50, 10**51)*2
print(x)
finddivs(x, 1)

for i in range(2, len(base)):
    n = x - base[i]
    if (n < 1): continue
    if (n % (base[i]-i) == 0) and (i % (n//(base[i]-i))) and (prostoe_gid(n//(base[i]-i))):
       open("antiseq_data4", "a").write(str(i)+" "+str(n//(base[i]-i))+" "+str(i*(n//(base[i]-i)))+"\n")
       print(i, n//(base[i]-i), i*(n//(base[i]-i)))

for i in range(x%2+2, len(base), 2):
    n = x*(base[i]-i)+i*base[i]
    print('i =',i, '                         \r', end='')
    open("aliq", "w").write(str(i))
    if (n % ncd(base[i], base[i]-i)**2): continue
    d = finddivs(n)
    for k in d:
        if ((k-base[i])%(base[i]-i)==0):
           if (((n//k)-base[i])%(base[i]-i)==0):
              if (prostoe_gid((k-base[i])//(base[i]-i)) == 1):
                 if (prostoe_gid((n//k-base[i])//(base[i]-i)) == 1):
                    if (i%((k-base[i])//(base[i]-i))):
                        if (i%((n//k-base[i])//(base[i]-i))):
                            open("antiseq_data4", "a").write(str(i*(k-base[i])//(base[i]-i)*(n//k-base[i])//(base[i]-i))+"\n")
                            print(i, (k-base[i])//(base[i]-i), (n//k-base[i])//(base[i]-i), i*(k-base[i])//(base[i]-i)*(n//k-base[i])//(base[i]-i))

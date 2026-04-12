import math

# An algebra problem

# Let a E R and let f(x) be a function. Consider the sequence (b{n}) such that b{1} E D(f) and b{n} = f(b{n-1}). Determine all values of a such that there always exists, for any value of
# b{1} E D(f), a p E N such that the subsequence (c{n}) = b{p*n} converges.

# The program cosiders, for aE[1.3;4], the sequence (c{n}) given by b{1} = e and f(x)=x^a-loga(x). It outputs the cycle (b{pK},b{pK+1},..,b{pK+p-1}) and the period. If the period does not
# exist, then it outputs 0.

def f(x,a): return x**a-math.log(x,a)

def fp(x,a,p):
    for k in range(p): x = f(x,a)
    return x

def getPeriod(a,b):
# Stage 1: Search for an alleged cycle
    t = 0
    arr = []

    while (( (int(10**9*b)) not in arr) and (t < 10000)):
        t += 1
        arr.append(int(10**9*b))
        b = f(b,a)

    if (t == 10000): return 0

# Stage 2: Confirm that this cycle is real
    l = len(arr) - arr.index(int(10**9*b))
    print("[POSSIBLE P]",a, l, len(arr))
    c = 1/100

    while 2:
        b2 = fp(b,a,l)
        if (abs(b2-b) < 1/10**14):
           print("Period was confirmed.")
           break
        if (abs(b2-b) > c):
           print("Period wasn't confirmed.")
           return 0
        if (abs(b2-b) == c):
           print("Period was confirmed:",abs(b2-b),c," but the length was calculated incorrectly.")
           break
        c = abs(b2-b)
        b = b2

# Stage 3: Output the period and verify its length.
    b = b2
    i = 0
    print("Cycle:",end=" ")
    while (i <= 2*l):
        print(b,end=" ")
        b = f(b,a)
        i += 1
        print("(",abs(b2-b),")",end=" ")
        if (abs(b2-b) < 1/10**12):
           print()
           print("[PERIOD] a = ",a,"and p =",i)
           return i
    print()
    print("Unable to calculate the period length")
    return 0

def find_zeros(xmin, xmax, depth=2.):
    p1 = getPeriod(xmin,2.718281828)
    p2 = getPeriod(xmax,2.718281828)
#    print("[COMPARAISON]: xmin =",xmin,"xmax =",xmax,"p1 =",p1,"p2 =",p2)
    if (p1 == p2) or (abs(xmax - xmin) < 1/10**10):
       print("x E ["+str(xmin)+";"+str(xmax)+"] ===> PeriodE =",p1)
       return
    i = xmin
    interval = (xmax - xmin)/depth
    if (not interval):
        print(xmin, xmax, interval)
        return
    while (i < xmax):
        find_zeros(i, i+interval)
        i += interval
    return

lb = 1.33
ub = 4.00
while (lb < ub):
   try:
      find_zeros(lb, lb+0.00001)
   except: print("b is not in the bassin for lb E ["+str(int(10**8*lb)/10**8)+";"+str(int(10**3+10**8*lb)/10**8)+"]")
   lb = lb+0.00001
'''
Let's define Smrnd(n) by being then concatenation of all integers from 1 to n.
For example, Smrnd(5) = 12345 and Smrnd(11) = 1234567891011.
It is unknown if Smrnd(n) may be prime, but it is conjectured that there are
an infinity of such numbers.

This tool finds small prime factors of such numbers, even if n is very large.
I tried the programm for some n~10^17 and it found all prime factors of
Smrnd(n) below 3000 in just 10 seconds.

This programm cannot prove primality of a given Smrnd(n), but it cannot
prove that the given Smrnd(n) is composite.

Some interesting values for n are n = 211693703833318391 and
n = 831188155845269097.

You are welcome to report any bugs or suggestions by e-mail:
borisiuk.ivan.224@gmail.com.

This application is written by Borisyuk Ivan in January 2025.
'''

import random

def ncd(a,b):
    if (b > a): return ncd(b, a)
    if (b == 0): return a
    
    while (a%b):
        c = a
        a = b
        b = c % b

    return b

def nck(a,b): return a*b//ncd(a,b)

def oldmod(k, n):
    s = ''
    for i in range(k+1): s += str(i)
    return int(s)%n

def main(k, n0):
    if (k == 0): return 0
    digs = len(str(k))
    l = main(10**(digs-1) - 1, n0)
   
    n = nck(n0, digs)
    a1 = ''
    for i in range(10**(digs-1), 10**(digs-1) + n//digs): a1 += str(i)
    a1 = int(a1)
    d = (n//digs) * ((10**n - 1)//(10**digs - 1))
    cn = ( (k - 10**(digs-1) + 1)//(n//digs) )
    to = cn*(n//digs)-1+10**(digs-1)

    s = cn * a1 + d * (cn*(cn-1))//2
    t = ''
    for i in range(to+1, k+1): t += str(i)
    if (t == ''): t = 0
    
    if (t == 0): return (s+l)%(10**n0-1)
    return (int(t) + (s + l)*10**(len(str(t))%n0))%(10**n0-1)

def action(k, primes, UPPER_BOUND=2000):
    prod = 1
    s = []
    while (k % (prod*2) == 0):
           s.append("2")
           prod *= 2
    while (k % (prod*5) == 0):
           s.append("5")
           prod *= 5
    print("Working on Smrnd("+str(k)+")...")
    print("TF result: gcd(Smrnd(k), k) =", prod)
    for i in primes:
        i = int(i) - 1
        if (i > UPPER_BOUND): break
        t = ncd(10**i-1, main(k,i))
        print("Checking if the number has any common factors with 10^"+str(i)+"-1"+"                                         \r", end='')
        if (prod % t):
            prod2 = nck(prod, t)
            print("*** Found new factor",prod2//prod,"using N="+str(i))
            s.append(str(prod2//prod))
            prod = prod2 
    if (s):
        print("Conclusion: Smrnd("+str(k)+") is not a prime. It is divisible by", str(prod)+"="+"*".join(s)+".")
    else: print("Conclusion: Smrnd("+str(k)+") may be a prime.")
    return prod

def generate_primes(x=2000):
    res = []
    arr = [0, 0] + [1] * (x - 2)
    s = 1
    for i in range(x):
        if (not arr[i]): continue
        res.append(i)
        for j in range(i*i, x, i): arr[j] = 0
    return i


primes = generate_primes()
x = int(input("Please enter an integer.."))
action(x, primes)

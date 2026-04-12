'''
    This program, written on Aug 5 of 2025, proves that the equation y^17 + 1107 = 10^x does
    not have any solutions in positive integers, by analysing it modulo different numbers.

    In particular, y^17 + 1107 (mod 613) and 10^x (mod 613) don't intersect, thus proving the
    claim.
'''

def f(a, b):
    c = 0
    for el in a:
        if el in b: return 1
    return c

i = 3
while 1:
    if (i % 5 == 0): i += 2
    a = []
    for y in range(i):
        m = (y**17+1107) % i
        a.append(m)
    a = list(set(a))
    b = [1]
    x = 10
    while (x % i != 1):
        b.append(x % i)
        x *= 10
    s = f(a,b)
    if (s == 0): print(i, a, b)
    i += 2
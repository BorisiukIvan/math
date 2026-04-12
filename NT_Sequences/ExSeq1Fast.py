# A very useful program if someone wants to find all small cycles. This is partically useful at finding fixed points. For cycles with big length, you should use the other tool.

def general(x):
    if (x < 2): return x
    if (x < 3): return 2
    if (x < 5): return 3
    if (x < 7): return 5
    if (x < 11): return 7
    if (x < 13): return 11
    if (x < 17): return 13
    if (x < 19): return 17
    if (x < 23): return 19
    if (x < 29): return 23
    if (x < 31): return 29
    if (x < 37): return 31
    if (x < 41): return 37
    if (x < 43): return 41
    if (x < 47): return 43
    if (x < 53): return 47
    if (x < 59): return 53
    if (x == 59): return 59

def f(a):
    global t
    s=1
    a2=str(a)
    mod = 0
    r = 0
    for i in range(0, len(a2)):
        a1 = mod*10 + int(a2[i])
        if (a1 > 1):
           n = general(a1)
           s = s * n
           r = r + 1
           mod = a1 - n
        else: mod = a1
    if (r < t): return 0
    return s

def cep(x):
    a = []
    while (x not in a):
       a.append(x)
       x = f(x)
       if (not x): break
    return x

def multiply(x):
    arr = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59]
    res = 1
    while (x):
       res = res * arr[x % 18]
       x = x // 18
    return res

def add(x):
    x = x + 1
    if (x % 18): return x
    n = 1
    s = 18
    x2 = x
    while (x2 % (s*18) == 0):
       n = n + s
       s = s * 18
    n = n * ( (x2//s) % 18)
    return x + n

x = 2335928772806608153894
t = 0
while (18**t * 18 < x): t = t + 1
k = []
while 1:
    if (x % 10000 == 3894): open("raspamn-log", "w").write(str(x))
    x = add(x)
    if (x >= 18**t): t = t + 1
    y = cep(multiply(x))
    if (y not in k):
        k.append(y)
        print(y)
import math

def check(x):
    if (x < 3): return 0
    arr = [1, 1, 2, 6, 24, 12, 72, 504, 4032, 36288]
    y = 1
    for i in str(x):
        y *= arr[int(i)]
        if (not y): return 0
        if (y > x): return 0
    return (x == y)

def multiply(x):
    arr = [1, 2, 6, 504]
    res = 1
    while (x):
        res = res * arr[x % 4]
        x = x // 4
    return res

def add(x0):
    x = x0 + 1;
    if (x % 4): return x
    n = 1;
    s = 4;
    x2 = x;
    while (x2 % (s*4) == 0):
       n = n + s
       s = s * 4
    n = n * ( (x2//s) % 4)
    return x + n

# Here, x is the counter. If x > 4^y, then all integers having less than y/4 digits are considered.

x = int(open("FactorionCount.txt").read())
i = int(math.log(x,4))
c = 0;
while (not check(multiply(x))):
	x = add(x)
	c = c + 1
	if (c % 100000 == 0):
		print(c, x)
		open("FactorionCount.txt","w").write(str(x))
	if (x >= 4**i):
		i = i + 1
		print(i)

print(multiply(x), '!!')

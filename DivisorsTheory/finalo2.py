def aliquot(n, i, lim):
    print('aliquot:', n, i, lim, '\r', end='')
    for x in range(1, lim+1, 2):
        if (x % n == 0): continue
        x2 = x
        for j in range(i):
            x2 = x2*n+1
            while (x2%2 == 0): x2//=2
        if (x2 == x):
            print('x=', x, ',n=',n, ',length=', i, '!!')
            open("result", "a").write(str(x)+" "+str(n)+" "+str(i))

def main(c, i):
# множитель
    n = int(2**(c/(i+0.)))
    if (n % 2 == 0): return

# знаменатель
    z = 2**c - n**i
    if (z == 0): return
    lim = ((n+1)**i - n**i) // z

# перебираем числитель
    aliquot(n, i, lim)

c = 1
while 1:
    for i in range(2, c):
        if (5**i > 2**c): break
        main(c, i)
    c += 1
    print('c:', c)

# The function aliquot() takes three parameters (n,i,lim), where n - multiplier, i - length of the cycle, lim - the limit of the lowest member.
# This function outputs all found cycles.

def aliquot(n, i, lim):
#    print('aliquot:', n, i, lim, '\r', end='')
    for x in range(1, lim+1, 2):
        if (x % n == 0): continue
        x2 = x
        for j in range(i):
            x2 = x2*n+1
            while (x2%2 == 0): x2//=2
        if (x2 == x): print('x=', x, ',n=',n, ',length=', i, '!!')

# The function main() takes (c,i), calculates the only possible multiplier n, the limit of the cycle's lowest member and brute forces integers from 1 to that limit.

def main(c, i):
    n = int(2**(c/(i+0.)))
    if (n % 2 == 0): return

    z = 2**c - n**i
    if (z == 0): return
    lim = ((n+1)**i - n**i) // z

    aliquot(n, i, lim)

# We iterate through c and i, where c is the number of total operations (multiplications&divisions), and i is the number of multiplications in an Extended Collatz cycle.
# For each pair (c,i), there exist at most one multiplier x for which cycles with c divisions and i operations are possible.
# In order to save time, the multiplier 3 is not considered.

c = 1
while 1:
    for i in range(2, c):
        if (5**i > 2**c): break
        main(c, i)
    c += 1
    print('c:', c)

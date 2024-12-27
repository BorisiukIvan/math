#coding: utf-8
# This programm finds all primes up to x

x = 1000                            # setting x
arr = [0, 0] + [1] * (x - 2)
print('The array is set!')

s = 1
for i in range(x):
    if (not arr[i]): continue
    print(i)
    for j in range(i*i, x, i): arr[j] = 0


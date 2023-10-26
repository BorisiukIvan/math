#coding: utf-8

x = 1000
arr = [0, 0] + [1] * (x - 2)
#prime = []
print 'Массив готов!'

s = 1
for i in range(x):
    if (not arr[i]): continue
    print i
    for j in range(i*i, x, i): arr[j] = 0


'''
    This program finds solutions of the equation a^3+b^3+c^3=a^2+b^2+c^2+4 <==> (a^3-a^2)+(b^3-b^2)+(c^3-c^2)=4 in
    integers. The result file for the range 0<=|a|<=|b|<=|c|<=1000 is in the folder.
'''

arr = []
for i in range(1000): arr += [i**3-i**2, -i**3-i**2]

for i in range(2000):
    for j in range(i,2000):
        for l in range(j,2000):
            if (arr[i]+arr[j]+arr[l] == 4): print(arr[i],arr[j],arr[l], arr[i]+arr[j]+arr[l])
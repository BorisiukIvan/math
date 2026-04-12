'''
    This program proves that 2025^2025 cannot be represented as a sum of i-powers of some pairwise distinct Fibonnachi numbers.
    In particular, for all integer i>1, the sum of i-powers of all Fibonnachi numbers lower or equal to (2025^2025)^(1/i) is
    lower than 2025^2025. If this sum is greater than (2025^2025)/2, the program outputs i and the ratio of sum:(2025^2025).
'''

i = 2 
n = 2025**2025
while (2**i < n): 
      a1 = 1 
      a2 = 1 
      s = 1 
      while (a2**i < n): 
            a3 = a2 + a1 
            a1 = a2 
            a2 = a3 
            s += a1**i 
      f = 10**9 / (n*10**9 // s) 
      if (f > 0.5): print(i, f) 
      i += 1

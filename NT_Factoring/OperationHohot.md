*Problem*. We call a number $x\in\mathbb{N}$ **laughable** if $\forall n\in\mathbb{N}$ such that $1\le n\le 6$, $x$ has exactly $n$ positive integer divisors such that their sum of digits of $n$.
The task is to find the smallest **laughable** number.

*Solution*. The smallest laughable number is $19451537952$. It is easy to prove that the smallest laughable number is divisible by 3, but isn't divisible by 9 and isn't divisible by 10. There could
be other big optimisations, but since this problem isn't that important, I didn't apply them and the program is quite slow. In the file 'OperationHohot.py' you can find its code that finds all
**laughable** numbers that are multiples of a given number $x_0$.
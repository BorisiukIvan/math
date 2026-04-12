*Problem*. Let $x_0>1$ be a positive integer. Define $(a_i)_{i\in\mathbb{N}$ as $a_0=x$ and $a_{i+1}=f(a_i)$, where $f(a_i)$ is the concatenation of $g(a_i)$ and $h(a_i)$, where $g(a_i)$ is the
digital root (of first digit of $a_i$ plus 1) and $h(a_i)$ is the second largest integer divisor of $a_i$. Is this true, that in any such sequence $a$, there is always a prime number?

(Examples: we have $f(37) = 41$, because the second largest integer divisor of 37 is 1 and the digital root of 3+1 is 4. We also have $f(94) = 147$, since the 2nd largest divisor of 94 is 47 and
the digital root of 9+1=10 is 1.)

*Solution*. This is false and the smallest counter-example to this problem is the cycle $\{3545297, 4506471, 51502157, 67357451, 79622493, 826540831, 943502149, 16886877, 25628959\}$, which
does not contain any prime numbers. The program **HighDiv.py** outputs sequences created by this function $f$.

*2nd Problem*. We change the definition of $h(a_i)$, and, when $a_i$ is prime, it is now equal to $a_i$. Now, our sequences are longer and there are way more cycles. The program **HighDiv2.py**
outputs sequences formed by this new rule. As always, the task is to analyse the new function $f$ and determine all cycles and the behaviour of sequences.
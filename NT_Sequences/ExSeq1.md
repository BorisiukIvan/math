If you are not familiar with working with integer sequences, but you are interested in the topic, you should work with some less important but easier integer sequences and
study their properties. In this directory, I am going to show you some example sequences, which I invented myself in order to study them and unterstand how they work.

In particular, in this file I will describe the 1st example of integer sequences. It is hard to understand the rule, but it is easy to calculate the next term, so that's why
I studied it.

Let's define S = {integers greater than 1} and f:S->S as a product of primes chosen depending on the argument. The definition of that function is very, very hard to formulate in a
understandable way, therefore I'll show you some examples. Some values of f are f(91) = 7x19 = 133, f(153) = 13x23 = 299 and f(173) = 17x3 = 51. Then, there are calculations:

- f(91): 1st digit of 91 is 9, the closest prime to 9 is 7, therefore 7 is in prime factorization of f(91). The reminder 9-7=2 and the next digit of 91 is 1, so we concat 2 and 1
to obtain 21. The closest prime to 21 is 19, therefore 19 is in prime factorization of f(91) too. Since we reached the end of 91, we conclude that f(91) = 7x19 = 133.

- f(153): 1st digit of 153 is 1, there are no primes <= 1, therefore we add simply concat the next digit (5) to 1 and obtain 15. The closest prime to 15 is 13, 15-13=2, so we concat
the next digit (3) to 2 and obtain 23. The closest prime to 23 is 23 and we reached the end of 153, so we have f(153) = 13x23 = 299.

- f(173): Similarly, there are no primes <= 1, so we look for the closest prime to 17. It is 17, 17-17=0, so we concat the last digit of 173 (3) to 0, obtain 03 (or 3), look for
the closest prime to 3, oh, it's 3, we reached the end so f(173) = 17x3 = 51.

Finally, we define the sequence $(a_i)_{i\in\mathbb{N}}(x)$ as $a_{i+1}=f(a_i)$ for all $i>1$, where $a_1=x$ is an arbitrary integer strictly greater than 1. As usual, our goal is to
study the behaviour of $a$ and to find the most cycles as we can.

Now, in the case you are really interested by this topic and/or by this particular function, I've made some exercices based on this sequence that you should do if you are a beginner
and if you want to improve.

1) Evaluate f(133), f(28), f(7007) and f(266) to make sure you understood the definition correctly (you should get respectfully 39, 14, 49 and 130).

2) Every positive integer $\ne$1 is a product of some primes. Question: does the equation $f(x)=n$, where $n\inS$ and $f$ is our function, always have a solution or not? (Answer: if $n$
contains prime factors $\ge 61$, then $f(x)$ can never equal $n$.)

3) Based on the answer of the 2nd question, suggest a relatively fast approach to find cycles and fixed points ($n$ is a fixed point if $f(n)=n$). (Answer: look at **ExSeq1Fast.py* in
this folder.)

An important observation is that no matter how big is $x$, our sequence $a(x)$ will always (or almost always) be beached to one of already known cycles. However, I have no idea if the
number of total cycles is finite or infinite. Maybe you can solve this question?
Let $f(x,a)$ be a function on real numbers. Then, let $s(f,a,n)$ be a sequence of real numbers, defined by the following two rules:
1. $s_1 = n$ and
2. for each $k>1$, we have $s_{k} = f(s_{k-1})$.

The program analysis the behaviour of the sequence when $k\rightarrow\infty$. Most of time, the sequence is eventually decreasing or increasing, but we are interested in the situation when infinitely many elements of $s$ approach some constant $X$. We say that $s(f,a,n)$ eventually becomes $s(f,a,X)$.

Example: if $f(x,a) := 

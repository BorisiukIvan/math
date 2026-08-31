Let $f(x,a)$ be a function on real numbers. Then, let $s(f,a,n)$ be a sequence of real numbers, defined by the following two rules:
1. $s_1 = n$ and
2. for each $k>1$, we have $s_{k} = f(s_{k-1})$.

The program analyses the behaviour of the sequence when $k\rightarrow\infty$. Most of time, the sequence is eventually decreasing or increasing, but we are interested in the situation when infinitely many elements of $s$ approach some constant $X$. We say that $s(f,a,n)$ eventually becomes $s(f,a,X)$ and $s(f,a,X)$ is called the <i>attractive cycle</i> of $f$ on $a$.

Example: if $f(x,a) := x^2-a $, then for $a = 1$ the attractive cycle is $\{0,1\}$ because no matter what $n\in[0; 1]$ we take, the sequence $s$ eventually will approach infinitely closely to $(0, 1, 0, 1, ...)$.

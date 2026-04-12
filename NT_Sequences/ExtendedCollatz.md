Collatz conjecture: Pick any $x\in \mathbb{N}$. Define the sequence $(n_i)_{i\in\mathbb{N}}$ recursively: let $n_1 = x$ and $n_{i+1} = \frac{3n_i+1}{2^{v_2(3n_i+1)}} \quad \forall i\mathbb{N}$.
Basically, we multiply $n_i$ by 3, add 1, divide by 2 until the result becomes odd, and then we have next number $n_{i+1}$. The conjecture states that we will eventually arrive at 1, no matter
what $x$ we pick. In math terms, we have $lim_{i\rightarrow\infty} n_i = 1 \quad \forall x\in\mathbb{N}$ (It's also notable that the conjecture fails for some $x\in\mathbb{Z}$, for example
if $x=-5$, then $n=\{-5; -7; -5; -7; ...\}$ is periodic and doesn't converge.)

However, if we change the definition of $n$ by choosing a multiplier bigger than 3 - for example, if we let $n_{i+1} = \frac{5n_i+1}{2^{v_2(5n_i+1)}}$, the behaviour of $n$ is completely different.
Not only $n$ diverges (tends to $+\infty$), but there may exist positive cycles (I mean sequences $n$ that are periodic or eventually periodic; for $x=3$, only negative cycles exist).

Therefore, I wrote this program, that finds all cycles for every $x$.

**EXAMPLE**: {17, 43, 27} is a _cycle_ for $x = 5$, because
- **17***5 + 1 = 86
- 86/2 = 43
- 43*5 + 1 = 216
- 216/2/2/2 = 27
- 27*5 + 1 = 136
- 136/2/2/2 = **17**

We reached the first number of the sequence. The sequence will repeat itself forever, so it fits our definition of a _cycle_.

My program found every possible solution when $(x+1)^i < 2^{220}$, where $i$ is length of the cycle.
These solutions are _{1, 3}_, _{13, 33, 83}_, _{17, 43, 27}_ for $x = 5$ and _{27, 611}_, _{35, 99}_ for $x = 181$.

You can easily check this by yourself. No additional modules are needed and I tried to make the code the most compehensible possible.
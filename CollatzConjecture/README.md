# Extended Collatz conjecture
As you all know, the Collatz conjecture claims that any positive integer will eventrually be reduced to 1 by appllying the sequence $n_i+1=x∗n_i+1$, when $n_i$ is odd, and $n_i+1=n_i/2$, when $n_i$ is even, where $x=3$.

But let's consider this conjecture for any possible $x$!

So, this program finds all _cycles_ for every $x$.

For example, {17, 43, 27} is a _cycle_ for $x = 5$, because
- **17***5 + 1 = 86
- 86/2 = 43
- 43*5 + 1 = 216
- 216/2/2/2 = 27
- 27*5 + 1 = 136
- 136/2/2/2 = **17**

We reached first number of the sequence, so the process will repeat again and again, so it's a _cycle_.

The program found every possible solution when $(x+1)^i < 2^220$, where $i$ is length of the cycle.
These solutions are _{1, 3}_, _{13, 33, 83}_, _{17, 43, 27}_ for $x = 5$ and _{27, 611}_, _{35, 99}_ for $x = 181$.

Check it by yourself!

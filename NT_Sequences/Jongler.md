Jongler conjecture: Choose a $x\in\mathbb{N}$. Define $(j_i)_{i\in\mathbb{N}}$ recursively as $j_1=x$ and $j_{i+1} = [\sqrt{j_i^3}]$ (if $j_i$ is odd) or $j_{i+1}=[\sqrt{j_i}]$ (if $j_i$ is even), where $[x]$ is the greatest integer lower than $x$. The
conjecture states that $lim_{i\rightarrow\infty} j_i = 1$ no matter what $x$ we chose.

My thoughts on it (if you're interested): I think the conjecture is true as Collatz conjecture probably is, because, for large $x$, we can neglige the floor function and claim that $j_{i+1}\approx \sqrt{j_i^3}$ or $j_{i+1}\approx \sqrt{j_i}$.
Then, it is evident that in this case the only cycle is $j={1;1;1;...}$ (expect by some miracle there exist very close powers of 2 and 3 giving us a possible solution). Nevertheless, the conjecture is almost certainly true.

Just like Collatz sequences, if we increase the exponent (in basic case it is equal to 3), the Jongler sequence will, for most $x$, tend to infinity. However, $j={1;1;...}$ always remains a cycle, and
other cycles are found with 5, 9 and 17 as the exponent.

The program takes an exponent m and outputs beginnings of Jongler sequences whose starting number $x \in [1; 10000]$ and is odd.
*Problem*. Find all positive integers $x$, such that $x$ times product of its digits is non-zero and contains only 0 and 1 in its decimal representation.

*Reasoning*. Obviously all $x$ of the form $\frac{10^n-1}{9}, n\ge 1$ are trivial solutions. I found only 2 non-trivial solutions - these are $x=4625$ and $x=72215$.
It is unknown if other solutions exist. In the file "ProdDig.cpp" you can find a program that eventually will find every solution to that problem.
When I run this program on my PC, it found every solution $\le \frac{10^{11}-1}{9}$ in less than $2$ seconds, which is quite fast. As usual, if you have any suggestions,
feel free to communicate with me here on GitHub or write an e-mail!
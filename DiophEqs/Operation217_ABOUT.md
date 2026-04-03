[Exercice](https://www.quora.com/How-do-I-find-all-positive-integer-x-y-such-that-2-x-17-y-is-a-perfect-cube). Find all positive integers x, y, such that $2^x+17^y$ is a perfect cube. 

[Solution](https://www.quora.com/How-do-I-find-all-positive-integer-x-y-such-that-2-x-17-y-is-a-perfect-cube/answer/Ivan-Borisyuk). Firstly, I proved that $3\not\mid x$. Then, I wrote the program *Operation217.py* and found that $\forall y\in\mathbb{N}, \exists n\in\mathbb{N}$ such that $2^x+17^y=z^3 \pmod{n}$ does not have any solution. Therefore, the answer is $\not\exists$ such $x,y$.

The proof file is named *Operation217_FINAL.txt*.

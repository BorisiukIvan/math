*Problem*: Does there exist a $x\in\mathbb{N}$ such that $x>2$ and such that the product of factorials of digits of $x$ is equal to $x$?
*Program implementation*: Since $x$ is product of (many) factorials, it certainly has many 0s at the end. The fact that $0!=1$ implies that we can remove these 0s and the product of
factorials of digits won't change, but the remaining number will be lower and easier to find. So, we can define a new operation $x?$ by removing all the 0s from the end of $x!$ and
search a number $y$ such that the product of ? of its digits is equal to $y$. By above, to obtain $x$ from $y$, we just append to $y$ as many 0s as needed. So, our program searches
$y$, and not $x$. Note that every of $(1?,2?,...,9?)$ is a product of some elements of the set $\{6=3?,2=2?,504=7?\}$. Therefore, I wrote a program that simply bruteforces integers
of the form $2^{a_1}\cdot 6^{a_2}\cdot 504^{a_3}$. But, it is highly unlikely that the program will find something.
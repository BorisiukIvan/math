# Programs that involve aliquot sequences

Hi! In this folder, you can find various programs that are connected to **aliquot sequences**. 

*Definition*: Aliquot sequence is a sequence $(a_i)_{i\in\mathbb{N}}$ defined recursively as $(a_{i+1})=\sigma(a_i)-a_i$, where $\sigma(a_i)$ denotes the sum of all posivite integer divisors of $a_i$.

In 2023, I was working on aliquot sequences and I invented a method to find some amicable pairs [a pair $(a,b)\in\mathbb{N}^2$ is called *amicable* iff $\sigma(a)=\sigma(b)=a+b$] and discovered nearly 300
amicable pairs that were unknown before. You can find the code here, in this folder.

Also, I discovered that some sociable 4-tuples [a 4-tuple $(a,b,c,d)\in\mathbb{N}^4$ is called *sociable* iff $\sigma(a)-a=b,\sigma(b)-b=c,\sigma(c)-c=d$ and $\sigma(d)-d=a$] bear a special form and I
developped a program that searched for them, but unfortunately the program didn't find any new sociable 4-tuple. The code is also in the folder.

And finally, I delevopped a method of solving the equation $\sigma(x) - x = a$, where $a$ is a given parameter. The code of it is also in the folder.
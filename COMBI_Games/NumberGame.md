*Problem*. Two players A and B are playing the following game. Firstly, a number X is chosen. Then, we make a board with "1" written on it. On each turn, a player must erase the number on the board and write another number instead. The newly written number must satisfy some conditions:
1. It must be a positive integer between 2 and $X^2$ never written on the board before.
2. It must be either divisible, either divide the previous number such that their ratio is $\in[\frac{1}{X}; X]$.

The game ends when a player cannot make a turn. Then, the player who cannot make a turn loses the game. The question is, what player has a winning strategy depending on what $X$ is chosen?

*Note*. For $X=10$, the game is available online (though already fully solved) at [https://antihackers.ezyro.com/playing/](antihackers.ezyro.com). 

*Solution*. I wrote a program that solves the game for given $X$. It found that for $X\in\{5,6,8,10\}$ the 1st player wins, while for $X\in\{1,2,3,4,7,9\}$ the second player wins. The program
is available at **NumberGame.cpp** in this folder.

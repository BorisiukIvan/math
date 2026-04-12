*Problem*. Two players A and B are playing the following game. There is a board with the number 1 written on it. In a turn, a player can erase the number on the board and write another number
instead. However, this another number must remain a positive integer never written on the board before such that its ratio with the erased number is a positive integer $\le X$ and such that
the new number is $\le X^2$, where $X\in\mathbb{N}$ is chosen before the game starts. The game ends when a player cannot make a turn and the player who cannot make a turn loses the game. The
question is, what player has a winning strategy depending on what $X$ is chosen.

*Note*. For $X=10$, the game is available online (though already fully solved) at [https://antihackers.ezyro.com/playing/](antihackers.ezyro.com). 

*Solution*. I wrote a program that solves the game for given $X$. It found that for $X\in\{5,6,8,10\}$ the 1st player wins, while for $X\in\{1,2,3,4,7,9\}$ the second player wins. The program
is available at **NumberGame.cpp** in this folder.
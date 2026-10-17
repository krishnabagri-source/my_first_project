My first Python project: a simple command-line Rock, Paper, Scissors game played against the computer.

How it works
The computer randomly picks Rock, Paper or Scissors using Python's random module.
You type r, p or s (upper or lower case both work).
The game prints both choices and tells you whether you win, lose, or it's a draw.
The game runs for 7 rounds by default.

Internally, each move is stored as a number:

Move	Value
Rock	1
Scissors	0
Paper	-1
Run it

Requires Python 3.6+ (no extra libraries needed).

bash
git clone https://github.com/krishnabagri-source/my_first_project.git
cd my_first_project
python "project 1.py"
Example
Enter your choice (r for Rock, p for Paper, s for Scissors): r
you choose rock
computer choose scissor
you win
What I practiced
Functions
Dictionaries (mapping input to values and back)
if / elif / else logic
User input with input() and .strip().upper()
The random module
f-strings and loops
Ideas for improvement
 Keep a running score and show the winner after 7 rounds
 Let the player choose how many rounds to play
 Re-ask on invalid input instead of skipping the round
 Simplify the win/lose logic with a (my_move - computer) % 3 trick
Author

Krishna Bagri – B.Tech CSE (AI & ML), Maharaja Agrasen Institute of Technology, Delhi GitHub

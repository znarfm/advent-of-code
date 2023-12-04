# Day 4: Scratchcards

[Problem Set](https://adventofcode.com/2023/day/4)

## Process

### Part 1

1. Parse input.
2. Iterate over each game
3. Check each number from user if its in winning list. If yes, +1 to win count.
4. First match is as is (1 point). But next points doubles.

### Part 2

Same as Part 1, with slight modifications. 
Used a dictionary to track the number of instances for each game.

1. Parse input
2. Iterate each game
3. Check how many matches
4. Iterate from current game number to (current game + matches)
5. Add each match to the corresponding key in dict.
6. Print the sum of the values of the dict to get the number of instances.

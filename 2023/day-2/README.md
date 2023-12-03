# Day 2: Cube Conundrum

[Problem Set](https://adventofcode.com/2023/day/2)

## Process

### Part 1

1. Read each line of the input.
2. Get the string after `:`, it is the sets for each game
3. Separate sets with `;` as the delimiter.
4. Separate each cube using `, `.
5. Separate quantity and color of the cube using whitespace ` ` as the delimiter.
6. Now, check if quantity exceeds cube color quantity limit.
7. If one of the cubes exceeds the limit, break from the loops so that we can iterate to another game number. Otherwise, record the game number.

### Part 2

Kind of the same as Part 1, but this doesn't have color limits. But we still used a dict to record the max quantity for each color for each game.

We just have to iterate over all the cubes in every set, then add the max quantity to the corresponding color in the dict.

Compute the product of the three values for each then get the sum.

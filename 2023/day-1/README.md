# Day 1: Trebuchet?!

[Problem Set](https://adventofcode.com/2023/day/1)

## Process

### Part 1

1. Iterate each char in every line.
2. Check if the char is a digit, append it to a temp list.
3. Get the first and last element of that list, convert it to int then add to `sum` variable.

### Part 2

Essentially the same as **Part 1**.
Just added a `line2num()` function.
**Purpose:** Loops over the digit_names list, to replace each word to its corresponding int value. but it also puts the original string to the left and the right of the int value (`{name}{num}{name}`). This is done to also catch words that share the same letter.
For example:

- eigh**t**wo: eight8eighttwo2two
- zer**o**ne: zero0zeroone1one
- etc.
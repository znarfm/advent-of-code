# Day 3: Gear Ratios

[Problem Set](https://adventofcode.com/2023/day/3)

## Process

### Part 1

1. Convert the input values into a 2D array, for easier traversal.
2. Ignore all numbers and dots/periods. 
3. When we see a symbol, check the 3x3 area around it; we want to look for digits.
4. If a digit is found, get the coords of its leftmost digit. **Save it to a set to avoid duplcation.**
5. After getting all the coordinates, go to each coordinates, traverse to the right until next char is not a digit (to get the number itself).
6. Add values

#### tldr

- Look for symbols
- Get digits around it
- Get leftmost digit of the found digit
- Get numbers from those coordinates
- Add them all

### Part 2

Pretty much the same as *Part 1*, but the set that collects the leftmost digit's coordinates is moved inside the conditional that checks if we found an asterisk.

This is to help find exactly two part numbers that fit the criteria only, and not having just one part number adjacent to an asterisk.

Then, multiply two part number values, and add to ratios total.

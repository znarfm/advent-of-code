# Day 3: Gear Ratios (part 1)

def main():
    ratios = 0

    # with open("example.txt", "r") as f:
    with open("input.txt", "r") as f:
        schematic = [list(line.strip()) for line in f.readlines()]
        # print(schematic)

    for l, line in enumerate(schematic):
        for c, ch in enumerate(line):
            # Ignore everything other than *
            if ch != "*":
                continue

            coordinates_of_first_digits = set()

            # check 3x3 area around the current *
            for current_row in [l - 1, l, l + 1]:
                for current_column in [c - 1, c, c + 1]:
                    # Ignore if out of bounds
                    if current_row < 0 or current_column < 0 or current_row >= len(schematic) or current_column >= len(schematic[current_row]) or not schematic[current_row][current_column].isdigit():
                        continue

                    # Digit found
                    # Now, find the leftmost digit
                    while schematic[current_row][current_column - 1].isdigit() and current_column > 0:
                        current_column -= 1
                    # Add the coordinates of the leftmost digit to the set
                    coordinates_of_first_digits.add((current_row, current_column))
            
            if len(coordinates_of_first_digits) != 2:
                continue

            numbers = get_numbers(schematic, coordinates_of_first_digits)
            ratios += numbers[0] * numbers[1]

    print(ratios)

def get_numbers(schematic:list, coordinates: list) -> list:
    # Temp list to store the numbers
    numbers = []
    
    # Loop through the coordinates
    for row, col in coordinates:
        # Temp string to store the number
        num_string = ""

        # Loop through the row until current char is a digit and not out of bounds
        while col < len(schematic[row]) and schematic[row][col].isdigit():
            num_string += schematic[row][col]
            col += 1
        numbers.append(int(num_string))

    return numbers


if __name__ == "__main__":
    main()
# Day 2: Cube Conundrum

def main():
    sum = 0
    with open("input.txt", "r") as f:
    # with open("example.txt", "r") as f:
        for num, game in enumerate(f.readlines()):
            color_counts = {"red": 0, "green": 0, "blue": 0}
            sets = game.split(":")[1]
            s = [s.strip() for s in sets.split(";")]
            for string in s:
                for cube in string.split(", "):
                    quantity, color = cube.split(" ")
                    quantity = int(quantity)
                    color_counts[color] = max(color_counts[color], quantity)
            # print(f"Game {num + 1}: {color_counts['red']} red, {color_counts['green']} green, and {color_counts['blue']} blue cubes.")
            # print(color_counts)
            # print(power(color_counts))
            sum += power(color_counts)
        print(sum)

def power(color_counts: dict):
    product = 1
    for x in color_counts:
        product *= color_counts[x]
    return product


main()
# Day 2: Cube Conundrum (Part 1)

def main():
    accepted = []
    with open("input.txt", "r") as f:
    # with open("example.txt", "r") as f:
        for num, game in enumerate(f.readlines()):
            is_possible = True
            color_limits = {"red": 12, "green": 13, "blue": 14}
            sets = game.split(":")[1]
            s = [s.strip() for s in sets.split(";")]
            for string in s:
                for cube in string.split(", "):
                    quantity, color = cube.split(" ")
                    quantity = int(quantity)
                    if quantity > color_limits.get(color):
                        is_possible = False
                        break
                if not is_possible:
                    break
            if is_possible:
                accepted.append(num + 1)

    print(sum(accepted))
    
main()
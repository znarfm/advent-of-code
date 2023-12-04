total = 0
with open("input.txt", "r") as f:
    games = [line.strip() for line in f.readlines()]

for num, game in enumerate(games):
    win_count = 0

    # Parsing
    cards = game.split(":")[1]
    winning, hand = cards.split(" | ")
    winning_list = [int(i) for i in winning.split(" ") if i != ""]
    hand_list = [int(i) for i in hand.split(" ") if i != ""]

    # Count wins per game
    for number in hand_list:
        if number in winning_list:
            win_count += 1

    # Calculate score
    if win_count == 0:
        continue
    total += 2 ** (win_count - 1)

print(total)

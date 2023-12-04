total = 0
with open("input.txt", "r") as f:
    games = [line.strip() for line in f.readlines()]

instances = {}
for num, game in enumerate(games):
    matches = 0

    # Add game to instances
    if num not in instances:
        instances[num] = 1

    # Parsing
    cards = game.split(":")[1]
    winning, hand = cards.split(" | ")
    winning_list = [int(i) for i in winning.split(" ") if i != ""]
    hand_list = [int(i) for i in hand.split(" ") if i != ""]

    # Count matches per game
    for number in hand_list:
        if number in winning_list:
            matches += 1

    # Iterate from current game to the game + matches
    for n in range(num + 1, num + matches + 1):
        # Add each match to the dictionary of instances
        instances[n] = instances.get(n, 1) + instances[num]

print(sum(instances.values()))
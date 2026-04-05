players = ["A", "B", "C", "D", "E"]
pets = ["Wolf", "Dragon", "Phoenix"]

first_mid =  (0 + 4) // 2
print(f"First check is index: {first_mid} which is player: {players[first_mid]}")

next_player = (4 + 1) % 5
print(f"After player E, the next is: {players[next_player]}")

total_combos = len(players) * len(pets)
print(f"Total unique teams: {total_combos}")
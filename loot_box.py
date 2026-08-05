helmets = ["Iron", "Gold", "Diamong"]
capes = ["Red", "Blue"]
swords = ["Short", "Long", "Fire"]
shield = ["Large", "Wide", "Rectangle", "Circle"]

# Possibilites
total_combinations = len(helmets) * len(capes) * len(swords) * len(shield)
print(f"Total unique character skins: {total_combinations}")
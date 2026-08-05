poisoned = 1
stunned = 2
shield = 4
flying = 8

hero_state = 0

hero_state = hero_state | shield
hero_state = hero_state | flying

print(f"Hero state number: {hero_state}")

hero_state = hero_state ^ flying
print(f"Hero state after landing: {hero_state}")

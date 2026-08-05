poisoned = 1
stunned = 2
shield = 4

hero_state = 200
is_poisoned = hero_state & poisoned
is_shielded = hero_state & shield
is_stunned = hero_state & stunned

print(f"Is hero poisoned? {is_poisoned > 0}")
print(f"Has hero shield? {is_shielded > 0}")
print(f"Is here stunned? {is_stunned > 0}")
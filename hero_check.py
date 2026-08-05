hero_state = 5

is_poisoned = hero_state & 1
is_stunned = hero_state& 2
has_shield = hero_state & 4

print(f"Is positioned? {is_poisoned}")
print(f"Is stunned? {is_stunned}")
print(f"Has shield? {has_shield}")
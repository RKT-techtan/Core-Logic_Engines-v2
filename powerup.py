# The tag
poison = 1
shield = 4
flying = 8

# Starting at no looted items
hero_state = 0

# Added flying(1) and shield(2)
# 1
hero_state = hero_state | shield
# 2
hero_state = hero_state | flying

print(f"Hero state: {hero_state}")
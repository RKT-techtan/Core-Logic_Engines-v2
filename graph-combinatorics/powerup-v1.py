# The tag
poison = 1
shield = 4
flying = 8

# Starting at no looted items
hero_state = 4

# Added flying(1) and shield(2)
# 1
hero_state = hero_state | shield
# 2
hero_state = hero_state | flying
# 3(added)
hero_state = hero_state | 8

print(f"Hero state: {hero_state}")
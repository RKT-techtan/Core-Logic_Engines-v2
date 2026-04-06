walking = 1
jumping = 2
crouching = 4

player_state = 0

player_state = player_state | walking
player_state = player_state | jumping

is_jumping = player_state & jumping

print(f"{player_state}")
print(f"{is_jumping > 0}")
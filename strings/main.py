# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
#deel 1
player_first_goal = 'Ruud Gullit'
player_second_goal = 'Marco van Basten'

goal_1 = 32
goal_2 = 54

scores = player_first_goal + ' ' + str(goal_1), player_second_goal + ' ' + str(goal_2)

print(scores)

report = f'{player_first_goal} scores at {goal_1}nd minute \n {player_second_goal} scores at {goal_2}th minute'

print(report)

#deel 2
player = 'Ronald Koeman'
player_lastName = 'Koeman'
firstName = player[:6]
lastName = player[7:13]
firstNameIndex = player.find("R")
lastNameIndex = player.find("K")
last_name_len = len(player_lastName)

print(f'players name: {firstName} {lastName} \n firstname index is {firstNameIndex} and lastname index is {lastNameIndex}')
print(last_name_len)

name_short = player[0] + ' ' + player_lastName

print(name_short)

chant = f'{firstName}! '
print(chant * 3)

good_chant = 'Ronald! '

print(good_chant == chant)
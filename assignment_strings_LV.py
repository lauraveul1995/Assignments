# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# Part 1
scorer_1 = "Ruud Gullit"
scorer_2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54
scorers = scorer_1+" "+str(goal_0)+", "+scorer_2+" "+str(goal_1)
report = f"{scorer_1} scored in the {goal_0}nd minute\n{scorer_2} scored in the {goal_1}th minute"

# Part 2
player = "Ruud Gullit"
first_name_index = player.find("Ruud")
first_name = player[0:4]
last_name_index = player.find("Gullit")
last_name = player[5:]
last_name_len = len(last_name)
name_short = f"{player[0]}. {player[5:]}"
chant = ((first_name+"! ")*len(first_name)).rstrip()
good_chant = chant[22] != " "


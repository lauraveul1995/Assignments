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
index = player.find(" ")
first_name = player[:index]
last_name = player[(index+1):]
last_name_len = len(last_name)
name_short = f"{first_name[0]}. {last_name}"
chant = ((first_name+"! ")*len(first_name)).rstrip()
good_chant = chant[-1] != " "


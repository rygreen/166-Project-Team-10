# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define v = Character("Vinay")
define s = Character("Sai")
define d = Character("Drishti")

# The game starts here.

label act4:
"Nirav arrives at the cricket lot with his newfound friends."
"He notices Sai walking towards the lot with Drishti and a group of boys."

v "Alright Nirav, you'll be the batsman this half. Go get'em."

//game

v "Hey, I've been wathcing that Sai guy, and I think he's our key to victory."
v "Look at him, he looks nervous as all hell."
v "He's good, but not strong mentally."
v "Get him to crack, and this will be our game."
"Nirav steps up as the bowler"


if blood_flag:
"Nirav remembers Sai's uneasiness towards blood."
"He bites his hand hard, drawing blood."
"Nirav smears his blood all over his hand, and waves it at Sai"

else:





    jump act5

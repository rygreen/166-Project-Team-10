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
"Nirav steps up to the batting area."
"Boy" "Hey you, haven't seen you around these parts before. You new here?"
menu:
    "Not too new to beat your ass!":
        jump tough
    "...":
        jump silent
    "Yeah":
        jump plain

label tough:
    "Boy" "Hoo, alright."
    "Boy" "Hope you're still that tough after the game."
    n "{i}What's he talking about. Is he threatening me?"
    n "{i}Aw jeez, I shouldn't have said that."
    jump pitch

label silent:
    "Boy" "Heh, another Sai type."
    "Boy" "No matter, I'll beat you all the same"
    jump pitch
label plain:
    "Boy" "Oh."
    "Boy" "Cool"
    n "..."
    "Boy" "..."
    jump pitch

label pitch:
"Boy" "Super Ultra Double Enhanced Curve Ball"
"He simply tosses the ball to Nirav"
"{i}Plack"
"Nirav easily hits the ball and starts running to the other side"
n "That was some pitch huh"
"Boy" "ARGH, just you wait!"


"The game proceeds, Nirav scores easy runs while Drishti shouts at his teammates"
d "You idiots! Stop losing to this damn noobie!"
d "I'll beat all of you up if you lose this game for us!"
"What's after this is unfinished"
v "Hey, I've been watching that Sai guy, and I think he's our key to victory."
v "Look at him, he looks nervous as all hell."
v "He's good, but not strong mentally."
v "Get him to crack, and this will be our game."
"Nirav steps up as the bowler"


if blood_flag:
    "Nirav remembers Sai's uneasiness towards blood."
    "He bites his hand hard, drawing blood."
    "Nirav smears his blood all over his hand, and waves it at Sai"
    jump after
else:
    "Else Text"
    jump after


label after:
    jump act5

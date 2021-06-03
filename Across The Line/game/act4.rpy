# The script of the game goes in this file.

# Sounds from Zapsplat.com

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
d "I'll beat all of you to a pulp if you lose this game for me!"

"As the ball flies through the air and the bat switches sides. Vinay pulls Nirav to the side."
v "Hey, I've been watching that Sai guy, and I think he's our key to victory."
v "We might be ahead in points right now, but he could let them catch up at any moment."
v "He's good, but not strong mentally."
v "Get him to crack, and this will be our game."

"Nirav steps up to the bowler position, preparing to throw"

menu:
    "Distract Sai":
        jump distract
    "Play Fair":
        jump fair
label distract:
    $ blood_trick = True
    if blood_flag:
        "Nirav stares at Sai, trying to think of a way to throw him off his game."
        "He suddenly remembers Sai's uneasiness towards blood when he refused Sai's bandaid yesterday."
        "Nirav bites his hand hard, drawing blood."
        "Nirav smears his blood all over his hand and the ball, then smiles and gives Sai a little wave. Making sure that he can see the blood"
        "Sai pales and looks sick, and cannot bring him to look at the ball."
        "Nirav throws the ball at Sai. And Sai, not wanting contact with the bloodied ball, dodges out of the way and lets the ball hit the wicket."
        "Sai is dismissed from the batting area, since he is now not allowed to score any more runs in the current innings."
        d "Sai!, WHAT THE HELL ARE YOU DOING?"
        "Needless to say, the game progresses smoothly after that."
        "And Vinay's team easily takes the victory"
        jump after
    else:
        "Nirav stares at Sai, trying to think of a way to throw him off his game."
        "But nothing seems to come to his mind."
        "Nirav shouts some taunts at Sai, calling him a loser and lameass"
        "But Sai seems unaffected"
        "However, despite the ineffectiveness of Nirav's taunts, Vinay's team still takes the victory by a narrow margin."
        jump after

label fair:
    $ blood_trick = False
    "Nirav comtemplates distracting Sai for the victory, but ultimately decides that he does not want to play dirty for his victory"
    "Nirav bowls the ball at Sai and Sai hits it across the line."
    "Vinay, disappointed at Nirav's inaction, decides to take a few jabs at unnerving Sai."
    v "Hey Sai, you ever think about what Drishti will do you guys if you lose?"
    v "Especially to us."
    v "Look at him, he's fuming. I bet he'll break your arm."
    v "You'll never get to play cricket again."
    "But despite Vinay's tauntings, Sai remains unwavered."
    "Luckily for Vinay, the game turned out in his favor after all"
    "Even by a small margin."
    jump after

label after:
    jump act5

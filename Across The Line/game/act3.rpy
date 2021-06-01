# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define v = Character("Vinay")
define s = Character("Sai")
define d = Character("Drishti")


# The game starts here.

label act3:
    v "Alright Nirav, we need to start training for the match. Do you know how to play cricket?"
    menu:
        "Yes":
            v "Well it's time to practice then!"
            jump practice
        "No":
            v "Explains cricket"
            jump practice

label practice:
    v "We only have 2 hours to practice before we have to get out of here. What do you want to work on first?"
    menu:
        "Batting Practice (30 minutes)":
            v "Alright, let's get ready to do some batting!"
            "The boys take turns batting after each other."
            "As the practice goes on, Nirav already feels like he's getting better at batting. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            jump practice_over
        "Fielding Practice (30 minutes)":
            v "Alright, everyone take the field and get ready to move!"
            "Vinay hits balls into the field as the boys run to catch and field to get quicker at beating the runners."
            "As the practice goes on, Nirav feels ready for fielding in the big game. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            jump practice_over
        "Bowling Practice (30 minutes)":
            v "Alright, let’s see who can be our bowlers for the game."
            "The boys take turns bowling and seeing who can throw the fastest."
            "Nirav gives it a shot, feeling confident if he gets called in for the game. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            jump practice_over
        "Running Practice (30 minutes)":
            v "Alright, we need to be ready to run when it's our turn to bat."
            "The boys race each other up and down the field to see who can run the fastest and the longest."
            "Nirav feels ready to give it his all in the big game, even though he is worn out now. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            jump practice_over

label practice_over:
    "All the boys gather together after practicing for the last 2 hours."
    v "I know you guys might be tired now, but I hope you feel ready for the big game tomorrow. We need to win this, the lot is on the line!"

    "As the gang gets hyped up for the game, they notice another group of boys approaching the field."

    v "It’s Drishti and his team!"

    "Drishti walks up with his team sporting a sly grin."
    d "I see you guys just finished practicing, you’re gonna need lots more if you think you can beat us."

    v "Yeah right, Drishti! You’re only here cuz you are scared and needed to scout us out. Get out of here, this is still our lot and always will be!"

    d "Is that so? I guess we will see tomorrow."
    "Drishti laughs and his gang starts to walk away."

    "As they turn to leave, Sai sees Nirav and waves to him remembering their time together the other day. Nirav waves back."

    v "Hey Nirav, you better not take it easy on them tomorrow cuz of that punk kid."
    n "Don’t worry Vinay, I’m here to win."

    "Nirav thinks to himself and doesn’t know if he is quite ready for what it takes to beat the rival gang. All he knows is that he is practiced and will try his best at the game."

    jump act4

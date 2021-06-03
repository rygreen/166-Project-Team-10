# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define v = Character("Vinay")
define s = Character("Sai")
define d = Character("Drishti")

image lot = "cricketLot.png"
image vNormal = "vinayBaseball.png"
image vYell = "vinayBaseballAngry.png"
image drish = "drishCasual.png"
image sai = "saiCasual.png"
image nirav = "niravSad.png"

# The game starts here.

label act3:
    scene lot

    show vNormal
    v "Alright Nirav, we need to start training for the match. Do you know how to play cricket?"
    hide vNormal

    $ practice_time = 120

    $ traitsNum = [0, 0, 0, 0]

    menu:
        "Yes":
            show vNormal
            v "Well it's time to practice then!"
            v "We only have 2 hours to practice before we have to get out of here. What do you want to work on first?"
            hide vNormal
            jump practice
        "No":
            show vNormal
            v "Well let me tell you how it works."
            v "Two teams take turns between fielding and batting."
            v "The team that is battting tries to score runs by hitting the ball that is bowled to them and then running to the wicket on the opposite side."
            v "The fielding team can get the batters out by catching the ball or hitting the wicket before they reach the other side."
            v "The team with the most runs wins the game."
            v "Now that you know how to play, lets get to practicing!"
            v "We only have 2 hours to practice before we have to get out of here. What do you want to work on first?"
            hide vNormal
            jump practice

label practice:
    menu:
        "Batting Practice (30 minutes)":
            show vYell
            v "Alright, let's get ready to do some batting!"
            hide vYell
            "The boys take turns batting after each other."
            "As the practice goes on, Nirav already feels like he's getting better at batting. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            $ previous_time = practice_time
            $ practice_time = (previous_time - 30)
            $ traitsNum = [traitsNum[0] + 1, traitsNum[1], traitsNum[2], traitsNum[3]]
            if practice_time > 0:
                jump practice
            jump practice_over
        "Fielding Practice (30 minutes)":
            show vYell
            v "Alright, everyone take the field and get ready to move!"
            hide vYell
            "Vinay hits balls into the field as the boys run to catch and field to get quicker at beating the runners."
            "As the practice goes on, Nirav feels ready for fielding in the big game. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            $ previous_time = practice_time
            $ practice_time = (previous_time - 30)
            $ traitsNum = [traitsNum[0], traitsNum[1] + 1, traitsNum[2], traitsNum[3]]
            if practice_time > 0:
                jump practice
            jump practice_over
        "Bowling Practice (30 minutes)":
            show vYell
            v "Alright, let’s see who can be our bowlers for the game."
            hide vYell
            "The boys take turns bowling and seeing who can throw the fastest."
            "Nirav gives it a shot, feeling confident if he gets called in for the game. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            $ previous_time = practice_time
            $ practice_time = (previous_time - 30)
            $ traitsNum = [traitsNum[0], traitsNum[1], traitsNum[2] + 1, traitsNum[3]]
            if practice_time > 0:
                jump practice
            jump practice_over
        "Running Practice (30 minutes)":
            show vYell
            v "Alright, we need to be ready to run when it's our turn to bat."
            hide vYell
            "The boys race each other up and down the field to see who can run the fastest and the longest."
            "Nirav feels ready to give it his all in the big game, even though he is worn out now. After 30 minutes goes by, Vinay calls the gang in to see what they are doing next."
            $ previous_time = practice_time
            $ practice_time = (previous_time - 30)
            $ traitsNum = [traitsNum[0], traitsNum[1], traitsNum[2], traitsNum[3] + 1]
            if practice_time > 0:
                jump practice
            jump practice_over

label practice_over:

    $ best_trait = 0
    $ x = 0

    while x < 4:
        $ currBest = 0
        if traitsNum[x] > currBest:
            $ currBest = traitsNum[x]
            $ best_trait = x + 1
        $ x = x + 1


    "All the boys gather together after practicing for the last 2 hours."
    show vNormal
    v "I know you guys might be tired now, but I hope you feel ready for the big game tomorrow. We need to win this, the lot is on the line!"
    hide vNormal

    "As the gang gets hyped up for the game, they notice another group of boys approaching the field."

    show vYell
    v "It’s Drishti and his team!"
    hide vYell

    show drish at right
    "Drishti walks up with his team sporting a sly grin."
    d "I see you guys just finished practicing, you’re gonna need lots more if you think you can beat us."

    show vYell at left
    v "Yeah right, Drishti! You’re only here cuz you are scared and needed to scout us out. Get out of here, this is still our lot and always will be!"

    d "Is that so? I guess we will see tomorrow."
    hide drish
    "Drishti laughs and his gang starts to walk away."
    hide vYell

    show sai
    "As they turn to leave, Sai sees Nirav and waves to him remembering their time together the other day. Nirav waves back."
    hide sai

    show vYell
    v "Hey Nirav, you better not take it easy on them tomorrow cuz of that punk kid."
    n "Don’t worry Vinay, I’m here to win."
    hide vYell

    show nirav
    "Nirav thinks to himself and doesn’t know if he is quite ready for what it takes to beat the rival gang. All he knows is that he is practiced and will try his best at the game."
    hide nirav

    jump act4

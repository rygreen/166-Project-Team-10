# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define v = Character("Vinay")
define s = Character("Sai")
define d = Character("Drishti")


image empty_lot = "cricketLot.png"
image nirav_sad = "niravSad.png"
image nirav = "niravHappy.png"
image restaurant = "inside restaurant.png"
image vinay_casual = "vinayCasual.png"
image vinay_casual_angry = "vinayCasualAngry.png"
image sai_casual = "saiCasual.png"
image sai_casual_sad = "saiCasualSad.png"
image neigh = "neighborhood.jpg"
image ditch = "ditch.jpg"
image drishti = "drishCasual.png"
image black = "black_background.jpg"





# The game starts here.

label act2:


show vinay_casual
v "My name is Vinay, by the way"
v "Don't worry, I can get you home in no time. But first let's go get something to eat!"
hide vinay_casual

scene restaurant
with Dissolve(.5)
"{i}At the restaurant{i}" #maybe we don't need the trasnsition and only use the background to convey them inside a restaurant

show vinay_casual
v "Now, before I can help you get home you have to run some errands for me. You help me, and I help you."
v "You see, We were trying to play cricket today, but it seems like some no good bums stole all our equipment. Now as friends, I think it’d be good for us to help one another out, right?"

hide vinay_casual
show nirav at left
menu:
    "Yeah,sure.":
        hide nirav
        jump choice1_yes

    "No, I don't think so.":
        hide nirav
        jump choice1_no

label choice1_yes:
    show vinay_casual
    v """Great, now I need you to go find us some of our lost equipment.
     It’s somewhere in the neighborhood.
     We can’t play cricket unless we have our equipment.
     """
    jump choice1_done

label choice1_no:
    show vinay_casual
    v """
        Don’t be that way buddy.
        You just help us find our equipment and then I can finish helping you get home.

     """

    jump choice1_done


label choice1_done:

v "Okay so we need you to find our three bats, and six cricket balls. They should be around this neighborhood somewhere."

hide vinay_casual

scene neigh with fade
#for change in scen do show image , with fade (this makes it turn black first and then the new scene)

# do the scene for finding items right here

"Nirav was able to find all the items that Vinay told him to find,although it seemed like someone really wanted to keep them hidden..."

scene ditch
with Dissolve(.5)

"Nirav's arms are full of stuff and he can't see where he is going. He is completely oblivious to the ditch in front of him."
play sound "audio/fall.mp3"
"Bam!!" with vpunch

"..Nirav fell and scraped his knee"

show nirav_sad
n "Oww! It hurts! I hate this! I just want to go home!"
hide nirav_sad

show sai_casual
"Unknown" "Who's there?"
"Unknown" "Oh no!" with hpunch
hide sai_casual
show sai_casual_sad
"Unknown" "You're bleeding! Are you okay, oh my god, what are we gonna do?!"
"Unknown" "Here, take this bandaid."
hide sai_casual_sad

menu:
    "Take the bandaid":
        jump choice2_yes

    "Don’t take a bandaid from the stranger":
        jump choice2_no

label choice2_yes:
    show nirav
    $ blood_flag = False
    n "Thank you, Who are you?"
    hide nirav
    show sai_casual
    s "I’m Sai."
    hide sai_casual

    jump choice2_done

label choice2_no:
    $ blood_flag = True
    show nirav
    n "I don’t know you."
    hide nirav
    show sai_casual
    s "I’m Sai, now can you please put on the bandaid , blood makes me queasy."
    hide sai_casual
    "Nirav takes the bandaid."


    jump choice2_done


label choice2_done:

show sai_casual
s "How are you feeling...uh...sorry...what’s your name again?"
hide sai_casual
show nirav
n "Nirav, My name is Nirav. I’m okay. "
hide nirav
show sai_casual
s " I’m glad! I think you dropped these… oh it's a cricket bat. Do you play cricket? I love cricket!"
hide sai_casual
show nirav
n "No I don't, I was just taking them to some ...friends?"
hide nirav
show sai_casual
s " Oh okay, I can help you! You know, if you want to learn, I can teach you and we can play sometime."
hide sai_casual
"The two boys begin walking towards the lot."
scene empty_lot with fade

show nirav
n "That would be nice but I’m just trying to get home."
hide nirav
show sai_casual
s "What do you mean? "
hide sai_casual
show nirav
n "Yesterday I got lost, and met this boy who said he would help me get home."
hide nirav
show sai_casual_sad
s " Oh no! That must be so scary, i don’t even know what I would do if I got lost, I would probably cry and..."
hide sai_casual_sad
show vinay_casual_angry at right
v "Nirav! Took you long enough! Hey it’s you!"
hide vinay_casual_angry
show sai_casual_sad at left
s "Oh no..."
hide sai_casual_sad
show vinay_casual_angry at right
v "What are you doing here! What are you doing with Nirav?!"
hide vinay_casual_angry
show sai_casual_sad at left
s "Hey guys! Long time no see, but I can explain..."
hide sai_casual_sad
show vinay_casual_angry at right
v "GET OUT OF HERE!" with hpunch
hide vinay_casual_angry

"The boys all run towards Sai"

show sai_casual_sad
s "Ah!"
hide sai_casual_sad

show drishti
"Unknown" "Hey! What do you think you are doing!?"
hide drishti
show sai_casual
s "Drishti!"
hide sai_casual
show vinay_casual_angry at right
v "Drishti, what are y'all doing on my street. Are you looking for a beating? "
hide vinay_casual_angry
show drishti at left
d "You? Beat me? Unlikely, we would beat you all in an instant. "
hide drishti
show vinay_casual_angry at right
v "Oh yeah? If only your cricket skills were as decent as your trash talking skills."

show drishti at left
d """Well I guess there is only one way to test that.
    Your team vs. mine
    Tomorrow afternoon. Winner takes the lot down the street, the losers have to admit that they suck.
    """
hide drishti

"One of Vinay's friends" "Vinay, that's our lot!"

show drishti
d "Don’t tell me you’re scared you’ll lose?"
hide drishti
show vinay_casual_angry at right
v "I’d never lose to you, you're on!"
hide vinay_casual_angry

show drishti
d "See you tomorrow,  let’s go boys! Sai come on."
hide drishti

show sai_casual_sad
s "Sorry Nirav,I guess I'll see you tomorrow."
hide sai_casual_sad


scene black
n "({i}What was that all about? What's up with this rivalry. Sucks that I can't hang out with Sai more{i})"



jump act3

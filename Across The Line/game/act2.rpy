# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define v = Character("Vinay")
define s = Character("Sai")
define d = Character("Drishti")

# The game starts here.

label act2:
v "My name is Vinay, by the way"
v "Don't worry, I can get you home in no time. But first you should finish meeting my friends"
"The two boys walk towards an empty dirt lot"
#here you can just show a picture of the empty lot
v "These are my boys _____" # here add a list of the boys and just one big piture of multiple kids in front of the lot
v "Now that you've all been introduced, let's go get something to eat!"
"{i}At the restaurant{i}" #maybe we don't need the trasnsition and only use the background to convey them inside a restaurant
v "Now, before I can help you get home you have to run some errands for me. You help me , and I help you."
v "You see, We were trying to play cricket today, but it seems like some no good bums stole all our equipment.Now as friends, I think it’d be good for us to help one another out, right?"

menu:
    "Yeah,sure.":
        jump choice1_yes

    "No, I don't think so.":
        jump choice1_no

label choice1_yes:
    #$ menu_flag = True
    v """Great, now I need you to go find us some of our lost equipment.
     It’s somewhere in the neighborhood.
     We can’t play cricket unless we have our equipment.
     """
    jump choice1_done

label choice1_no:
    #$ menu_flag = False
    v """
        Don’t be that way buddy.
        You just help us find our equipment and then I can finish helping you get home.

     """

    jump choice1_done


label choice1_done:

v "Okay so we need you to find our three bats, and six cricket balls. They should be around this neighborhood somewhere."

#for change in scen do show image , with fade (this makes it turn black first and then the new scene)

# do the scene for finding items right here

"Now that Nirav is done finding everything, it is time to report back to Vinay"

"Nirav's arms are full of stuff and he can't see where he is going. He is completely oblivious to the ditch in front of him"

"Bam!!" with vpunch

"..Nirav fell and scraped his knee"

n "Oww! It hurts! I hate this! I just want to go home!" #add picture of nirav crying

"Unknown" "Who's there"
"Unknown" "Oh no!" with hpunch
"Unknown" "You're bleeding! Are you okay, oh my god, what are we gonna do ?!" #add picture of him looking very anxious
"Unknown" "Here, take this bandaid."

menu:
    "Take the bandaid":
        jump choice2_yes

    "Don’t take a bandaid from a stranger":
        jump choice2_no

label choice2_yes:
    $ blood_flag = False
    n "Thank you, Who are you?"
    s "I’m Sai"

    jump choice2_done

label choice2_no:
    $ blood_flag = True
    n "I don’t know you."
    s "I’m Sai , now can you please put on the bandaid , blood makes me queasy."
    "Nirav takes bandaid"


    jump choice2_done


label choice2_done:


s "How are you feeling...uh...sorry...what’s your name again?"
n "Nirav, My name is Nirav. I’m okay. "
s " I’m glad! I think you dropped these… oh its a cricket bat. Do you play cricket? I love cricket!"
n "No I don't, I was just taking them to some ...friends?"
s " Oh okay, I can help you! You know, if you want to learn , I can teach you and we can play sometime."
n "That would be nice but I’m just trying to get home."
s "What do you mean? "
n "Yesterday I got lost, and met this boy who said he would help me get home."
s " Oh no! That must be so scary, i don’t even know what I would do if I got lost, I would probably cry and.."
v "Nirav! Took you long enough! Hey it’s you!"
s "Oh no..."
v "What are you doing here! What are you doing with Nirav?!"
s "Hey guys! Long time no see, but I can explain.."
v "GET OUT OF HERE!" with hpunch

"The boys all run towards Sai"

s "Ah!"
"Unknown" "Hey! What do you think you are doing!?"
s "Drishti!"
v "Drishti, what are y'all doing on my street. Are you looking for a beating? "
d "You? Beat me? Unlikely, we would beat you all in an instant. "
v "Oh yeah? If only your cricket skills were as decent as your trash talking skills."
d """Well I guess there is only one way to test that.
    Your team vs. mine
    Tomorrow afternoon. Winner takes the lot down the street, the losers have to admit that they suck.
    """
"One of Vinay's friends" "Vinay, that's our lot!"
d "Don’t tell me you’re scared you’ll lose?"
v "I’d never lose to you, you're on!"

#the boys are rowady and cheer

d "See you tomorrow,  let’s go boys! Sai come on."
s "Sorry Nirav,I guess I'll see you tomorrow."

n "({i}What was that all about? What's up with this rivalry. Sucks that I can't hang out with Sai more{i})"



jump act3

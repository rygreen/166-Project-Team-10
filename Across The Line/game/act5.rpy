# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define v = Character("Vinay")
define s = Character("Sai")
define f = Character("Nirav's Father")


# The game starts here.

label act5:

"As the game concludes, the onlookers start clearing out, leaving the kids to themselves once more."

s "Nirav! I have to give it to you there, regardless of the result, you were the star of your team!" #if training has boolean want to have it say ’s batting/bowling/fielding

"Drishti storms off but Sai stays behind."

"Vinay is busy celebrating with his friends."

"Nirav sees Sai and walks up to him."

menu:
    "Good game, my friend.":
        jump choice1_friendly

    "Look at the score, the lot’s ours! You should find somewhere else to play.":
        jump choice1_mean

label choice1_friendly:
    s "I appreciate it, and it would be great for our team to play with yours some more in the future."

    n "Great idea! I am very fortunate to have met both you and Vinay, although you two are rivals."

    if blood_flag:
        s "That distraction was quite underhanded. I hope to see less of that in the future though."
        n "I'm sorry, I really wanted to win the game for my group."

    jump c1done

label choice1_mean:
    s "(Shying away) Understood. Deal’s a deal."

    if blood_flag:
        s "That distraction was dirty. You knew how I feel about it."
        n "Hey, game's a game. Our lot now."

    jump c1done


label c1done:

"Everyone starts parting ways. While packing up, Nirav spots a familiar figure amidst the leaving crowd."

n "Father? What are you doing here?"

f "What am I doing here? What are you doing here!? Where did you learn to play cricket?"

menu:
    "I’m the best!":
        jump choice2_best

    "I made some friends in my time away.":
        jump choice2_friends

label choice2_best:
    f "I recall playing catch with you just last week and you were scared of the ball hitting your face, boy! The bat was too heavy for you as well!"

    n "I... uh... let's go home!"

    jump c2done

label choice2_friends:
    f "Are these the friends on the lot here? They seem alright, although they should know better about where to play."

    n "This is a great spot, we just finished a match too."

    jump c2done


label c2done:

n "Can I play more?"

f "Another day, your mother is worried sick."

n "Awww. How did you end up finding me anyway?"

f "I happened to be passing by this area on the way home from work."

n "Oh okay. What’s for dinner?"

f "Hold your horses. Just wait until we get home."

#show field being closed off as walking home

"As Nirav and his father head home, it seems that a sign is being put up near the lot."

"Nirav reunites with his parents at home and catches them up on his adventure in the city. After dinner he proceeds to go to bed."

"Nirav wakes to a sunny day and the birds chirping. Excited, he hurries downstairs catching his father heading to work."

f "Oh Nirav! You’re up early! Can you grab my keys off the counter for me?"

n "Sure, here you go."

#show keys with company on keychain

f "Thank you. I don’t want to be late today, I have a very important meeting. Don’t be out for too long today."

menu:
    "Don’t worry I’ll be home in time for dinner.":
        jump choice3_good

    "It’ll only be a few weeks, it’s fiiiiine.":
        jump choice3_funny

label choice3_good:
    f "Good. I have a busy day today. If it ends well, we might end up living in a nicer place too."

    n "Interesting, good luck! I'm looking forward to meeting my friends again."

    jump c3done

label choice3_funny:
    f "Hmph, and I suppose I'll find you with a new gang of ruffians on a random plot of land again too."

    n "Hey! I picked up a few skills and friends along the way. We're meeting again today as well."

    jump c3done


label c3done:

f "Come sooner please. I have to go, have a good day."

"As both Nirav and his father head to their destinations, we see Nirav and a huddled group of his friends at the cricket field, now fenced off."

#show background of closed off lot

n "What’s up guys? Why are we crowded here?"

v "The lot’s been closed off."

"The sign reads: COMING SOON: Premium apartments brought to you by Dubai Better Living™!"

n "Oh. My. God."

v "What is it?"

n "Not only is the lot closed off, but look at why it has been closed."

v "Yeah, just for some apartments right?"

n "Yes, but the company that’s developing the land… now I know why my dad found me here. He’s a project manager there!"

return

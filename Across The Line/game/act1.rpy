
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define m = Character("Unknown Man1")
define u = Character("Unknown Man2")
define w = Character("Waiter")
define k = Character("Kid")

image crowd1 = "crowd1.png"
image crowd2 = "crowd2.png"
image kids = "kids.png"
image waiter = "waiter.png"
image unknown man1 = "unknown man1.png"
image unknown man2 = "unknown man2.png"
image Nirav = "Nirav.png"
image Vinay = "Vinay.png"

image inside vehicle = "inside vehicle.png"
image inside restaurant = "inside restaurant.png"
image petrol station = "petrol station.png"
image roads = "roads.png"
image square = "square.png"



# The game starts here.

label act1:
show crowd1
show crowd2
show Nirav
n "Mom? Dad?"
"Unknown Voice: Got it."
show inside vehicle
menu:
    "Option 1" :
        n "Who are you?"
        "Nirav's voice woke up the man who’s sleeping and was forced to faint again."
    "Option 2" :
        "Nirav keep silence and observe surrounding."
        "Nirav see two men at the front of the car, one is driving the car and the other is sleeping. "
        m"(talking to someone through the phone) Hey, we're about to reach the Delhi's outskirts."
label after_menu:
"The car kept moving until it reached a petrol station in the outskirts of Delhi. "
show petrol station
show unknown man1
m "Hey, I’m going to get some Thali, keep an eye on this kid."
show unknown man2
u "relax bro, he’s fainted. Bring me some Nans!"
show unknown man1
m "Okay, I’ll be right back."
"several minutes later"
show unknown man2
u "Damn, what’s taking him so long?"
"the man leaves, Nirav wakes up and found out the door isn’t locked"
"Shouts from far away"
show unknown man1 at left
m "Hey man, don’t rush me!"
show unknown man2 at right
u "Why don’t you hurry the hell up then"
m "Shouldn’t you be watching the kid?"
u "Don’t worry about him, he’s knocked out cold."
n "It’s my only chance…"
"Nirav opened the door and ran quickly to the wild"

show roads

"Nirav finally reached Delhi’s downtown"
show inside restaurant
n "(hungry and tired in front of a restaurant) “ I have to get some food…"
show waiter
n "(talked to the waiter) “Please, can you give me some food? I’m starving. I don’t have any money but I can work for you."
w "Sorry pal, we’re not a charity."
show square
"Nirav leaves the restaurant, very disappointed, wandering in the square"
show kids
"several kids grouped there playing Cricket"
k "Hey! You!"
show Nirav
n "me?"
show kids
k "Duh, you. Man, you look terrible. What happened to you?"
show Nirav
n "I’m not quite sure."
n "I just woke up in the back of some truck."
show kids
k "Hmm, I see."
k "Where are you from?"
show Nirav
n "Mumbai. But I got lost..."
"Nirav’s stomach is making noise"
n "Sorry… I haven’t eaten anything for the whole day."
show kids
k "Wow that’s really far."
"Kids whispered from a second"
k "Hey, do you want to join us? We can get you some food and a place to sleep."
show Nirav
n "(touched) “Thanks...thank you guys…"
show kids
k "No problem. What’s your name?"
show Nirav
n "My name is Nirav!"

    

jump act2

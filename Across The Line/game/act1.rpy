
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("Nirav")
define m = Character("Unknown Man1")
define u = Character("Unknown Man2")
define w = Character("Waiter")
define k = Character("Kid")

image crowd1 = im.Scale("crowd1.png", 800, 600)
image crowd2 = im.Scale("crowd2.png", 800, 600)
image waiter = "waiter.png"
image unknown man1 = "unknown man1.png"
image unknown man2 = "unknown man2.png"
image Nirav = "niravHappy.png"
image Vinay = "vinayCasual.png"

image inside vehicle = im.Scale("inside vehicle.png", 1280, 720)
image inside restaurant = im.Scale("inside restaurant.png", 1280, 720)
image petrol station = im.Scale("petrol station.png", 1280, 720)
image roads = im.Scale("roads.png", 1280, 720)
image square = im.Scale("square.png", 1280, 720)
image black = im.Scale("black.png", 1280, 720)
image cricketlot = im.Scale("cricketLot.png", 1280, 720)



# The game starts here.

label act1:
scene square
show crowd1 with fade
hide crowd1
show crowd2 with fade
hide crowd2
show Nirav
n "Mom? Dad?"
hide Nirav
hide square
scene black
"Unknown Voice: Got it."
hide black
scene inside vehicle
"Nirav wakes up in a vehicle in panic."
menu:
    "(Ask)Who are you?":
        "Nirav's voice wakes up the man who is sleeping and was knocked out again."
    "Keep silence and observe surrounding":
        "Nirav see two men at the front of the car, one is driving the car and the other is sleeping. "
        m"(talking to someone through the phone) Hey, we're about to reach Delhi's outskirts."
label after_menu:
"The car continues moving until it reached a petrol station in the outskirts of Delhi. "
hide inside vehicle
scene petrol station
show unknown man1
m "Hey, I’m going to get some Thali, keep an eye on this kid."
hide unknown man1
show unknown man2
u "Relax bro, he’s fainted. Bring me some Naan!"
hide unknown man2
show unknown man1
m "Okay, I’ll be right back."
hide unknown man1
"Several minutes later"
show unknown man2
u "Damn, what’s taking him so long?"
hide unknown man2
"The man leaves, Nirav wakes up and found out the door isn’t locked."
"Shouts from far away"
show unknown man1
m "Hey man, don’t rush me!"
show unknown man2
u "Why don’t you hurry the hell up then"
m "Shouldn’t you be watching the kid?"
u "Don’t worry about him, he’s knocked out cold."
hide unknown man1
hide unknown man2
show Nirav
n "It’s my only chance…"
hide Nirav
"Nirav opens the door and runs quickly into the outskirts."
hide petrol station
scene roads
"Nirav finally reaches Delhi’s downtown."
hide roads
scene inside restaurant
n "(Hungry and tired in front of a restaurant) “ I have to get some food…"
show waiter
n "(Talking to the waiter) “Please, can you give me some food? I’m starving. I don’t have any money but I can work for you."
w "Sorry pal, we’re not a charity."
hide inside restaurant
hide waiter
scene square
show Nirav
"Nirav leaves the restaurant, very disappointed, wandering in the square"
hide Nirav
hide square
scene cricketlot
show Vinay
"several kids grouped there playing Cricket"
k "Hey! You!"
hide Vinay
show Nirav
n "me?"
hide Nirav
show Vinay
k "Duh, you. Man, you look terrible. What happened to you?"
hide Vinay
show Nirav
n "I’m not quite sure."
n "I just woke up in the back of some truck."
hide Nirav
show Vinay
k "Hmm, I see."
k "Where are you from?"
hide Vinay
show Nirav
n "Mumbai. But I got lost..."
"Nirav’s stomach is making noise"
n "Sorry… I haven’t eaten anything for the whole day."
hide Nirav
show Vinay
k "Wow that’s really far."
"The other kids whisper amongst themselves for a little bit, occasionally stealing a glance at Nirav."
k "Hey, do you want to join us? We can get you some food and a place to sleep."
hide Vinay
show Nirav
n "(touched) “Thanks...thank you guys…"
hide Nirav
show Vinay
k "No problem. What’s your name?"
hide Vinay
show Nirav
n "My name is Nirav!"
hide Nirav



jump act2

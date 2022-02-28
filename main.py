#starter stuff
import random
def bars():
    print("0================0")
def logo():
    print("------------EGames")
    print("(\___/)")
    print("|0=W=0|")
    print("------------------")

#goals
"""
-choices affect stats
-if stats == etc
-stay alive as long as you can
-a bunch of prompts that show up at random
-setting:sapce
-bob
"""
#add or subtract to change results(-2 - 2)
health = 0

#score system
score = 0

#scenes
def sce_one():
    bars()
    global health
    print("Steve: Someone stole my spaceship!")
    print("Steve: Ive been drifting around forever")
    print("Steve: Can you help me find that no life?")
    x = int(input("Yeah lets get that loser(1) or Sorry im busy...(2): "))
    if x == 1:
        print("Steve: Yeah!")
        print("Narrator: After traveling with the old man for a while you notice youre just going in cricles")
        print("Steve: Sorry to do this to you kid")
        print("Steve: Hands in the air this is a robbery!")
        health = health - 1
        gb_meter()
    else:
        print("Steve: You dang youngsters always busy")
        print("Steve: Back in my day we always had time to be robbed")
        print("Steve: Bye you whipper snapper!")
        gb_meter()
def sce_two():
    global health
    bars()
    print("Bob: Hi sir, can I have a momment of your time?")
    x = int(input("Yes of course(1) or No I dont have time to hear you religious rambling(2)"))
    if x == 1:
        print("Bob: Im glad to hear it!")
        print("Bob: If you can guess the number im thinking of right now from 0-3 Ill give you useful info")
        xx = random.randint(0, 3)
        xm = int(input("Type guess here: "))
        if xm == xx:
            print("Bob: Correct!")
            print("Bob: My info is dont trust people names Steve")
            print("Have a good day!")
            health = health + 1
            gb_meter()
        else:
            print("Bob: sorry the number was ")
            print(xx)
            print("Bob: mabye next time friend Ill see you around!")
            gb_meter()
    else:
        print("Bob: Well no need to be so rude :(")
        gb_meter()

#scene picker
def sce_pick():
    xx = random.randint(1, 2)
    if xx == 1:
        sce_one()
    else:
        sce_two()
#based on health ranging from -2 - 2 it will change the graphic
def gb_meter():
    global health
    global health_meter
    health_meter = ["v", "v", "|", "^", "^"]
    if health == -1:
        health_meter = ["v", "|", "0", "^", "^"]
    elif health == -2:
        health_meter = ["|", "v", "0", "^", "^"]
    elif health == 1:
        health_meter = ["v", "v", "0", "|", "^"]
    elif health == 2:
        health_meter = ["v", "v", "0", "^", "|"]
    else:
        health_meter = ["v", "v", "|", "^", "^"]
    print(health_meter)

#main menu
def menu():
    logo()
    print("Welcome to space!")
    print("In this experience youll try to stay alive while navigating alien prompts")
    print("You will see how youre doing based on this scale [v,v,|,^,^]")
    print("If you go to far left you lose, and too far right you get 1-2 extra points that round")
    print("You represent the line (this thing --> |)")
    print("The goal is too end the game with the most amount of points")
    print("Enjoy!")
    x = input("Press enter to start: ")
    sce_pick()
menu()

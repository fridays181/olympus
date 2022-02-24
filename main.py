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
-setting:greek mythology
-run mount olympus and let in people / gods according to lore
"""

#add or subtract to change results(-2 - 2)
health = 0

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
    print("In his game you play as the mighty greek god")
    print("BOB!")
    print("As bob you will choose who is allowed up the mount olympus")
    print("If youre choices are good the gods will reward you")
    print("But if youre choices are bad you will be punished :)")
    print("You will see how you are with the gods based on this scale [v,v,|,^,^]")
    print("If you go to far left you lose, and too far right you get 1-2 extra points that round")
    print("You represent the line (this thing --> |)")
    print("Enjoy!")
    x = input("Press enter to start: ")

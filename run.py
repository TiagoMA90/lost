from datetime import date
from datetime import datetime
import time
logtime = datetime.now()

def pact():
    print("Very well. I will scavange for edibles.")

def start():
    print('"Transmission accepted"')
    print("")
    name = input("Who is this? What is your name? ")
    time.sleep(2)
    print("Finally... You must be from the Operator, from Stationary division EPSILON.")
    time.sleep(1)
    print("I have been trying to contact you guys for days.")
    time.sleep(2)
    print(f"Listen " + name + " ... I am Jerry... and I am the sole surviour of SIGMA-02, research team.")
    time.sleep(2)
    print("Me and my crew disembarked from Earth en route to Mars two months ago...")
    time.sleep(3)
    print("A pick up vessel was supposed to dock this morning and pick us up... Except, it never landed...")
    print("There was an incident last night, I dont know what exactly happened...")
    time.sleep(3)
    print("I woke up this morning in my pod and my team disapeared.")
    time.sleep(1)
    print("Our internal hardware is damaged and I cannot salvage anything from...")
    print()
    
    print("Connection lost...")
    print("Reconnecting...")
    time.sleep(2)
    print("Reconnecting...")
    time.sleep(9)
    print("Connection established")
    print(logtime)
    print("")
    print("Are you still here? The connection is weak... It is imperative that you help me!")
    time.sleep(2)
    print("Help is not coming! I need to get out of here. ")
    tim.sleep(1)
    act_one = input("Can you stay online and help me?")
    if act_one == "y" or act_one == "Y" or act_one == "yes" or act_one == "Yes" or act_one == "YES" or act_one == "sure" or act_one == "ok":
            pact()
    elif act_one == "n" or act_one == "N" or act_one == "no" or act_one == "No" or act_one == "NO":
            print("Call suspended")


print("-------------------")
print("      ㄥㄖ丂ㄒ")
print("-------------------")
time.sleep(2)
print("Incoming signal...")
time.sleep(3)
print("Incoming signal...")
time.sleep(1)
print("Incoming signal...")
print("Connecting...")
time.sleep(0.3)
print("Connection established")
print(logtime)
print("EPSILON Station-P3, Mars")
print()
time.sleep(2)
print("Hello?")
time.sleep(1)
print("Hello?! Anybody there?")
print("")

startgame = input("Accept transmission? (Y/N)")
if startgame == "y" or startgame == "Y" or startgame == "yes" or startgame == "Yes" or startgame == "YES":
    start()
elif startgame == "n" or startgame == "N" or startgame == "no" or startgame == "No" or startgame == "NO":
    print("Call suspended")
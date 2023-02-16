from datetime import date
from datetime import datetime
from datetime import timedelta
import time
import random

def gameover():
        print('"Connection lost..."')
        time.sleep(2)
        print('"Reconnecting..."')
        print('"Failed to connect"')
        time.sleep(3)
        print(" ")
        print("")
        print(" ")
        print(" ")
        print(" ")
        print("GAME OVER")
        print(" ")
        print(" ")
        print(" ")
        while True:
            print('"Retry (yes / no)"')
            go_continue = str(input(""))
            print(" ")
            print(" ")
            if go_continue == "yes" or go_continue == "y" or go_continue == "accept":
                start()
            elif go_continue == "no" or go_continue == "n" or go_continue == "decline":
                print('"Call Declined"')

def countdown():
    print("Ready for take off!")
    for countdown in range(9, 0, -1):
        print(countdown)
        time.sleep(1)
        print()
        print()
        print()
        print(" THE END ")
        print()
        print()
        print()
        print()
        print()
        print("created and develped by Tiago Moura")


def getaway():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def display_board():
        print("? |" + " A:" + "| " + "B:" + "| " + "C:")
        print("D:| " + str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
        print("E:| " + str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
        print("F:| " + str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]))
        
    def playgame():
        display_board()
        position = input("Input the position ")
        position = int(position)
        board[position] = "X"
        
        if position == 7:
            countdown()
        else:
            gameover()
    
    playgame()

def takeoff():
    print("Great! So far, so good.")
    time.sleep(3)
    print("The systems are running...")
    time.sleep(1)
    print("I must input the correct number, as in this schematics.")
    time.sleep(3)
    print("Hang on a second, I am uploading the data to you...")
    time.sleep(4)
    print("We should have two tries... before  permanent system shutdown.")
    time.sleep(2)
    print("have you seen anything like it? Which one is the execution number?")

    getaway()


def puzzle():
    login = ("python")
    password = login
    underline = ["*", "*", "*", "*", "*", "*"]
    entry = []
    attempts = 3
    correct = 0

    print("*"*len(password))

    while True:
        print("Input characters:")
        characters = str(input("Characater: "))
        entry.append(characters)
    
        if password == "python":
            if characters in password:
                underline[password.index(characters)] = (characters)
                print(underline)
                correct += 1
            else:
                print("This is the incorrect character!")
                attempts -= 1
                print("Remaining tries {}". format(attempts))
            if attempts <= 0:
                gameover()
            if correct == 6:
                print('"Access granted. Systems online"')
                time.sleep(2)
                print("Bingo!, you unlocked it! Wait a second... ")

                takeoff()


def shuttle():
    print("Here I am, I found the Emergency shuttle. Ernst made it here, before he went back to base. I can see his workers tag.")
    time.sleep(1)
    print("I imagine he didn't have the card with him, so he had to go back.")
    time.sleep(2)
    print("The power cells are in place.")
    time.sleep(1)
    print("I just need to power up the ignition panels.")
    time.sleep(5)
    print("The power is on!")
    time.sleep(2)
    print("A log in is requiered to access the systems, the characters should be introduced one by one...")
    time.sleep(2)
    print("Any clues?")

    puzzle()

def negotiation():
    captainscore = 0
    diazscore = 0

    while True:
        hands = ["Rock", "Paper", "Scissors"]
        captain = random.choice(hands)
        print()
        diaz = input("Which hand should I play? ").capitalize()
        
        if diazscore == 2:
            print("I beat him, fair and square!!!...")
            time.sleep(3)
            print("Does this mean...")
            time.sleep(2)
            print("I refused to accept his gun... He kept his word and let me go.")
            time.sleep(5)
            print("He also said, 'F + B' should launch the shuttle.")
            time.sleep(2)
            print("I am going to the shuttle.")
            time.sleep(2)
            print("I'll get back to you in a moment shortly.")
            time.sleep(5)
            print("Did you hear that? I just heard a gunshot...")
            time.sleep(2)
            print("I suppose he took matters with his own hands.")
            time.sleep(4)
            shuttle()
            break
        elif captainscore == 2:
            gameover()
            break
            
        if diaz == captain:
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I tied against the Captain, we have to go again.")
        elif diaz == "Rock" and captain == "Scissors":
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I won this round against the Captain!")
            diazscore += 1
        elif diaz == "Paper" and captain == "Rock":
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I beat him this round!")
            diazscore += 1
        elif diaz == "Scissors" and captain == "Paper":
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("The Captain lost this round!")
            diazscore += 1
        else:
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I lost!")
            captainscore += 1


def pitsalt():
    print("I made my way to the pits.")
    time.sleep(2)
    print("It's very wind here...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(2)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(4)
    print("It should take a while to find a safe zone...")
    time.sleep(3)
    print("There is something moving in the distance... someone...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(3)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(6)
    print("This conection... Don't die on me now...")
    time.sleep(2)
    print("Someone is coming this way...")
    time.sleep(3)
    print("Is that the Captain?")
    time.sleep(2)
    print("He looks very ill... I should go up to him at once.")
    time.sleep(15)
    print("The Captain is out of his head...")
    time.sleep(2)
    print("Wait! He has a gun... and is demanding the keycard from me.")
    time.sleep(1)
    print("There is only one passenger seat in that emergency shuttle...")
    time.sleep(2)
    print("He insists the shuttle is his ticket home...")
    time.sleep(5)
    print("The egoistic bastard... he is also infected... He is as good as dead... there is no cure for what he has.")
    time.sleep(1)
    print("What should I do? He sees a dilemma on his hands too, and would hate to kill me for the card...")
    time.sleep(4)
    print("We agreed on a stand off, of 'Rock Paper Scissors'...")
    time.sleep(2)
    print("Never in my life would I bet my life this way... careful not to to play around..., best out of 3... the captain is not fooling...")
    time.sleep(2)

    negotiation()


def finaldeed():
    while True:
        print("What do you think I should do? (kill him and take the keycard / trade the gun for the key)")
        decisionmaker = input("")
        decisionmaker = decisionmaker.lower()
        if decisionmaker == "trade" or decisionmaker == "give" or decisionmaker == "give him the gun" or decisionmaker == "trade the gun for the card":
            print("You better know what I am doing... I will give him my gun for the keycard...")
            time.sleep(2)
            print("He thanked me... seemed desperate to have it...")
            time.sleep(3)
            print("I don't know what he will do with that gun... There was only one bullet in that gun...")
            time.sleep(2)
            print("But he repeatedly said 'F + B' I fail to comprehend what he meant...")
            time.sleep(4)
            print("Lets get a move on. The shuttle is just ahead!")
            time.sleep(5)
            print(" ")
            print('"Connection lost..."')
            time.sleep(1)
            print('"Reconnecting..."')
            time.sleep(2)
            print('"Reconnecting..."')
            print('"Connection established"')
            print(" ")
            print("I just heard a gunshot behind the pits... Captain?")
            time.sleep(2)
            print("Oh... I see now...")
            time.sleep(4)
            print("The shuttle is just ahead.")
            time.sleep(5)
        
            shuttle()


        elif decisionmaker == "shoot" or decisionmaker == "shoot him dead" or decisionmaker == "kill" or decisionmaker == "kill him":
            print("It's the last bullet... I better know what I am doing...")
            print("I wonder if putting him out of his misery is the correct thing to do.")
            time.sleep(2)
            print("Will this make me a murderer? I guess there is no other way. Everyone for himself, right?")
            time.sleep(7)
            print("I killed him...")
            time.sleep(3)
            print("This is on both of us. My actions are a reflection of your decisions.")
            time.sleep(5)
            print("Let's get the keycard and never look back... he has something written on his hand.")
            time.sleep(2)
            print('It says "F + B"')
            time.sleep(3)
            print("I should keep going... The shuttle is just ahead...")
            time.sleep(5)
        
        shuttle()

def settlement():
    takeaction = input("")
    takeaction = takeaction.lower()
    if takeaction == "threaten" or takeaction == "threaten him" or takeaction == "threat" or takeaction == "point the gun at him":
        print("I'll insist...")
        time.sleep(2)
        print("I pointed the gun at him!")
        time.sleep(6)
        print("Is he nuts? He made a proposal, the keycard of the shuttle in exchange for my gun...")
        time.sleep(4)
        print("If I give up the gun, he will kill me and take the shuttle... nonsense...")
        time.sleep(2)
        print("I could just kill him and take the keycard for myself, but... I am not a murderer...")
        print("You are my guide here...")
        time.sleep(1)
        
        finaldeed()


    elif takeaction == "shoot" or takeaction == "shoot him dead" or takeaction == "kill" or takeaction == "kill him":
        print("It's the last bullet... I better know what I am doing...")
        print("I wonder if putting him out of his misery is the correct thing to do.")
        time.sleep(2)
        print("Will this make me a murderer? I guess there is no other way. Everyone for himself.")
        time.sleep(7)
        print("I killed him...")
        time.sleep(3)
        print("This is on both of us. My actions are a reflection of your decisions.")
        time.sleep(5)
        print("Let's get the keycard and never look back.")
        time.sleep(2)
        
        shuttle()


def pits():
    print("I made my way to the pits...")
    time.sleep(2)
    print("It's very wind here...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(2)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(4)
    print("It should take a while to find a safe zone...")
    time.sleep(5)
    print("Hold on...")
    time.sleep(3)
    print("There is something moving in the distance... someone...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(3)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(6)
    print("Don't die on me now.")
    time.sleep(2)
    print("Someone is coming this way...")
    time.sleep(3)
    print("Is that the Captain?")
    time.sleep(2)
    print("Great, he has the keycard, so... perhaps no need to bypass the ignition panels.")
    print("He looks very ill... I'll get back to you once I speak with him")
    time.sleep(15)
    print("The Captain is out of his head...")
    time.sleep(1)
    print("There is only one passenger seat in that emergency shuttle... and he carries the card")
    time.sleep(2)
    print("He insists the shuttle is his ticket home and everyone for himself...")
    time.sleep(5)
    print("I understand his point of view, but should I stand ground and submit to his demands???")
    time.sleep(2)
    print("The egoistic bastard... he is also infected... He is as good as dead... there is no cure for what he has.")
    time.sleep(1)
    print("How should I confront him? (threaten him/shoot him dead)")
    time.sleep(3)

    settlement()



def keycard():
    password = "virgo"
    guess = ""
    countguess = 0
    maxguess = 2
    outofguess = False

    while guess != password and not(outofguess):
        if countguess < maxguess:
            guess = input("Password: ")
            guess = guess.lower()
            countguess = countguess + 1
        else:
            outofguess = True

    if outofguess:
        gameover()
    else:
        print('"The keycard has been been disarmed"')
        print("")
        print("This should ignite the shuttle.")
        time.sleep(2)
        print("I'll walk a little further...")
        time.sleep(4)
        print("This is beautiful, never seen a planet with two suns.")
        time.sleep(3)
        print("The view is rather spectacular, but very hot up here, No wonder there is no nightime in this planet...I can see the stars though.")
        time.sleep(2)
        print("I can see the pits from up here. I'll get back to you once I get more updates.")
        time.sleep(6)
        
        pitsalt()


def plateau():
    print("It's a long walk, and very hot in the open. I should get back to you in a minute.")
    time.sleep(30)
    print("Great, I am back. Good to know you waited for me... I finally reached the checkpoint.")
    time.sleep(3)
    print("Do you want to hear the good news or bad news? Well, I assume both...")
    time.sleep(3)
    print("The good news is... I found part of my crew... Davies and Laurent.")
    time.sleep(4)
    print("The bad news... They are dead. But not just dead...")
    time.sleep(3)
    print("Their faces are full of fungus... infested by mold... an infection.")
    time.sleep(4)
    print("They died of something extraordinary... like a sickness or some sort...")
    time.sleep(2)
    print("Horrific...")
    time.sleep(5)
    print("Hold on...")
    time.sleep(3)
    print("I found the keycard for the shuttle by their camp. This should come in handy, till we reach our next destination.")
    time.sleep(2)
    print("It requires a password in order to unock it... Laurents pad has a note...")
    print("It reads...")
    print(" ")
    time.sleep(5)
    print("----------------------------------------------------------------------------------------------------")
    print("DOWNLOADING DATA...")
    print("----------------------------------------------------------------------------------------------------")
    print(datetime.now() + timedelta(days=101773, hours=-10))
    print("'Be careful, something sinister dwells in this ecosystem.'")
    print("'If you see it run and don't look back. Davies and I managed to escape, but we have been infected...")
    print("'I also retrieved the keycard from the scrapyard, there is also some food left...'")
    print("'If you want to open the kit, containing the keycard, it should be the 6th constellation sign of the Zodiac, planet Earth.'")
    print("'Careful not to mistype it else it will selfdestruct, with you included. The blast can be fatal.")
    print("'I had to arm it, because of Van Beek, me and Davies made a detour from him... You have two tries, before it explodes.'")
    print("'The stars, so bright... I think I will lie down here for a while...'")
    print("- Martin Laurent")
    print("----------------------------------------------------------------------------------------------------")
    
    keycard()


def risk():
    outcome = ["hit", "miss"]
    shot = random.choice(outcome)
    if shot == "hit":
        print("I shot it!!!")
        time.sleep(2)
        print("But, it ran off! I better make my way to the exit!")
        time.sleep(5)
        print("I managed to reach the exit... How I missed the sunlight...")
        time.sleep(8)
        print("I need to take a breath...")
        time.sleep(4)
        print("Whatever that thing was... it go hold of them...")
        print("I still have one bullet left...")
        time.sleep(3)
        print("I can see the pits from down here. I'll contact you once I get to my next checkpoint.")
        time.sleep(15)
        
        pits()
        
    else:
        print("Damn...I missed it! No more bullets...!")
        time.sleep(1)
        print("I saw it in a flash. The horror...")
        time.sleep(3)
        gameover()



def fightorflee():
    caveencounter = input("")
    caveencounter = caveencounter.lower()
    if caveencounter == "run" or caveencounter == "r" or caveencounter == "run away" or caveencounter == "run towards the exit":
        print("OK... I am running, I AM RUNNING!!!")
        time.sleep(10)
        print("It's after me!")
        time.sleep(2)
        print("I made it... I made it to the exit!")
        print("I can see the pits from down here. I'll contact you once I get to my next checkpoint.")

        pits()

    elif caveencounter == "sneak" or caveencounter == "sneak past it" or caveencounter == "stealth" or caveencounter == "move quietly":
        print("Very well... I'll move quietly...")
        time.sleep(5)
        print("Perhaps it won't hear me...")
        time.sleep(3)
        print("It's hard to see... I feel warm breathing on my neck...")
        print("What is this?... NO WAIT!!!")

        gameover()

    else:
        print("This is a shot in the dark. If I miss, I am dead...")
        print("Steady...")

        risk()

def gunholster():
    password = "emma"
    guess = ""
    countguess = 0
    maxguess = 3
    outofguess = False

    while guess != password and not(outofguess):
        if countguess < maxguess:
            guess = input("Password: ")
            guess = guess.lower()
            countguess = countguess + 1
        else:
            outofguess = True

    if outofguess:
        gameover()
    else:
        print('"The holster has been unlocked"')
        print("")
        print("I never used a gun before, but should be easy to shoot right?")
        time.sleep(4)
        print("Wait... something is strange...")
        time.sleep(3)
        print("The ground is silent and the air is still... Everything is too quiet.")
        time.sleep(4)
        print("I can no longer hear or feel the droplets of water falling down from the ceiling...")
        time.sleep(5)
        print("The issing is gone...")
        time.sleep(1)
        print("Should I run, move quietly towards the exit or shoot my way through? (run / sneak / shoot)")
        fightorflee()


def cave():
    print("Very well then... I shall enter the depths of this cave.")
    time.sleep(5)
    print("I wonder if this was a wise decision...")
    time.sleep(5)
    print("Can't see much... The air is cold... and the soil is wet.")
    time.sleep(2)
    print("It echoes in here, I can hear drops of water... Could this mean life???")
    time.sleep(7)
    print("What was that?!!...")
    time.sleep(3)
    print("The darkness must be playing tricks on me...")
    time.sleep(2)
    print("Ever felt like there is someone watching you?")
    time.sleep(6)
    print("Did you hear that?")
    time.sleep(2)
    print("There is definetly something in here... I can hear it... it is hissing from afar.")
    time.sleep(4)
    print("Rather creepy... Can't make scence from where is coming from.")
    time.sleep(7)
    print("Hardly any light in here, but I see an opening at the end of the tunel.")
    time.sleep(5)
    print("I am surprised the connection is still good in here....")
    time.sleep(3)
    print("On my way towards the exit...")
    print("Wait. What is this?...")
    time.sleep(5)
    print("The smell of blood... there's a metalic scent...")
    time.sleep(2)
    print("I found part of my crew, what happened in here???")
    time.sleep(1)
    print("Fujin was shot dead...Van Beek whatever happened to him, he has no wounds, but has an infection all over his face.")
    time.sleep(5)
    print("What happened to them...")
    time.sleep(2)
    print("I should keep moving... But wait... I can perhaps take their gun.")
    time.sleep(3)
    print("It requires a password... to remove it from from Van Beeks holster...")
    time.sleep(3)
    print("There is a note... I am uploading it to you, right now...")  
    print("")
    print("----------------------------------------------------------------------------------------------------")
    print("DOWNLOADING DATA...")
    print("----------------------------------------------------------------------------------------------------")
    print(datetime.now() + timedelta(days=101770, hours=-5))
    print("'Christ... This Fujin guy, is flipping out... He insists the only gun onboard belongs to him and to himself only... while my life gets to depend on him.'")
    print("'Who put him in charge? He doesn't let anyone near it... The selfish bastard... When he least expects, I will grab it.'")
    print("'He thinks he has everything covered... I saw him changing the password for the holster, it is the anthropolists first name...'")
    print("'He had a crush on her since we made preparations in Mars... what an idiot...'")
    print("'Mars... Earth... Home... I haven't been there since I've been working for SIGMA-02.'")
    print("'It doesn't matter now. I need to get that gun. I must fend myself against whatever is in this cave.' - Van Beek")
    print("----------------------------------------------------------------------------------------------------")
    print("I should have a few tries before I attract unwanted attention.")

    gunholster()



def pact():
    time.sleep(2)
    print("Great. Very well. I need you to help me navigate to the Emergency Shuttle.")
    time.sleep(1)
    print("It detached 24km southwest from here, should take a few hours from where I stand.")
    print("My GPS is damaged..., but you should be able to guide me through this ecosystem.")
    time.sleep(1)
    print("I am walking towards my next destination...")
    time.sleep(2)
    print("I'll be uploading data profiles to you in the meantime...")
    print("Not that it matters, this is futile information now...")
    time.sleep(3)
    print(" ")
    print("............................")
    print("DOWNLOADING DATA...")
    print("............................")
    print("Name: Ernst, Klaus")
    print("Age: 50")
    print("Planet: Earth, CH")
    print("Duty: Biologist")
    print("Status: Dead")
    time.sleep(2)
    print("............................")
    print("Name: Fujin, Akira")
    print("Age: 32")
    print("Planet: Earth, JP")
    print("Duty: Geologist")
    print("Status: Dead")
    time.sleep(3)
    print("............................")
    print("Name: Davies, Emma")
    print("Age: 33")
    print("Planet: Earth, EN")
    print("Duty: Anthropologist")
    print("Status: Dead")
    time.sleep(3)
    print("............................")
    print("Name: Laurent, Martin")
    print("Age: 44")
    print("Planet: Earth, FR")
    print("Duty: Photo/Videographer ")
    print("Status: Dead")
    time.sleep(1)
    print("............................")
    print("Name: Diaz, Juan")
    print("Age: 29")
    print("Planet: Earth, ES")
    print("Duty: Documenter")
    print("Status: Alive")
    time.sleep(4)
    print("............................")
    print("Name: Salazar, Pedro")
    print("Age: 45")
    print("Planet: Earth, PT")
    print("Duty: Captain")
    print("Status: Alive")
    time.sleep(3)
    print("............................")
    print("Name: van Beek, Johannes")
    print("Age: 36")
    print("Planet: Earth, BE")
    print("Duty: Lead Research")
    print("Status: Dead")
    time.sleep(2)
    print("............................")
    print("DOWNLOAD COMPLETE")
    print("............................")
    print("")
    time.sleep(4)
    print()
    print("The Captain is still missing...")
    time.sleep(2)
    print("I oughta find him, in order to leave this place. He should have the keycard for the shuttle.")
    time.sleep(5)
    print("Anyway...")
    time.sleep(4)
    print("This planet is far from ready for colonization... the air is toxic and the soil unarable... we know that now...")
    time.sleep(2)
    print("We haven't found any life forms around... this should be more than enough to conclude that Planet-9 is dead.")
    time.sleep(3)
    print("Looks like I arrived at my checkpoint...")

    while True:
        print("From here on, I should choose a route... The Cave or the Plateau? (go through the plateau / go inside the cave)")
        pathway = input("")
        pathway = pathway.lower()
        if pathway == "plateau" or pathway == "p" or pathway == "take the plateau" or pathway == "go to the plateau" or pathway == "go through the plateau":
            plateau()
        elif pathway == "cave" or pathway == "c" or pathway == "take the cave" or pathway == "go inside the cave" or pathway == "go through the cave":
            cave()
            

def start():
    print('"Transmission accepted"')
    print("")
    print("Hello!")
    print("Who is this? What is your name? ")
    name = str(input(""))
    time.sleep(2)
    print("Finally... Somebody! You must be the assigned Operator, from Stationary division EPSILON.")
    time.sleep(1)
    print("I have been trying to contact you guys for days.")
    time.sleep(2)
    print("Listen " + name + " ... I am the deployed documenter, Diaz... I am the sole survivour of SIGMA-02, Planet-9 - Research team.")
    time.sleep(2)
    print("Me and my crew disembarked from Mars en route to Planet-9 two months ago, our ship GAMMA crashed...")
    time.sleep(3)
    print("An SOS pick up vessel was supposed to dock a few days and pick us up... Except, it never landed...")
    print("There was another incident last week, I dont know what happened...")
    time.sleep(3)
    print("I woke up dizzy in my pod, Ernst was found dead by the dinner table with a hand written note on his hand.")
    time.sleep(3)
    print()
    print("'The path to your salvation lies in this riddle:")
    print("I am not a snake... I am not a comedy group... I am an ancient programing language used by earthlings. What am I?'")
    print()
    time.sleep(3)
    print("Anyway... The rest of team disapeared...")
    time.sleep(2)
    print("It was him who closed our Pods, before the start of his shift.")
    time.sleep(1)
    print("Crew status indicates they are dead, with the exception of the Captain...")
    time.sleep(1)
    print("Our internal hardware is damaged and I cannot salvage anything from our station...")
    print()
    print('"Connection lost..."')
    print('"Reconnecting..."')
    time.sleep(2)
    print('"Reconnecting..."')
    time.sleep(9)
    print('"Connection established"')
    print(datetime.now() + timedelta(days=101775, hours=-5))
    print()
    print(name + " are you still there? The connection is weak here... It is imperative that you help me!")
    time.sleep(2)
    print("I need to get out of here. That is why they sent you right?")
    time.sleep(1)

    while True:
        print("Can you stay online and help me? (yes / no)")
        response = input("")
        response = response.lower()
        if response == "y" or response == "yes" or response == "sure" or response == "ofcourse" or response == "definetly" or response == "i will stay online" or response == "i will help you":
            pact()
        elif response == "n" or response == "no" or response == "no way" or response == "no way jose" or response == "sorry" or response == "i can't help you" or response == "not in the mood":
            print('"Call suspended"')
            
            
print("............................................................................................")
time.sleep(2)
print(datetime.now() + timedelta(days=101775, hours=-5))
print("Final report of Research Starship 'GAMMA'.")
time.sleep(2)
print("The other members of the Crew... are dead, the Captain is missing, the cargo and ship wrecked.")
print("I should reach the Emergency shuttle in a week.")
time.sleep(1)
print("With a little luck, the operator will accept my transmission call...")
time.sleep(4)
print("This is Diaz, the last survivor of startship GAMMA... logging off.")
print("............................................................................................")
time.sleep(5)
print(" ")
print(".̪̜̳͓̟.̳͎ͅ.̩̩̰...̭̗͕.̲͙.̜͇͈.̖..̺̟̬̠̞.̹͍̙.͈͙.̲̗̗͙.͙̩͍͇.̼͓̮̺.̯͖͚̞.͙̣̳͎..̲̫̱͇.͎͓̘...̙̦͓̭͙.̝ͅ.̩.̹͓ͅ.̳͇͕.̤̹.̮̥̻.̣̤̫.̻̞̯.̗͖̦̟̮.̖.̻.͍̱ͅ...̹͚͎.̗̜̞.̰.̙̩̲͍.̫̳̮̱.̱̰͕͉..̳.͓͖͖.̗.̞̮̣̰̣.͚̭.͓̩.̞͕̼ͅ.̼̫.̠͙̪..̰̤̙̗.̰̰̳.̺̬̜̯̰.̠͕͕̠.̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫.͚̜̙.͚̦..͎̟.͇.̱̺.̰͖̖̗̠..̮..̫͚.̰ͅ.̥̜͙̫̘.̰͎͖.̹̼̞̤͈.̻̙͎.͕̗̼̺̬.̞̘...̲͈.̼̳..̦̖̣̳͈.")
print(" ")
print("                                                                                            ")
print("                                          ㄥㄖ丂ㄒ                                           ")
print("                                                                                            ")
print(" ")
print(".̫̳̮̱.̱̰͕͉..̳.͓͖͖.̗.̞̮̣̰̣.͚̭.͓̩.̞͕̼ͅ.̼̫.̠͙̪.͇.̱̺.̰͖̖̗̠..̮..̫͚.̰ͅ.̥̜͙̫̘.̰͎͖.̹̼̞̤͈.̻̙͎.͕̗̼̺̬.̞̘...̲͈.̼̳..̦̖̣̳͈..̪̜̳͓̟.̳͎ͅ.̩̩̰...̭̗͕.̲͙.̜͇͈.̖..̺̟̬̠̞.̹͍̙.͈͙.̲̗̗͙.͙̩͍͇.̼͓̮̺.̯͖͚̞.͙̣̳͎..̲̫̱͇.͎͓̘...̙̦͓̭͙.̝ͅ.̩.̹͓ͅ.̳͇͕.̤̹.̮̥̻.̣̤̫..̰̤̙̗.̰̰̳.̺̬̜̯̰.̠͕͕̠.̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫.͚̜̙.͚̦..͎̟.̻̞̯.̗͖̦̟̮.̖.̻.͍̱ͅ...̹͚͎.̗̜̞.̰.̙̩̲͍")
print(" ")
time.sleep(2)
print(" ")
print('"Incoming signal..."')
time.sleep(3)
print('"Incoming signal..."')
time.sleep(1)
print('"Incoming signal..."')
print('"Connecting..."')
time.sleep(0.3)
print("Connection established")
print(datetime.now() + timedelta(days=101775, hours=-5))
print("EPSILON Station-P3, Mars")
print()
time.sleep(2)
print("Hello?")
time.sleep(1)
print("Hello?! Anybody there?")
print("")

while True:
    print("Accept transmission? (accept / decline)") 
    startgame = input("")
    startgame = startgame.lower()
    if startgame == "yes" or startgame == "y" or startgame == "accept":
        start()
    elif startgame == "no" or startgame == "n" or startgame == "decline":
        print("Call Declined")
        gameover()
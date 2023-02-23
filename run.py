# ----------------------Built-in Modules-----------------------
from datetime import date
from datetime import datetime
from datetime import timedelta
from colorama import Fore
import time
import random
import sys

# ----------------------Typewriter function-----------------------
# This function a invokes a typewriter effect
# and determines the how fast Diaz types


def diaz(text):
    for letters in text:
        sys.stdout.write(letters)
        sys.stdout.flush()
        time.sleep(.05)
    print("")

# ----------------------------Credits-----------------------------


def credits():
    print()
    print()
    print()
    print()
    print("         THE END")
    print()
    print()
    print()
    print("LOST created by Tiago Moura, 2023")
    time.sleep(10)
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    # Invokes game over, for anothe run
    gameover()

# ---------------------------GAME OVER----------------------------
# This function is called if the player makes the wrong call
# and at the end of the Credits


def gameover():
    print()
    print('"Connection lost..."')
    time.sleep(2)
    print('"Reconnecting..."')
    print('"Failed to connect"')
    time.sleep(3)
    print()
    print(
        ".̪̜̳͓̟.̳͎ͅ.̩̩̰...̭̗͕.̲͙.̜͇͈.̖"
        "..̺̟̬̠̞.̹͍̙.͈͙.̲̗̗͙.͙̩͍͇.̼͓̮̺.̯͖͚̞.͙̣̳͎."
        ".̲̫̱͇.͎͓̘...̙̦͓̭͙.̝ͅ.̩.̹͓ͅ.̳͇͕"
        ".̤̹.̮̥̻.̣̤̫.̻̞̯.̗͖̦̟̮.̖.̻.͍̱ͅ"
        "...̹͚͎.̗̜̞.̰.̙̩̲͍.̫̳̮̱.̱̰͕͉..̳"
        ".͓͖͖.̗.̞̮̣̰̣.͚̭.͓̩.̞͕̼ͅ.̼̫.̠͙̪..̰̤̙̗"
        ".̰̰̳.̺̬̜̯̰.̠͕͕̠.̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫"
        ".͚̜̙.͚̦..͎̟.͇.̱̺.̰͖̖̗̠..̮..̫͚."
        )
    print()
    print()
    print()
    print(
        "                                  GAME "
        "OVER                                    "
        )
    print()
    print()
    print(
        ".̫̳̮̱.̱̰͕͉..̳.͓͖͖.̗.̞̮̣̰̣.͚̭.͓̩.̞͕̼ͅ"
        ".̼̫.̠͙̪.͇.̱̺.̰͖̖̗̠..̮..̫͚"
        ".̰ͅ.̥̜͙̫̘.̰͎͖.̹̼̞̤͈.̻̙͎.͕̗̼̺̬.̞̘...̲͈"
        ".̼̳..̦̖̣̳͈..̪̜̳͓̟.̳͎ͅ.̩̩̰.."
        ".̭̗͕.̲͙.̜͇͈.̖..̺̟̬̠̞.̹͍̙.͈͙.̲̗̗͙.͙̩͍͇"
        ".̼͓̮̺.̯͖͚̞.͙̣̳͎..̲̫̱͇.͎͓̘...̙̦͓̭͙.̝ͅ"
        ".̩.̹͓ͅ.̳͇͕.̤̹.̮̥̻.̣̤̫..̰̤̙̗.̰̰̳.̺̬̜̯̰"
        ".̠͕͕̠.̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫.͚̜̙.͚̦"
        )
    print()
    # This loop locks the User here, untill a correct choice is typed
    while True:
        print('"Retry (yes / no)"')
        go_continue = str(input("- "))
        print()
        print()
        if (go_continue == "yes"
            or go_continue == "y"
                or go_continue == "accept"):
            # Invokes start()
            start()
        elif (go_continue == "no"
                or go_continue == "n"
                or go_continue == "decline"):
            print('"Call Declined"')

# ---------------------------COUNTDOWN(Act16)----------------------------
# This function summons a countdown from 9 to 1, before the credits are rolled


def countdown():
    print()
    diaz("You got it!")
    time.sleep(3)
    diaz("This is it, departure.")
    time.sleep(5)
    diaz("I am ready for take off!")
    print()
    for countdown in range(9, 0, -1):
        time.sleep(1)
        print(countdown)
    print()
    # Invokes the credits()
    credits()

# ----------------------------Ignition(Act15)----------------------------
# This function presents the user with a board of numbers and letters
# which the user must press in order to proceed to the next function


def getaway():
    board = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    def display_board():
        print("? |" + " A:" + "| " + "B:" + "| " + "C:")
        print(
            "D:| " + str(board[0]) + " "
            "| " + str(board[1]) + " | " + str(board[2])
            )
        print(
            "E:| " + str(board[3]) + " "
            "| " + str(board[4]) + " | " + str(board[5])
            )
        print(
            "F:| " + str(board[6]) + " "
            "| " + str(board[7]) + " | " + str(board[8])
            )

    def playgame():
        # Invokes display_board()
        display_board()
        # And the handleposition()
        handleposition()

    def handleposition():
        # Positions the character X in the board
        position = int(input("I pressed number "))
        position = int(position)
        board[position] = "X"
        display_board()
        board[position] = "X"

        # If the User presses 7
        # the X will be marked in the give position and the countdown starts
        if position == 7:
            # Invokes countdown()
            countdown()
        # Otherwise, the User üressed the wron button and it's Game Over
        else:
            print("Failed to initiate Countdown: 'Permanent Shutdown'")
            # Invokes gameover()
            gameover()
    # Invokes playgame
    playgame()

# --------------------------Take Off(Act14)------------------------------------
# Block of Text(Narrative)


def takeoff():
    diaz("Great! So far, so good.")
    time.sleep(3)
    diaz("The systems are running...")
    time.sleep(1)
    diaz("I must input the correct number, as in this schematics.")
    time.sleep(3)
    diaz("Hang on a second, I am uploading the data to you...")
    time.sleep(4)
    diaz("We should have only one try... before permanent system shutdown.")
    diaz("Don't mess this up.")
    time.sleep(2)
    diaz("Have you seen anything like it? Which one is the execution number?")
    print()
    getaway()

# -----------------------------Puzzle(Act13)---------------------------------
# This function calls the user to introduce letters
# to find a secrete word, similar to Hangman


def puzzle():
    password = "python"
    attempts = 0
    chances = 3
    log = ["*"]*len(password)

    print("--------| " + str(attempts) + " | " + str(chances) + " |--------")
    print(str(log).replace(',', ''))
    print("-------------------------")

    # While the User Attempts are below and not equal to the Chances
    # the deciphered word(joined list after the input) is looped through
    while attempts < chances and "".join(log) != password:
        character = input("Input a character: ")
        # If the input of the User is in the Password, defined by Length
        # spoil the letter in the Log
        if character in password:
            for i in range(len(password)):
                if character == password[i]:
                    log[i] = character
        else:
            print()
            # Incrememts Attempts by 1
            attempts += 1

        print(
            "--------|" + str(attempts) + " "
            "| " + str(chances) + " |--------"
            )
        print(str(log).replace(',', ''))
        print("-------------------------")

    # if the number of Attemps reaches the number of Chances it's Game Over
    if attempts == chances:
        print()
        print('"Access denied"')
        print(
            "- The shuttle has been locked. "
            "Diaz must live his remaining days in Planet-9 alone -")
        # invokes gameover()
        gameover()
    # else the user will be sent to the next stage
    else:
        print('"Access granted. Systems online"')
        print()
        time.sleep(2)
        diaz("Bingo!, you unlocked it! ")
        # invokes the next act
        takeoff()

# --------------------------Shuttle(Act12)------------------------------


def shuttle():
    diaz("Here I am, I found the Emergency shuttle.")
    diaz(
        "Ernst made it here, before he went back to base. "
        "I can see his workers tag."
    )
    time.sleep(1)
    diaz("I imagine he didn't have the card with him, so he had to go back.")
    time.sleep(2)
    diaz("The keycard worked.... The power cells are in place.")
    time.sleep(1)
    diaz("I just need to power up the ignition panels.")
    time.sleep(5)
    diaz("The power is on!")
    time.sleep(2)
    diaz(
        "A log in is requiered to access the systems, "
        "the characters should be introduced one by one...")
    time.sleep(2)
    diaz("Ernst must have locked it before he double tagged. Any clues?")
    print()
    # invokes puzzle()
    puzzle()

# --------------------------Rock Paper Scissors(Act11)-------------------------
# Rock, Paper, Scissors function against the AI of Captain.
# The first to reach the score of 3 wins


def negotiation():
    captainscore = 0
    diazscore = 0
    # This loop locks the User here, untill a correct choice is typed.
    while True:
        hands = ["Rock", "Paper", "Scissors"]
        captain = random.choice(hands)
        print()
        diaz = input("Which hand should I play? ").capitalize()
        # if the User reaches 2
        # (incrememt starting from 0, ergo 3 rounds) the User wins
        if diazscore == 2:
            print("I beat him, fair and square!!!...")
            time.sleep(3)
            print("Does this mean...")
            time.sleep(2)
            print(
                "I refused to accept his gun... "
                "He kept his word and let me go.")
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
        # Otherwise, if the captain makes it first to the 3 rounds
        # Captain wins and it's Game over for the user
        elif captainscore == 2:
            print("- Captain Salazar won the game and took Diaz life -")
            # Invokes gameover()
            gameover()
            break

        # If Diaz & Capatin draw the same hands it's a draw
        if diaz == captain:
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I tied against the Captain, we have to go again.")
        # Otherwise, Diaz(Rock) beats Captain(Scissors)
        # and the score is incremeted by 1
        elif diaz == "Rock" and captain == "Scissors":
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I won this round against the Captain!")
            diazscore += 1
        # Otherwise, Diaz(Paper) beats Captain(Rock)
        # and the score is incremeted by 1
        elif diaz == "Paper" and captain == "Rock":
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I beat him this round!")
            diazscore += 1
        # Otherwise, Diaz(Scissors) beats Captain(Paper)
        # and the score is incremeted by 1
        elif diaz == "Scissors" and captain == "Paper":
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("The Captain lost this round!")
            diazscore += 1
        # Otherwise, when all statements above are false
        # Captain wins and his score is incremented by 1
        else:
            print("Captain: ", captain)
            print("Diaz: ", diaz)
            print()
            print("I lost!")
            captainscore += 1


# --------------------------Pits(Act7alt)------------------------------
# Block of Text(Narrative)
def pitsalt():
    time.sleep(4)
    diaz("I made my way to the pits.")
    time.sleep(2)
    diaz("It's very windy here...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(2)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(4)
    diaz("It should take a while to find a safe zone...")
    time.sleep(3)
    diaz("There is something moving in the distance... someone...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(3)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(6)
    diaz("This conection... Don't die on me now...")
    time.sleep(2)
    diaz("Someone is coming this way...")
    time.sleep(3)
    diaz("Is that the Captain?")
    time.sleep(2)
    diaz("He looks very ill... I should go up to him at once.")
    time.sleep(15)
    diaz("The Captain is out of his head...")
    time.sleep(2)
    diaz("Wait! He has a gun... and is demanding the keycard from me.")
    time.sleep(1)
    diaz("There is only one passenger seat in that emergency shuttle...")
    time.sleep(2)
    diaz("He insists the shuttle is his ticket home...")
    time.sleep(5)
    diaz("The egoistic bastard... he is also infected...")
    diaz("He is as good as dead... there is no cure for what he has.")
    time.sleep(1)
    diaz(
        "What should I do? He sees a dilemma on his hands too, "
        "and would hate to kill me for the card...")
    time.sleep(4)
    diaz("We agreed on a stand off, of 'Rock Paper Scissors'...")
    time.sleep(2)
    diaz("Never in my life would I bet my life this way...")
    diaz(
        "Careful not to to play around... best out of 3... "
        "the Captain is not fooling..."
        )
    time.sleep(2)
    # Invokes negotiation()
    negotiation()

# --------------------------Leap(Act10)------------------------------
# Block of Text(Narrative)


def finaldeed():
    # This loop locks the User here, untill a correct choice is typed
    while True:
        diaz("What do you think I should do?")
        print("(kill him and take the keycard / trade the gun for the key)")
        decisionmaker = input("- ")
        decisionmaker = decisionmaker.lower()
        if (decisionmaker == "trade"
            or decisionmaker == "give"
            or decisionmaker == "give him the gun"
                or decisionmaker == "trade the gun for the card"):
            diaz(
                "You better know what I am doing... "
                "I will give him my gun for the keycard..."
                )
            time.sleep(2)
            diaz("He thanked me... seemed desperate to have it...")
            time.sleep(3)
            diaz(
                "I don't know what he will do with that gun... "
                "There was only one bullet left..."
                )
            time.sleep(2)
            diaz(
                "But he repeatedly said 'F + B' "
                "I fail to comprehend what he meant..."
                )
            time.sleep(4)
            diaz("Lets get a move on. The shuttle is just ahead!")
            time.sleep(5)
            print(" ")
            print('"Connection lost..."')
            time.sleep(1)
            print('"Reconnecting..."')
            time.sleep(2)
            print('"Reconnecting..."')
            print('"Connection established"')
            print(" ")
            diaz("I just heard a gunshot behind the pits... Captain?")
            time.sleep(2)
            diaz("Oh... I see now...")
            time.sleep(4)
            diaz("The shuttle is just ahead.")
            time.sleep(5)
            # Invokes shuttle()
            shuttle()

        elif (decisionmaker == "shoot"
                or decisionmaker == "shoot him dead"
                or decisionmaker == "kill"
                or decisionmaker == "kill him"):
            diaz("It's the last bullet... I better know what I am doing...")
            time.sleep(1)
            diaz(
                "I wonder if putting him out of his misery "
                "is the correct thing to do."
                )
            time.sleep(2)
            diaz(
                "Will this make me a murderer? "
                "I guess there is no other way. Everyone for himself, right?"
                )
            time.sleep(7)
            diaz("I killed him...")
            time.sleep(3)
            diaz(
                "This is on both of us. "
                "My actions are a reflection of your decisions."
                )
            time.sleep(5)
            diaz(
                "Let's get the keycard and never look back... "
                "he has something written on his forearm."
                )
            time.sleep(2)
            diaz('It says "F + B"')
            time.sleep(3)
            diaz("I should keep going... The shuttle is just ahead...")
            time.sleep(5)
        # Invokes shuttle()
        shuttle()

# --------------------------Judgement(Act9)------------------------------
# Block of Text(Narrative)


def settlement():
    takeaction = input("- ")
    takeaction = takeaction.lower()
    # The user either chooses this path
    if (takeaction == "threaten"
        or takeaction == "threaten him"
        or takeaction == "threat"
            or takeaction == "point the gun at him"):
        diaz("I'll insist...")
        time.sleep(2)
        diaz("I pointed the gun at him!")
        time.sleep(6)
        diaz("Is he nuts? He made a proposal.")
        diaz("The keycard of the shuttle in exchange for my gun...")
        time.sleep(4)
        diaz(
            "If I give up the gun, he will kill me and take the shuttle... "
            "nonsense..."
            )
        time.sleep(2)
        diaz("I could just kill him and take the keycard for myself")
        diaz("But... I am not a murderer...")
        time.sleep(1)
        diaz("You are my guide here...")
        time.sleep(1)
        # Invokes finaldeed()
        finaldeed()

# --------------------------Killer(Act8)------------------------------
    # Otherwise the User takes this path
    elif (takeaction == "shoot"
            or takeaction == "shoot him dead"
            or takeaction == "kill"
            or takeaction == "kill him"):
        diaz("It's the last bullet... I better know what I am doing...")
        diaz(
            "I wonder if putting him out of his misery "
            "is the correct thing to do."
            )
        time.sleep(2)
        diaz(
            "Will this make me a murderer? "
            "I guess there is no other way. Everyone for himself."
            )
        time.sleep(7)
        diaz("I killed him...")
        time.sleep(3)
        diaz(
            "This is on both of us. "
            "My actions are a reflection of your decisions."
            )
        time.sleep(5)
        diaz(
            "Let's get the keycard and never look back... "
            "he has something written on his forearm..."
            )
        time.sleep(2)
        diaz('It says "F + B"')
        time.sleep(2)
        diaz("I should keep going... The shuttle is just ahead...")
        time.sleep(4)
        # Invokes shuttle()
        shuttle()

# --------------------------Pits(Act7)------------------------------
# Block of Text(Narrative)


def pits():
    diaz("I made my way to the pits...")
    time.sleep(2)
    diaz("It's very windy here...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(2)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(4)
    diaz("It should take a while to find a safe zone...")
    time.sleep(5)
    diaz("Hold on...")
    time.sleep(3)
    diaz("There is something moving in the distance... someone...")
    print(" ")
    print('"Connection lost..."')
    time.sleep(1)
    print('"Reconnecting..."')
    time.sleep(3)
    print('"Reconnecting..."')
    print('"Connection established"')
    print(" ")
    time.sleep(6)
    diaz("Don't die on me now.")
    time.sleep(2)
    diaz("Someone is coming this way...")
    time.sleep(3)
    diaz("Is that the Captain?")
    time.sleep(2)
    diaz(
        "Great, he should have the keycard, so... "
        "perhaps no need to bypass the ignition panels."
        )
    time.sleep(4)
    diaz("He looks very ill... I'll get back to you once I speak with him.")
    time.sleep(15)
    diaz("The Captain is out of his head...")
    time.sleep(1)
    diaz(
        "There is only one passenger seat in that emergency shuttle... "
        "and he has the card."
        )
    time.sleep(2)
    diaz(
        "He insists the shuttle is his ticket home "
        "and everyone for himself..."
        )
    time.sleep(5)
    diaz("I understand his point of view...")
    diaz("But... should I stand ground and submit to his demands???")
    time.sleep(2)
    diaz("The egoistic bastard... he is also infected...")
    diaz("He is as good as dead... there is no cure for what he has.")
    time.sleep(1)
    diaz("How should I confront him? (threaten him/shoot him dead)")
    time.sleep(3)
    # Invokes settlement()
    settlement()


# --------------------------Keycard(Act5b)------------------------------
# This function allows the user to answer the question
# which one must answer correctly within 2 chances, else gameover() is called.
# Function that prompts User to type in the correct answer, else it's Game Over
def keycard():
    password = "virgo"
    guess = ""
    countguess = 0
    maxguess = 2
    outofguess = False
    # This loop locks the User here, untill a correct answer is typed
    # while the correct guess is not the same as password
    # the outofguesses remains false
    # and the guess count is incremented by 1, otherwise it's true
    while guess != password and not (outofguess):
        if countguess < maxguess:
            guess = input("Password: ")
            guess = guess.lower()
            countguess = countguess + 1
        else:
            outofguess = True

    if outofguess:
        print("- The kit self desctructed and gave a fatal blast to Diaz -")
        # Invokes gameover()
        gameover()
    else:
        diaz('"The keycard has been been disarmed"')
        print("")
        diaz("This should ignite the shuttle.")
        time.sleep(2)
        diaz("I'll walk a little further...")
        time.sleep(4)
        diaz("This is beautiful, never seen a planet with two suns.")
        time.sleep(3)
        diaz("The view is rather spectacular, but very hot up here,.")
        diaz(
            "No wonder there is no nightime in this planet... "
            "I can see the stars though."
            )
        time.sleep(2)
        diaz(
            "I can see the pits from up here. "
            "I'll get back to you once I get more updates."
            )
        time.sleep(6)
        # Invokes pitsalt()
        pitsalt()

# --------------------------Plateau(Act4b)------------------------------
# Block of Text(Narrative)


def plateau():
    diaz(
        "It's a long walk and very hot in the open. "
        "I should get back to you in a minute."
        )
    time.sleep(20)
    diaz("Great, I am back. Good to know you waited for me...")
    diaz("I finally reached the checkpoint.")
    time.sleep(3)
    diaz(
        "Do you want to hear the good news or bad news? "
        "Well, I assume both..."
        )
    time.sleep(3)
    diaz("The good news is... I found part of my crew... Davies and Laurent.")
    time.sleep(4)
    diaz("The bad news... They are dead. But not just dead...")
    time.sleep(3)
    diaz("Their faces are full of fungus... infested by mold... an infection.")
    time.sleep(4)
    diaz(
        "They died of something extraordinary... "
        "like a sickness or some sort..."
        )
    time.sleep(2)
    diaz("Horrific...")
    time.sleep(5)
    diaz("Hold on...")
    time.sleep(3)
    diaz("I found the keycard for the shuttle by their camp.")
    diaz("This should come in handy, till we reach our next destination.")
    time.sleep(2)
    diaz(
        "It requires a password in order to unock it... "
        "Laurents pad has a note..."
        )
    time.sleep(1)
    print("It reads...")
    print(" ")
    time.sleep(5)
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    print("DOWNLOADING DATA...")
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    print(datetime.now() + timedelta(days=101773, hours=-10))
    print("'Be careful, something sinister dwells in this ecosystem.")
    print("If you see it run and don't look back.")
    print("Davies and I managed to escape, but we have been infected...")
    print(
        "I also retrieved the keycard from the scrapyard, "
        "there is also some food left..."
        )
    print("If you want to open the kit, containing the keycard...")
    print(
        "Then it should be the 6th constellation sign "
        "of the Zodiac, planet Earth."
        )
    print(
        "Careful not to mistype it else it will selfdestruct, "
        "with you included."
        )
    print("The blast can be fatal.")
    print(
        "I had to arm it, because of Van Beek, "
        "Davies and I made a detour from him..."
        )
    print("You have two tries, before it explodes.")
    print(
        "The stars, so bright... "
        "I think I will lie down here for a while...'"
        )
    print("- Martin Laurent")
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    # Invokes keycard()
    keycard()

# --------------------------Gun(Act7a)------------------------------
# Block of Text(Narrative)
# This function makes use of the random module


def risk():
    # Either "hit" or "miss", the computer draws one or another
    outcome = ["hit", "miss"]
    shot = random.choice(outcome)
    if shot == "hit":
        diaz("I shot it!!!")
        time.sleep(2)
        diaz("But, it ran off! I better make my way to the exit!")
        time.sleep(5)
        diaz("I managed to reach the exit... How I missed the sunlight...")
        time.sleep(8)
        diaz("I need to take a breath...")
        time.sleep(4)
        diaz("Whatever that thing was... it go hold of them...")
        time.sleep(1)
        diaz("I still have one bullet left...")
        time.sleep(3)
        diaz(
            "I can see the pits from down here. "
            "I'll contact you once I get to my next checkpoint."
            )
        time.sleep(15)
        # Invokes pits()
        pits()

    else:
        diaz("Damn...I missed it! No more bullets...!")
        time.sleep(1)
        diaz("I saw it in a flash. The horror...")
        time.sleep(3)
        # Invokes gameover()
        print(
            "- Something dwelling the cave got a hold of Diaz, "
            "never to be heard of him again -"
            )
        gameover()


# --------------------------Encounter(Act6a)------------------------------
# This function allows the user to make a choice within the narrative
# while the input matches one of the choices
def fightorflee():
    while True:
        caveencounter = input("- ")
        caveencounter = caveencounter.lower()
        if (caveencounter == "run"
            or caveencounter == "r"
            or caveencounter == "run away"
                or caveencounter == "run towards the exit"):
            diaz("OK... I am running, I AM RUNNING!!!")
            time.sleep(10)
            diaz("It's after me!")
            time.sleep(2)
            diaz("I made it... I made it to the exit!")
            time.sleep(3)
            diaz("I can see the pits from down here.")
            diaz("I'll contact you once I get to my next checkpoint.")
            time.sleep(10)
            # Invokes pits()
            pits()

        elif (caveencounter == "sneak"
                or caveencounter == "sneak past it"
                or caveencounter == "stealth"
                or caveencounter == "move quietly"):
            diaz("Very well... I'll move quietly...")
            time.sleep(5)
            diaz("Perhaps it won't hear me...")
            time.sleep(3)
            diaz("It's hard to see... I feel warm breathing on my neck...")
            time.sleep(0.5)
            diaz("What is this?... NO WAIT!!!")
            print(
                "- Something dwelling the cave got a hold of Diaz, "
                "never to be heard of him again -"
                )
            # Invokes gameover()
            gameover()

        elif (caveencounter == "shoot"
                or caveencounter == "shoot it"
                or caveencounter == "blast it"
                or caveencounter == "fire at will"):
            diaz("This is a shot in the dark. If I miss, I am dead...")
            time.sleep(5)
            diaz("Steady...")
            time.sleep(5)
            # Invokes risk()
            risk()

# --------------------------GunHolster(Act5a)------------------------------
# This function allows the user to answer the question
# which one must answer correctly within 3 chances, else gameover() is called.
# Function that prompts User to type in the correct answer, else it's Game Over


def gunholster():
    password = "emma"
    guess = ""
    countguess = 0
    maxguess = 3
    outofguess = False
    # This loop locks the User here, untill a correct choice is typed
    # while the correct guess is not the same as thepassword
    # the outofguesses remains false
    # and the guess count is incremented by 1, otherwise it's true
    while guess != password and not (outofguess):
        if countguess < maxguess:
            guess = input("Password: ")
            guess = guess.lower()
            countguess = countguess + 1
        else:
            outofguess = True

    # If the user is out of guesses, it's Game Over
    if outofguess:
        print(
            "- It took Diaz to long to guess the a hold of the Gun. "
            "Something got him first -"
            )
        # Invokes gameover()
        gameover()
    # Otherwise the User is sent to the next stage
    else:
        diaz('"The holster has been unlocked"')
        print("")
        diaz("I never used a gun before, but should be easy to shoot right?")
        time.sleep(4)
        diaz("Wait... something is strange...")
        time.sleep(3)
        diaz(
            "The ground is silent and the air is still... "
            "Everything is too quiet."
            )
        time.sleep(4)
        diaz(
            "I can no longer hear or feel the droplets of water "
            "falling down from the ceiling..."
            )
        time.sleep(5)
        diaz("The hissing is gone...")
        time.sleep(1)
        diaz(
            "Should I run, move quietly towards the exit "
            "or shoot my way through?"
            )
        print("(run / sneak / shoot)")
        # Invokes fightorflee()
        fightorflee()

# --------------------------Cave(Act4a)------------------------------
# Block of Text(Narrative)


def cave():
    diaz("Very well then... I shall enter the depths of this cave.")
    time.sleep(5)
    diaz("I wonder if this was a wise decision...")
    time.sleep(5)
    diaz("Can't see much... The air is cold... and the soil is wet.")
    time.sleep(2)
    diaz(
        "It echoes in here, I can hear drops of water... "
        "Could this mean life???"
        )
    time.sleep(7)
    diaz("What was that?!!...")
    time.sleep(3)
    diaz("The darkness must be playing tricks on me...")
    time.sleep(2)
    diaz("Ever felt like there is someone watching you?")
    time.sleep(6)
    diaz("Did you hear that?")
    time.sleep(2)
    diaz("There is definetly something in here... I can hear it...")
    diaz("It is hissing from afar.")
    time.sleep(4)
    diaz("Rather creepy... Can't make scence from where is coming from.")
    time.sleep(7)
    diaz(
        "Hardly any light in here, "
        "but I see an opening at the end of the tunel."
        )
    time.sleep(5)
    diaz("I am surprised the connection is still good in here....")
    time.sleep(3)
    diaz("On my way towards the exit...")
    time.sleep(1)
    diaz("Wait. What is this?...")
    time.sleep(5)
    diaz("The smell of blood... there's a metallic scent...")
    time.sleep(2)
    diaz("I found part of my crew, what happened in here???")
    time.sleep(1)
    diaz("Fujin was shot dead...Van Beek whatever happened to him...")
    diaz("He has no wounds, but has an infection all over his face.")
    time.sleep(5)
    diaz("What happened to them...")
    time.sleep(2)
    diaz("I should keep moving... But wait... I can perhaps take their gun.")
    time.sleep(3)
    diaz("It requires a password, to remove it from from Van Beeks holster...")
    time.sleep(3)
    diaz("There is a note... I am uploading it to you, right now...")
    print("")
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    print("DOWNLOADING DATA...")
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    print(datetime.now() + timedelta(days=101770, hours=-5))
    print("'Christ... This Fujin guy, is flipping out...")
    print(
        "He insists the only gun onboard belongs to him "
        "and to himself only..."
        )
    print("While my life gets to depend on him.")
    print("Who put him in charge? He doesn't let anyone near it...")
    print("The selfish bastard... When he least expects, I will grab it.")
    print("He thinks he has everything covered...")
    print("I saw him change the password for the holster...")
    print("It's the anthropologists first name.")
    print(
        "He had a crush on her since we made preparations in Mars... "
        "what an idiot..."
        )
    print(
        "Mars... Earth... Home... "
        "I haven't been there since I've been working for SIGMA-02."
        )
    print("It doesn't matter now. I need to get that gun.")
    print("I must fend myself against whatever is in this cave.' - Van Beek")
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    print("DOWNLOADING COMPLETE...")
    print(
        "----------------------------------------"
        "----------------------------------------"
        )
    time.sleep(3)
    print()
    diaz("I should have a few tries before I attract unwanted attention.")
    print()
    # Invokes gunholster()
    gunholster()


# --------------------------DATA(Act3))------------------------------
# This function defines a class for the whole crew of this narrative
def pact():
    # Class that manifests information about characters that are linked below
    class Worker:
        def __init__(self, name, age, planet, duty, status):
            self.name = name
            self.age = age
            self.planet = planet
            self.duty = duty
            self.status = status
    # Information about Workers that are called in the narrative below
    worker_1 = Worker(
        "Ernst, Klaus", 50, "Earth, "
        "CH", "Biologist", "Dead"
        )
    worker_2 = Worker(
        "Fujin", 32, "Earth, "
        "JP", "Geologist", "Dead"
        )
    worker_3 = Worker(
        "Davies, Emma", 33, "Earth, "
        "EN", "Anthropologist", "Dead"
        )
    worker_4 = Worker(
        "Laurent, Martin", 44, "Earth, "
        "FR", "Photo/Videographer", "Dead"
        )
    worker_5 = Worker(
        "Diaz, Juan", 29, "Earth, "
        "ES", "Documenter", "Alive"
        )
    worker_6 = Worker(
        "Salazar, Pedro", 45, "Earth, "
        "PT", "Captain", "Alive"
        )
    worker_7 = Worker(
        "van Beek, Johannes", 36, "Earth, "
        "BE", "Lead Research", "Dead"
        )

    time.sleep(2)
    diaz(
        "Great. Very well. "
        "I need you to help me navigate to the Emergency Shuttle."
        )
    time.sleep(1)
    diaz("It detached 24km southwest from here.")
    diaz("Should take a few hours from where I stand.")
    diaz(
        "My GPS is damaged... "
        "but you should be able to guide me through this ecosystem."
        )
    time.sleep(1)
    diaz("I am walking towards my next destination...")
    time.sleep(2)
    diaz("I'll be uploading data profiles to you in the meantime...")
    diaz("Not that it matters, this is futile information now...")
    time.sleep(3)
    print(" ")
    print("............................")
    print("DOWNLOADING DATA...")
    print("............................")
    time.sleep(1)
    # This batch of code belongs to the Class Worker
    print("Name:", worker_1.name)
    print("Age:", worker_1.age)
    print("Planet:", worker_1.planet)
    print("Duty:", worker_1.duty)
    print("Status:", worker_1.status)
    print("............................")
    time.sleep(0.5)
    print("Name:", worker_2.name)
    print("Age:", worker_2.age)
    print("Planet:", worker_2.planet)
    print("Duty:", worker_2.duty)
    print("Status:", worker_2.status)
    print("............................")
    time.sleep(2)
    print("Name:", worker_3.name)
    print("Age:", worker_3.age)
    print("Planet:", worker_3.planet)
    print("Duty:", worker_3.duty)
    print("Status:", worker_3.status)
    print("............................")
    time.sleep(1)
    print("Name:", worker_4.name)
    print("Age:", worker_4.age)
    print("Planet:", worker_4.planet)
    print("Duty:", worker_4.duty)
    print("Status:", worker_4.status)
    print("............................")
    time.sleep(1)
    print("Name:", worker_5.name)
    print("Age:", worker_5.age)
    print("Planet:", worker_5.planet)
    print("Duty:", worker_5.duty)
    print("Status:", worker_5.status)
    print("............................")
    time.sleep(0.5)
    print("Name:", worker_6.name)
    print("Age:", worker_6.age)
    print("Planet:", worker_6.planet)
    print("Duty:", worker_6.duty)
    print("Status:", worker_6.status)
    print("............................")
    time.sleep(0.5)
    print("Name:", worker_7.name)
    print("Age:", worker_7.age)
    print("Planet:", worker_7.planet)
    print("Duty:", worker_7.duty)
    print("Status:", worker_7.status)
    print("............................")
    time.sleep(2)
    print("DOWNLOAD COMPLETE")
    print("............................")
    print()
    time.sleep(4)
    diaz("The Captain is still missing...")
    time.sleep(2)
    diaz("I oughta find him, in order to leave this place.")
    diaz("He should have the keycard for the shuttle.")
    time.sleep(5)
    diaz("Anyway...")
    time.sleep(4)
    diaz("This planet is far from ready for colonization...")
    diaz("the air is toxic and the soil unarable... we know that now...")
    time.sleep(2)
    diaz("We haven't found any life forms around...")
    diaz("This should be more than enough to conclude that Planet-9 is dead.")
    time.sleep(3)
    diaz("Looks like I arrived at my checkpoint...")
    # Invoke route()
    route()

# --------------------------Choose a Path------------------------------
# This function allows the user to make a choice within the narrative


def route():
    # This loop locks the User here, untill a correct choice is typed
    while True:
        diaz(
            "From here on, I should choose a route... "
            "The Cave or the Plateau?")
        print("(go through the plateau / go inside the cave)")
        pathway = input("- ")
        pathway = pathway.lower()
        # Here the User is asked to make a choice
        # either take the route towards the Plateau
        if (pathway == "plateau"
            or pathway == "p"
            or pathway == "take the plateau"
            or pathway == "go to the plateau"
                or pathway == "go through the plateau"):
            plateau()
        # Else, go through the Cave
        elif (pathway == "cave"
                or pathway == "c"
                or pathway == "take the cave"
                or pathway == "go inside the cave"
                or pathway == "go through the cave"):
            cave()

# --------------------------Accept(Act2)------------------------------
# Block of Text(Narrative)


def start():
    print('"Transmission accepted"')
    print("")
    diaz("Hello!")
    diaz("Who is this? What is your name?")
    name = str(input("- "))
    time.sleep(2)
    diaz("Finally... Somebody!")
    diaz(
        "You must be the assigned Operator, "
        "from Stationary division EPSILON."
        )
    time.sleep(1)
    diaz("I have been trying to contact you guys for days.")
    time.sleep(2)
    diaz("Listen " + name + "... I am the deployed documenter, Diaz...")
    diaz("I am the sole survivor of SIGMA-02, Planet-9 - Research team.")
    time.sleep(2)
    diaz(
        "Me and my crew disembarked from Mars "
        "en route to Planet-9 two months ago."
        )
    diaz("Our ship GAMMA crashed...")
    time.sleep(3)
    diaz(
        "An SOS pick up vessel was supposed to dock a few days "
        "and pick us up..."
        )
    diaz("Except, it never landed...")
    time.sleep(1)
    diaz("There was another incident last week, I dont know what happened...")
    time.sleep(3)
    diaz(
        "I woke up dizzy in my pod, Ernst was found dead by the dinner table "
        "with a hand written note on his hands."
        )
    time.sleep(3)
    print()
    diaz('"The path to your salvation lies in this riddle:"')
    diaz('"I am not a snake... I am not a comedy group..."')
    diaz('"I am an ancient programing language used by earthlings."')
    diaz('"What am I?"')
    print()
    time.sleep(2)
    diaz("Whatever that means...")
    time.sleep(3)
    diaz("Anyway... The rest of team disapeared...")
    time.sleep(2)
    diaz("It was him who closed our Pods, before the start of his shift.")
    time.sleep(1)
    diaz(
        "Crew status indicates they are dead, "
        "with the exception of the Captain..."
        )
    time.sleep(1)
    diaz(
        "Our internal hardware is damaged "
        "and I cannot salvage anything from our station."
        )
    print()
    print('"Connection lost..."')
    print('"Reconnecting..."')
    time.sleep(2)
    print('"Reconnecting..."')
    time.sleep(9)
    print('"Connection established"')
    print(datetime.now() + timedelta(days=101775, hours=-5))
    print()
    diaz(
        name + " are you still there? The connection is weak here... "
        "It is imperative that you help me!"
        )
    time.sleep(2)
    diaz("I need to get out of here. That is why they sent you right?")
    time.sleep(1)

    # This loop locks the User here, untill a correct choice is typed
    while True:
        diaz("Can you stay online and help me? (yes / no)")
        response = input("- ")
        response = response.lower()
        # If the input is positive, the User is sent to the next act
        if (response == "y"
            or response == "yes"
            or response == "sure"
            or response == "ofcourse"
            or response == "definetly"
            or response == "i will stay online"
            or response == "i will help you"
                or response == "ok"):
            # Invokes pact()
            pact()
        # Otherwise it's Game Over for the User
        elif (response == "n"
                or response == "no"
                or response == "no way"
                or response == "no way jose"
                or response == "nah"
                or response == "sorry"
                or response == "i can't help you"
                or response == "not in the mood"):
            print('"Call suspended"')
            # Invokes gameover()
            gameover()

# --------------------------Intro(Act1)------------------------------
# Block of Text(Narrative)


print(
    Fore.RED + "......................................"
    "........................................."
    )
time.sleep(2)
print(datetime.now() + timedelta(days=101775, hours=-5))
diaz("Final report of Research Starship 'GAMMA'.")
time.sleep(2)
diaz("The other members of the Crew... are dead.")
diaz("The Captain is missing, the cargo and ship wrecked.")
diaz("I should reach the Emergency shuttle in a week.")
time.sleep(1)
diaz("With a little luck, the operator will accept my transmission call...")
time.sleep(4)
diaz("This is Diaz, the last survivor of startship GAMMA... logging off.")
print(
    "........................................"
    ".......................................")
time.sleep(5)
print(" ")
print(
    ".̪̜̳͓̟.̳͎ͅ.̩̩̰...̭̗͕.̲͙.̜͇͈.̖..̺̟̬̠̞"
    ".̹͍̙.͈͙.̲̗̗͙.͙̩͍͇.̼͓̮̺.̯͖͚̞.͙̣̳͎..̲̫̱͇"
    ".͎͓̘...̙̦͓̭͙.̝ͅ.̩.̹͓ͅ.̳͇͕.̤̹.̮̥̻.̣̤̫"
    ".̻̞̯.̗͖̦̟̮.̖.̻.͍̱ͅ.."
    ".̹͚͎.̗̜̞.̰.̙̩̲͍.̫̳̮̱.̱̰͕͉..̳.͓͖͖.̗.̞̮̣̰̣"
    ".͚̭.͓̩.̞͕̼ͅ.̼̫.̠͙̪..̰̤̙̗.̰̰̳.̺̬̜̯̰"
    ".̠͕͕̠.̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫.͚̜̙.͚̦"
    "..͎̟.͇.̱̺.̰͖̖̗̠..̮..̫͚."
    )
print(" ")
print(
    "                                      "
    "                                         "
    )
print(
    "                                    "
    "ㄥㄖ丂ㄒ                                    "
    )
print(
    "                                        "
    "                                       "
    )
print(" ")
print(
    ".̫̳̮̱.̱̰͕͉..̳.͓͖͖.̗.̞̮̣̰̣.͚̭.͓̩.̞͕̼ͅ"
    ".̼̫.̠͙̪.͇.̱̺.̰͖̖̗̠..̮."
    ".̫͚.̰ͅ.̥̜͙̫̘.̰͎͖.̹̼̞̤͈.̻̙͎.͕̗̼̺̬.̞̘.."
    ".̲͈.̼̳..̦̖̣̳͈..̪̜̳͓̟.̳͎ͅ.̩̩̰.."
    ".̭̗͕.̲͙.̜͇͈.̖..̺̟̬̠̞.̹͍̙.͈͙.̲̗̗͙.͙̩͍͇"
    ".̼͓̮̺.̯͖͚̞.͙̣̳͎..̲̫̱͇.͎͓̘...̙̦͓̭͙.̝ͅ"
    ".̩.̹͓ͅ.̳͇͕.̤̹.̮̥̻.̣̤̫..̰̤̙̗.̰̰̳.̺̬̜̯̰.̠͕͕̠"
    ".̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫.͚̜̙.͚̦"
    )
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
diaz("Hello?")
time.sleep(1)
diaz("Hello?! Anybody there?")
print("")

# --------------------------Play or Close the game-----------------------------
# This function makes a call for the User if one wants to play or not
while True:
    print("Accept transmission? (accept / decline)")
    startgame = input("- ")
    startgame = startgame.lower()
    # If the answer is Yes, the User moves to the next act
    if (startgame == "yes"
            or startgame == "y"
            or startgame == "accept"):
        # Invokes start()
        start()
    # Otherwise it's Game Over
    elif (startgame == "no"
            or startgame == "n"
            or startgame == "decline"):
        print("Call Declined")
        # invokes Game over
        gameover()

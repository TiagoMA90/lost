from datetime import date
from datetime import datetime
from datetime import timedelta
import time

logtime = datetime.now()

def plateau():
    print("It's a long walk, and very hot in the open. I should get back to you in a minute.")
    time.sleep(30)
    print("Great, i am back. Good to know you waited for me. I finally reached the checkpoint.")
    time.sleep(3)
    print("Do you want to hear the good news or bad news? I assume both.")
    time.sleep(3)
    print("I found part of my crew... Davies and Laurent.")
    time.sleep(4)
    print("Those are the bad news... They are dead.")
    print("The good news is, I found the a ration kit. This should suffice till we reach the shuttle.")
    time.sleep(2)
    print("It requires a password... Laurents pad has a note...")
    print("It reads...")
    print(" ")
    time.sleep(5)
    print("----------------------------------------------------------------------------------------------------")
    print("DOWNLOADING DATA...")
    print("----------------------------------------------------------------------------------------------------")
    print(datetime.now() + timedelta(days=-2, hours=-10))
    print("'Be careful, something sinister dwells in this ecosystem.'")
    print("'If you see it run and don't look back. Davies and I managed to escape, but we have been infected...")
    print("'I also retrieved the ration kit from the scrapyard, there is some food left...'")
    print("'If you want to open it, it is the 6th constellation sign of the Zodiac, planet Earth.'")
    print("'Careful not to mistype it else it will selfdestruct, with you included.")
    print("I had to arm it... You have two tries, before it explodes.'")
    print("'The stars, so bright... I think I will lie down here for a while...'")
    print("- Martin Laurent")
    print("----------------------------------------------------------------------------------------------------")
    
    rationkit()
    cave()

def rationkit():
    password = "VIRGO"
    guess = ""
    countguess = 0
    maxguess = 2
    outofguess = False

    while guess != password and not(outofguess):
        if countguess < maxguess:
            guess = input("Password: ")
            guess = guess.upper()
            countguess = countguess + 1
        else:
            outofguess = True

    if outofguess:
        print("Connection lost...")
        print("Reconnecting...")
        time.sleep(2)
        print("Reconnecting...")
        time.sleep(3)
        print("Failed to connect")
        time.sleep(3)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("GAME OVER")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    else:
        print("The ration kit has been unlocked")
        print("")
        print("This should help me on my journey.")

def fightorflee():
    caveencounter = input("")
    caveencounter = caveencounter.upper()
    if caveencounter == "RUN" or caveencounter == "run" or caveencounter == "SPRINT" or caveencounter == "RUN TOWARDS THE EXIT":
        print("OK... I am running, I AM RUNNING!!!")
    elif caveencounter == "SNEAK" or caveencounter == "CRAWL" or caveencounter == "STEALTH" or caveencounter == "MOVE QUIETLY":
        print("Very well... I'll move quietly...")
        print("Perhaps it won't hear me...")
        print("It's hrd to see... I feel breathing on my neck...")
        print("What is this?... NO WAIT!!!")
        print("GAME OVER make a function here")
    else:
        print("This is a shot in the dark. If I miss I am dead...")
        print("I saw it, the flash. The horror!")
        print("GAME OVER make a function here")



def cave():
    print("Very well then... I shall enter the the depths of this cave")
    time.sleep(5)
    print("There is something here. I can hear it... it is issing from affar.")
    time.sleep(4)
    print("Rather creepy? Can't make scence from where is coming from.")
    time.sleep(6)
    print("Hardly any light in here, but I see an opening at the end of the tunel.")
    time.sleep(3)
    print("I am surprised the connection is good in here....")
    time.sleep(3)
    print("On my way towards the exit...")
    print("Wait. What is this?...")
    time.sleep(5)
    print("The smell of blood... the metalic scent...")
    time.sleep(2)
    print("I found part of my crew, what happened in here? Fujin was shot dead...Van Beek whatever happened to him, he has no wounds.")
    time.sleep(5)
    print("What happened to them... I don't want to happen to me.")
    print("I should keep moving... But wait, I can perhaps take their gun.")
    time.sleep(3)
    print("It requires a password though... to remove it, from Van Beeks holster...")
    print("There is a note... I a uploading to you...")  
    print("")
    print("----------------------------------------------------------------------------------------------------")
    print("DOWNLOADING DATA...")
    print("----------------------------------------------------------------------------------------------------")
    print(datetime.now() + timedelta(days=-5, hours=-5))
    print("'This Fujin guy, is flipping out. He insists the only gun onboard belongs to him and to himself only... while my life gets to depend on him.'")
    print("'Who put him in charge? He doesn't let anyone near it... The selfish bastard... When he least exects, I will grab it.'")
    print("'He thinks he has everything covered... I saw him changing the password for the holster, it is the anthropolists first name...'")
    print("'He had a crush on her since we made preparations in Mars...'")
    print("'Mars... Earth... Home... I haven't been there since I've been working for SIGMA-02.'")
    print("'It doesn't matter now. I need to get that gun. I must fend myself against whatever is in this cave.' - Van Beek")
    print("----------------------------------------------------------------------------------------------------")
    print("I should have a few tries before I attract unwanted attention.")

    gunholster()

def gunholster():
    password = "EMMA"
    guess = ""
    countguess = 0
    maxguess = 3
    outofguess = False

    while guess != password and not(outofguess):
        if countguess < maxguess:
            guess = input("Password: ")
            guess = guess.upper()
            countguess = countguess + 1
        else:
            outofguess = True

    if outofguess:
        print("Oh no!... No WAIT!")
        print("Connection lost...")
        time.sleep(2)
        print("Reconnecting...")
        print("Failed to connect")
        time.sleep(3)
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("GAME OVER make a function here")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
    else:
        print("The holster has been unlocked")
        print("")
        print("Never used a gun before, but should be easy to shoot right?")
        time.sleep(2)
        print("Wait... something is strange. There is no sound... Everything is too quiet.")
        time.sleep(4)
        print("I can no longer hear or feel the droplets of water falling down from the ceiling...")
        time.sleep(5)
        print("The issing is gone... and... no screeching at all.")
        time.sleep(1)
        print("Should I run or quietly move towards the exit? (Run/Sneak/Shoot)")
        fightorflee()


def pact():
    time.sleep(2)
    print("Great. Very well. I need you to help me navigate to the emergency Shuttle.")
    time.sleep(1)
    print("It detached 24km southwest from here, should take a few hours from where I stand.")
    print("My GPS is damaged..., but you should be able to guide me through this ecosystem.")
    time.sleep(1)
    print("I am walking towards my next destination...")
    time.sleep(2)
    print("I'll be uploading data profiles to you...")
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
    print("I should find him, in order to leave this place.")
    time.sleep(5)
    print("Looks like I arrived at my checkpoint...")
    print("From here on, I should choose a route... The Cave or th Plateau? (Plateau / Cave)")
    act_one = input("")
    act_one = act_one.upper()
    if act_one == "PLATEAU" or act_one == "P" or act_one == "TAKE THE PLATEAU" or act_one == "GO TO THE PLATEAU":
            plateau()
    elif act_one == "CAVE" or act_one == "TAKE THE CAVE" or act_one == "GO INSIDE THE GAVE" or act_one == "GO THROUGH THE CAVE":
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
    print(f"Listen " + name + " ... I am the deployed documenter, Diaz... I am the sole survivour of SIGMA-02, Planet-9 - Research team.")
    time.sleep(2)
    print("Me and my crew disembarked from Mars en route to Planet-9 two months ago, our ship GAMMA crashed...")
    time.sleep(3)
    print("An SOS pick up vessel was supposed to dock a few days and pick us up... Except, it never landed...")
    print("There was another incident last week, I dont know what happened...")
    time.sleep(3)
    print("I woke up dizzy in my pod, Ernst was found dead by the dinner table and the rest of team disapeared...")
    print("It was him who closed our Pods, before he started his shift.")
    print("Crew status indicates they are dead, with the exception of the Captain...")
    time.sleep(1)
    print("Our internal hardware is damaged and I cannot salvage anything from our station...")
    print()
    
    print("Connection lost...")
    print("Reconnecting...")
    time.sleep(2)
    print("Reconnecting...")
    time.sleep(9)
    print("Connection established")
    print(logtime)
    print()
    
    print("Are you still here? The connection is weak here... It is imperative that you help me!")
    time.sleep(2)
    print("I need to get out of here. That is why they sent you right?")
    time.sleep(1)
    print("Can you stay online and help me? (Yes / No)")
    act_one = input("")
    act_one = act_one.upper()
    if act_one == "Y" or act_one == "YES" or act_one == "SURE" or act_one == "OFCOURSE" or act_one == "DEFINETLY":
            pact()
    elif act_one == "N" or act_one == "NO" or act_one == "NO WAY" or act_one == "SORRY" or act_one == "CAN'T HELP YOU":
            print("Call suspended")
            
            
print("............................................................................................")
time.sleep(2)
print(datetime.now() + timedelta(days=5, hours=-5))
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
print("                                      ㄥㄖ丂ㄒ                                               ")
print("                                                                                            ")
print(" ")
print(".̫̳̮̱.̱̰͕͉..̳.͓͖͖.̗.̞̮̣̰̣.͚̭.͓̩.̞͕̼ͅ.̼̫.̠͙̪.͇.̱̺.̰͖̖̗̠..̮..̫͚.̰ͅ.̥̜͙̫̘.̰͎͖.̹̼̞̤͈.̻̙͎.͕̗̼̺̬.̞̘...̲͈.̼̳..̦̖̣̳͈..̪̜̳͓̟.̳͎ͅ.̩̩̰...̭̗͕.̲͙.̜͇͈.̖..̺̟̬̠̞.̹͍̙.͈͙.̲̗̗͙.͙̩͍͇.̼͓̮̺.̯͖͚̞.͙̣̳͎..̲̫̱͇.͎͓̘...̙̦͓̭͙.̝ͅ.̩.̹͓ͅ.̳͇͕.̤̹.̮̥̻.̣̤̫..̰̤̙̗.̰̰̳.̺̬̜̯̰.̠͕͕̠.̠̭͖.͓͉̮̹.͔͕̮..̪.̤̯̘̭.͎̣̮.̫̯̫.͚̜̙.͚̦..͎̟.̻̞̯.̗͖̦̟̮.̖.̻.͍̱ͅ...̹͚͎.̗̜̞.̰.̙̩̲͍")
print(" ")
time.sleep(2)
print(" ")
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

print("Accept transmission? (Accept/Decline)") 
startgame = input("")
startgame = startgame.upper()
if startgame == "YES" or startgame == "Y" or startgame == "ACCEPT":
    start()
elif startgame == "NO" or startgame == "N" or startgame == "DECLINE":
    print("Call Declined")
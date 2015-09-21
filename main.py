"""
    Author: David Thong Nguyen
    Date Created: Nov 14th, 2013


Date Modified: Nov 17th, 2013
    - changed command infinite loop into "try,except"
    - imported sys
    --> Commands work fine for now

NEXT OBJECTIVES:
    + fixing commands so there will be no error looping (done)
    + fixing attribute distribution (done)
Date Modified: Nov 18th, 2013
    - added complete structures for leveling up
    - fixed looping correctly upon declining to close window
    - tested fights between 2 characters

NEXT OBJECTIVES:
    + add timer between fighting turns
Date Modified: Dec 7th, 2013
    - changed name of file to main.py

NEXT OBJECTIVES:
    + add timer between fighting turns    
"""

import sys
import random
import createChar
import createMobs
import fightMechanics

print("Welcome to Planet Chaoz!\n")


#############
# INTERFACE #
#############

def pageBreak():
    print("\n=============================================================================")

def PROMPT():
    return "> "

def printList(lst):
    result = "["
    for x in range(0,len(lst)):
        if x < len(lst)-1:
            result += lst[x].name + ", "
        else:
            result += lst[x].name + "]"
    print(result)



#####################
# CLASS INFORMATION #
#####################

def displayClssInfoFighter():
    for line in open("clssInfoFighter.txt"):
        line = line.strip()
        print(line)
    expChar = createChar.mkFighter("Example Fighter")
    createChar.displayExampleCharInfo(expChar)
    del expChar

def displayClssInfoGuardian():
    for line in open("clssInfoGuardian.txt"):
        line = line.strip()
        print(line)
    expChar = createChar.mkGuardian("Example Guardian")
    createChar.displayExampleCharInfo(expChar)
    del expChar

def displayClssInfoRogue():
    for line in open("clssInfoRogue.txt"):
        line = line.strip()
        print(line)
    expChar = createChar.mkRogue("Example Rogue")
    createChar.displayExampleCharInfo(expChar)
    del expChar

def displayClssInfoRanger():
    for line in open("clssInfoRanger.txt"):
        line = line.strip()
        print(line)
    expChar = createChar.mkRanger("Example Ranger")
    createChar.displayExampleCharInfo(expChar)
    del expChar

def displayClssInfoMage():
    for line in open("clssInfoMage.txt"):
        line = line.strip()
        print(line)
    expChar = createChar.mkMage("Example Mage")
    createChar.displayExampleCharInfo(expChar)
    del expChar
    
def displayClssInfoHealer():
    for line in open("clssInfoHealer.txt"):
        line = line.strip()
        print(line)
    expChar = createChar.mkHealer("Example Healer")
    createChar.displayExampleCharInfo(expChar)
    del expChar

CMDSclss = {"1" : displayClssInfoFighter,
            "2" : displayClssInfoGuardian,
            "3" : displayClssInfoRogue,
            "4" : displayClssInfoRanger,
            "5" : displayClssInfoMage,
            "6" : displayClssInfoHealer}

def clssInfo(playerList,playerListTable):
    while sys.stdin:
        try:
            print("\nChoose class to display information:\n(Enter the corresponding number")
            print("1. Fighter")
            print("2. Guardian")
            print("3. Rogue")
            print("4. Ranger")
            print("5. Mage")
            print("6. Healer")
            print("0. Return to Main Menu")
            cmd = input(PROMPT())
            print()
			
            if cmd == "0":
                pageBreak()
                return
            elif cmd in CMDSclss:
                CMDSclss[cmd]()
				
                input("\nPress ENTER to choose again...")
            else:
                print("\nWrong input!")
                input("\nPress ENTER to choose again...")
        except:
            break
    


######################
# CHARACTER CREATION #
######################

CMDSNofPlayers = {"1":None,
                  "2":None,
                  "3":None,
                  "4":None}

def getNofPlayers():
    while sys.stdin:
        try:
            number_of_players = input("How many players are there? (1-4, integer only): ")
            if number_of_players in CMDSNofPlayers:
                number_of_players = int(number_of_players)
                return number_of_players
            else:
                number_of_players = 0
                print("\nPlease enter a value from 1 to 4\n")
        except:
            break
    
CMDScreateChar = {"1" : "Fighter",
                  "2" : "Guardian",
                  "3" : "Rogue",
                  "4" : "Ranger",
                  "5" : "Mage",
                  "6" : "Healer"}

def charCreate(playerList,playerListTable):
    print("\nCHARACTER CREATION:")
    NofPlayers = getNofPlayers()
    while sys.stdin:
        try:
            for x in range(1,int(NofPlayers+1)):
                print("\nPlayer #",x,"!",sep="")
                charName = input("Enter your character's name: ")
                print("Select your class:")
                print("1. Fighter")
                print("2. Guardian")
                print("3. Rogue")
                print("4. Ranger")
                print("5. Mage")
                print("6. Healer")
                print("0. Return to Main Menu")
                charClssInput = input(PROMPT())
                try:
                    if charClssInput in CMDScreateChar:
                        playerListTable[x] = charName
                        newChar = createChar.makeCharacter(charName,\
                                                           CMDScreateChar[charClssInput])
                        playerList.append(newChar)
                        print("Current players are:",playerListTable)
                    elif charClassInput == "0":
                        # return to main menu
                        pass
                    else:
                        print("Wrong input!")
                except:
                    break
            return playerList, playListTable
        except:
            break


    
###############
# LEVELING UP #
###############

def STRup(char):
    char.STR += 1
def INTup(char):
    char.INT += 1
def ENDup(char):
    char.END += 1
def AGIup(char):
    char.AGI += 1

""" Better define each of STR, INT, END, and AGI and not leave them as strings"""
CMDSattr = {"1" : STRup,
            "2" : INTup,
            "3" : ENDup,
            "4" : AGIup}

def levelUp(char):
    char.level += 1
    char.attrPts += 10
    print(char.name,"leveled up!")
    input("Press ENTER to continue...")


def attrDistribution(char):
    print("Choose the attribute you would like to increase:")
    while sys.stdin:
        try:
            while char.attrPts > 0:
                print("(Remaining points:",char.attrPts,")")
                print("1. STR")
                print("2. INT")
                print("3. END")
                print("4. AGI")
                cmd = input(PROMPT())
                if cmd in CMDSattr:
                    CMDSattr[cmd](char)
                    char.attrPts -= 1
                    createChar.statsConvert(char)
                else:
                    print("Wrong input!")
                if char.attrPts == 0:
                    return
        except:
            break
    


##########
# FIGHTS #
##########

def enemySpawn(playerList,enemyList):
    """
    Testing to create goblins
    for x in range(random.randint(1,4)):
        goblin = createMobs.mkGoblin()
        enemyList.append(goblin)
    """
    Jeremy = createChar.mkFighter("Jeremy")
    enemyList.append(Jeremy)
    print(playerList[0].name,"encounters",\
              enemyList[0].name,", aaaaand they clash.")


def battle(playerList,enemyList):
    if playerList[0].SPD >= enemyList[0].SPD:
        faster = playerList[0]
        slower = enemyList[0]
    else:
        faster = enemyList[0]
        slower = playerList[0]
        
    while faster.HP > 0 and slower.HP > 0:
        fightMechanics.normalHit(faster,slower)
        if slower.HP <= 0:
            print(slower.name,"fainted.")
            break
        else:
            print(slower.name," has ",slower.HP,\
                  " health points left.",sep="")
        fightMechanics.normalHit(slower,faster)
        if faster.HP <= 0:
            print(faster.name,"fainted.")
            break
        else:
            print(faster.name," has ",faster.HP,\
                  " health points left.",sep="")
    input("Press ENTER to continue...")
	


###################
# MAJOR FUNCTIONS #
###################

def init():
    global playerList, playerListTable, enemyList
    playerList = []
    playerListTable = {}
    enemyList = []

CMDSStartMenu = {"1" : charCreate,
                "2" : clssInfo}

def startMenu():
    while sys.stdin:
        try:
            print("MAIN MENU: ")
            print("Enter 1 for Character Creation")
            print("Enter 2 for Class Information")
            print("Enter 0 to exit game")
            cmd = input(PROMPT())
            if cmd in CMDSStartMenu:
                CMDSStartMenu[cmd](playerList,playerListTable)
                if cmd == "1":
                    return playerList, playerListTable
            elif cmd == "0":
                input("Goodbye!")
                exit()
                return
            else:
                print("\nWrong input!")
                pageBreak()
        except:
            break


def gameStarted():
    printList(playerList)
    print("facing")
    printList(enemyList)
    print()
    input("Press ENTER to continue...")

    battle(playerList,enemyList)
    



#############
# EXECUTION #
#############

init()
startMenu()
if playerList != []:
    print()
    enemySpawn(playerList,enemyList)
    gameStarted()


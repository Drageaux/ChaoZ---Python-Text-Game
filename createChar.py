"""
    Author: David Thong Nguyen
    Date Created: Nov 14th, 2013

Date Modified: Nov 17th, 2013
    - lowered sum of basic stats to 200
    - balanced Guardian and Fighter's stats
    - changed MP conversion
    - added a statsConvert() function to conform all char
    - CRITDMG base is x1.5 (too high?)
    --> Everything is quite balanced
    
    + 2ndary stat = (3*dominant_primary + 1*lesser_primary) / 4
              or = primary stat
    - increased CRITRATE every primary stat
    - updated Wikia


NEXT OBJECTIVES:
    + leveling up (add primary while also adding 2ndary) (done, in mainMenu)
Date Modified: Nov 18th, 2013
    - see main file
"""

import math
import decimal

##############################
# CLASS INSTANCES AND MAKERS #
##############################

### TEMPLATE ###
class Character():
    __slots__ = ("name","startClss","currClss","level","attrPts",\
                 "HP","MP","STR","INT","END","AGI",\
                 "PATK","PDEF","MATK","MDEF",\
                 "SPD","ACC","EVA","CRITRATE","CRITRES","CRITDMG",\
                 "AD","AS")


### SECONDARY STATS CONVERTER ###
def statsConvert(char):
    char.HP = int(round((((char.STR * 1) + (char.END * 3)) / 2),0))
    char.MP = int(round((char.INT * 2),0))
    char.PATK = int(round((((char.STR * 3) + (char.AGI * 1)) / 4),0))
    char.PDEF = int(round((((char.STR * 1) + (char.END * 3)) / 4),0))
    char.MATK = int(round((char.INT),0))
    char.MDEF = int(round((((char.INT * 1) + (char.END * 3)) / 4),0))
    char.SPD = int(round(char.AGI,0))
    char.ACC = int(round((((char.STR * 1) + (char.AGI * 3)) / 4),0))
    char.EVA = int(round((((char.END * 1) + (char.AGI * 3)) / 4),0))
    char.CRITRATE = round(((char.STR * 0.1) + (char.AGI * 0.25)),2)
    char.CRITRES = round(((char.END * 0.25) + (char.AGI * 0.1)),2)
    char.CRITDMG = round((round(((char.STR * 0.2) + (char.AGI * 0.1)),2)/100) + 1.5,2)
    char.AD = int(round((((char.STR * 3) + (char.INT * 4) + (char.AGI * 1)) / 4),0))
    char.AS = int(round((((char.INT * 4) + (char.END * 4)) / 4),0))


### FIGHTER ###
def mkFighter(name):
    newChar = Character()
    newChar.name = str(name)
    newChar.startClss = "Fighter"
    newChar.currClss = "Fighter"
    newChar.level = 1
    newChar.attrPts = 0
    newChar.STR = 70
    newChar.INT = 35
    newChar.END = 45
    newChar.AGI = 50
    statsConvert(newChar)
    return newChar


### GUARDIAN ###
def mkGuardian(name):
    newChar = Character()
    newChar.name = str(name)
    newChar.startClss = "Guardian"
    newChar.currClss = "Guardian"
    newChar.level = 1
    newChar.attrPts = 0
    newChar.STR = 50
    newChar.INT = 40
    newChar.END = 70
    newChar.AGI = 40
    statsConvert(newChar)
    return newChar


### ROGUE ###
def mkRogue(name):
    newChar = Character()
    newChar.name = str(name)
    newChar.startClss = "Rogue"
    newChar.currClss = "Rogue"
    newChar.level = 1
    newChar.attrPts = 0
    newChar.STR = 45
    newChar.INT = 45
    newChar.END = 40
    newChar.AGI = 70
    statsConvert(newChar)
    return newChar


### ARCHER ###
def mkRanger(name):
    newChar = Character()
    newChar.name = str(name)
    newChar.startClss = "Ranger"
    newChar.currClss = "Ranger"
    newChar.level = 1
    newChar.attrPts = 0
    newChar.STR = 55
    newChar.INT = 50
    newChar.END = 30
    newChar.AGI = 65
    statsConvert(newChar)
    return newChar


### MAGE ###
def mkMage(name):
    newChar = Character()
    newChar.name = str(name)
    newChar.startClss = "Mage"
    newChar.currClss = "Mage"
    newChar.level = 1
    newChar.attrPts = 0
    newChar.STR = 35
    newChar.INT = 70
    newChar.END = 35
    newChar.AGI = 60
    statsConvert(newChar)
    return newChar


### HEALER ###
def mkHealer(name):
    newChar = Character()
    newChar.name = str(name)
    newChar.startClss = "Healer"
    newChar.currClss = "Healer"
    newChar.level = 1
    newChar.attrPts = 0
    newChar.STR = 35
    newChar.INT = 65
    newChar.END = 60
    newChar.AGI = 40
    statsConvert(newChar)
    return newChar



#############
# FUNCTIONS #
#############

### CREATE A CHARACTER ### 
def makeCharacter(charName,charClssInput):
    if charClssInput == "Fighter":
        return mkFighter(charName)
    elif charClssInput == "Guardian":
        return mkGuardian(charName)
    elif charClssInput == "Rogue":
        return mkRogue(charName)
    elif charClssInput == "Ranger":
        return mkRanger(charName)
    elif charClssInput == "Mage":
        return mkMage(charName)
    elif charClssInput == "Healer":
        return mkHealer(charName)


### DISPLAY CHARACTER LIBRARY ###
def displayExampleCharInfo(char):
    print("Class:",char.startClss,\
          "\nHealth:",char.HP,\
          "\nMana:",char.MP,\
          "\nStrength:",char.STR,\
          "\nIntelligence:",char.INT,\
          "\nEndurance:",char.END,\
          "\nAgility:",char.AGI)


### DISPLAY CURRENT CHARACTER INFO ###    
def displayCharInfo(char):
    print("Name: ",char.name,\
          "\nStarting Class: ",char.startClss,\
          "\nCurrent Class: ",char.currClss,\
          "\nLevel: ",char.level,\
          "\nAttribute Points: ",char.attrPts,\
          "\nHealth: ",char.HP,\
          "\nMana: ",char.MP,\
          "\nStrength: ",char.STR,\
          "\nIntelligence: ",char.INT,\
          "\nEndurance: ",char.END,\
          "\nAgility: ",char.AGI,\
          "\nP.Atk: ",char.PATK,\
          "\nP.Def: ",char.PDEF,\
          "\nM.Atk: ",char.MATK,\
          "\nM.Def: ",char.MDEF,\
          "\nSpeed: ",char.SPD,\
          "\nAccuracy: ",char.ACC,\
          "\nEvasion: ",char.EVA,\
          "\nCrit Rate: ",char.CRITRATE,"%",\
          "\nCrit Resist: ",char.CRITRES,"%",\
          "\nCrit Damage: x",char.CRITDMG," or ",int(round(char.CRITDMG*100,0)),"%",\
          "\nArtz Damage: ",char.AD,\
          "\nArtz Support: ",char.AS,\
          sep = "")

"""
    Author: David Thong Nguyen
    Date Created: Nov 15th, 2013

Date Modified: Nov 17th, 2013
    - tested random damage multiplier [8,9]
    - decided multiplier's optimal range: [8,10]
    --> Damage is quite balanced

NEXT OBJECTIVES:
    + add evasion system/check accuracy
"""


import random
import math

def normalHit(attacker,target):
    damage = physDamage(attacker,target)
    if critHit(attacker,target) == True:
        damage = int(round((damage*attacker.CRITDMG),0))
        print("\n",attacker.name," inflicts ",damage,\
              " damage on ",target.name,"!",sep="")
        print("It's a critical hit!")
    else:
        print("\n",attacker.name," inflicts ",damage,\
              " damage on ",target.name,"!",sep="")
    if damage > 0:
        target.HP -= damage
    elif damage <= 0:
        print(attacker.name,"missed.")
    

def critHit(attacker,target):
    critChance = int(round(((attacker.CRITRATE/target.CRITRES) * 2.5),0))
    RNGList = []
    for x in range(0,critChance):
        RNG = random.randint(0,100)
        if RNG == critChance:
            return True
        else:
            RNGList.append(RNG)
    return False


def physDamage(attacker,target):
    return int(round(math.sqrt((attacker.PATK / target.PDEF)\
                    * random.randrange(8,10) / 10) * 22,0))


def magDamage(attacker,target):
    return int(round(math.sqrt((attacker.MATK / target.MDEF)\
                    * random.randrange(8,10) / 10) * 22,0))

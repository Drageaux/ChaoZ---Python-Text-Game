"""
    Author: David Thong Nguyen
    Date Created: Nov 15th, 2013

Date Modified: Nov 17th, 2013
    - lowered Goblin's END by half
    - lowered Goblin's STR a little
    --> Goblin's END is a little low(?), possible for Fighter for 2HKO
"""


import random 

class Enemy():
    __slots__ = ("name","level",\
                 "HP","MP","STR","INT","END","AGI",\
                 "PATK","PDEF","MATK","MDEF",\
                 "SPD","ACC","EVA","CRITRATE","CRITRES","CRITDMG")
def mkGoblin():
    enemy = Enemy()
    enemy.name = "Goblin"
    enemy.level = 1
    enemy.STR = random.randint(30,33)
    enemy.INT = random.randint(15,18)
    enemy.END = random.randint(12,15)
    enemy.AGI = random.randint(33,36)

    enemy.HP = int(round(((enemy.STR * 2) + (enemy.END * 5) / 20),0))
    enemy.MP = int(round(((enemy.INT * 7) / 20),0))
    enemy.PATK = int(round((((enemy.STR * 5) + (enemy.AGI * 2)) / 10),0))
    enemy.PDEF = int(round((((enemy.STR * 2) + (enemy.END * 5)) / 10),0))
    enemy.MATK = int(round(((enemy.INT * 7) / 10),0))
    enemy.MDEF = int(round((((enemy.INT * 2) + (enemy.END * 5)) / 10),0))
    enemy.SPD = int(round(((enemy.AGI * 7) / 10),0))
    enemy.ACC = int(round((((enemy.STR * 2) + (enemy.AGI * 5)) / 10),0))
    enemy.EVA = int(round((((enemy.END * 2) + (enemy.AGI * 5)) / 10),0))
    enemy.CRITRATE = round(((enemy.STR * 0.05) + (enemy.AGI * 0.125)),2)
    enemy.CRITRES = round(((enemy.END * 0.125) + (enemy.AGI * 0.05)),2)
    enemy.CRITDMG = (round(((enemy.STR * 0.2) + (enemy.AGI * 0.1)),2)/100)
    return enemy


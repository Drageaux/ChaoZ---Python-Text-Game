import random
import createChar
import createMobs

"""
print(13)
critical_hit = False
RNGList = []
for x in range(0,13):
    RNG = random.randint(0,100)
    if RNG == 13:
        RNGList.append(RNG)
        print(RNGList)
        critical_hit = True
        break
    else:
        RNGList.append(RNG)
        print(RNGList)
print(critical_hit)
"""
"""
playerList = [createChar.mkRogue("David")]
def battle(playerList):
    enemyList = []
    for x in range(random.randint(1,4)):
        goblin = createMobs.mkGoblin()
        enemyList.append(goblin)
    print(enemyList)
battle(playerList)
"""




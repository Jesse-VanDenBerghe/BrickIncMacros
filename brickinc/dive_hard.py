import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from enum import Enum
from utils.adb import *
from utils.ochestrator import *
from utils.stack import *
from brickinc.upgrades import *
from brickinc.brick import *
from brickinc.rank import *
from datetime import datetime, timedelta
import asyncio

class Abilities(Enum):
    GOLDEN_PAINT = (1, 2, 0, 0)
    OUTPUT_AMPLIFICATION = (2, 5, 0, 0)
    DEEP_DIVE = (3, 10, 0, 0)
    GREEDY_HAND = (4, 20, 0, 0)
    ADRENALIN_BOOSRTER = (5, 30, 0, 0)
    ELECTRIC_BRAIN = (6, 50, 0, 0)

    def __init__(self, code, cost, x, y):
        self.code = code
        self.cost = cost
        self.x = x
        self.y = y

abilityBuyStack = Stack([
    Abilities.ELECTRIC_BRAIN,
    Abilities.ADRENALIN_BOOSRTER,
    Abilities.GREEDY_HAND,
    Abilities.DEEP_DIVE,
    Abilities.OUTPUT_AMPLIFICATION,
    Abilities.GOLDEN_PAINT
])

AP = 0

async def incrementAP():
    global AP
    while True:
        await asyncio.sleep(10)
        AP += 1

def buyAbilities():
    global AP
    while not abilityBuyStack.isEmpty():
        nextAbility = abilityBuyStack.peek()
        if AP >= nextAbility.cost:
            AP -= nextAbility.cost
            abilityBuyStack.pop()
            buyAbility(nextAbility.code, nextAbility.x, nextAbility.y)
        else:
            break

def buyAbility(code, x, y):
    print(f"Buying ability {code} at ({x}, {y})")
    # Implement the actual ability purchase logic here

DIVE_DURATION = 5 * 60 # seconds
ALMOST_DONE = 20 # seconds

async def dive():
    rankUp = RankUp.SMALL_RANK_UP 
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=DIVE_DURATION)

    apCounterTask = asyncio.create_task(incrementAP())

    while datetime.now() < endTime:
        
        if rankUp != RankUp.NO_RANK_UP:
            upgradeFields()
            autoFire()


        loopAmount = 5 if rankUp == RankUp.BIG_RANK_UP else 3

        for _ in range(loopAmount):
            buyAbilities()

            upgradeWeapons()
            upgradeResearch()
            upgradeFields()
            upgradeAllUpgrades()

            if datetime.now() >= endTime - timedelta(seconds=ALMOST_DONE):
                print("Almost done with dive, exiting loop early to rank up before end.")
                break

        rankUp = upgradeRank()

    apCounterTask.cancel()
    print("Dive complete.")

asyncio.run(dive())
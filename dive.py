from adb import *
from ochestrator import *
from upgrades import *
from brick import *
from rank import *

def dive():
    rankUp = RankUp.SMALL_RANK_UP

    while True:
        
        if rankUp != RankUp.NO_RANK_UP:
            upgradeFields()
            autoFire()


        loopAmount = 5 if rankUp == RankUp.BIG_RANK_UP else 3

        for _ in range(loopAmount):
            upgradeWeapons()
            upgradeResearch()
            upgradeFields()
            upgradeAllUpgrades()

        rankUp = upgradeRank()


dive()
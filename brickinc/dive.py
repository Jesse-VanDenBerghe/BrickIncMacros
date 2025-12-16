import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.adb import *
from utils.ochestrator import *
from brickinc.upgrades import *
from brickinc.brick import *
from brickinc.rank import *

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
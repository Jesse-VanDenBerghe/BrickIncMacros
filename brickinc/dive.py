import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.adb import *
from utils.ochestrator import *
from brickinc.upgrades import *
from brickinc.brick import *
from brickinc.rank import *
from datetime import datetime, timedelta

DIVE_DURATION = 5 * 60 # seconds
ALMOST_DONE = 20 # seconds

def dive():
    rankUp = RankUp.SMALL_RANK_UP 
    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=DIVE_DURATION)

    while datetime.now() < endTime:
        
        if rankUp != RankUp.NO_RANK_UP:
            upgradeFields()
            autoFire()


        loopAmount = 5 if rankUp == RankUp.BIG_RANK_UP else 3

        for _ in range(loopAmount):
            upgradeWeapons()
            upgradeResearch()
            upgradeFields()
            upgradeAllUpgrades()

            if datetime.now() >= endTime - timedelta(seconds=ALMOST_DONE):
                print("Almost done with dive, exiting loop early to rank up before end.")
                break

        rankUp = upgradeRank()
    
    print("Dive complete.")


dive()
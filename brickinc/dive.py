import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from utils.stack import Stack
from utils.adb import *
from utils.ochestrator import *
from brickinc.upgrades import *
from brickinc.brick import *
from brickinc.rank import *
from datetime import datetime, timedelta

DIVE_DURATION = 5 * 60 # seconds

def bestDive():

    RANK_UP_TRIGGERS = Stack([
        280, 210, 120, 30
    ])

    rankUp = RankUp.SMALL_RANK_UP 
    nextTrigger = 0

    startTime = datetime.now()
    endTime = startTime + timedelta(seconds=DIVE_DURATION)

    while datetime.now() < endTime:
        
        if rankUp != RankUp.NO_RANK_UP:
            upgradeFields()
            autoFire()

        while datetime.now() < endTime:

            upgradeWeapons()
            upgradeResearch()
            upgradeFields()
            upgradeAllUpgrades()

            if datetime.now() >= endTime:
                print("Dive time over, exiting loop.")
                break

            try:
                nextTrigger = RANK_UP_TRIGGERS.peek()
            except:
                nextTrigger = DIVE_DURATION + 1

            print(f"Next rank up trigger at {nextTrigger} seconds.")

            if datetime.now() >= startTime + timedelta(seconds=nextTrigger):
                trigger = RANK_UP_TRIGGERS.pop()
                print(f"Rank up trigger reached {trigger}, exiting loop rank up before end.")
                break

        rankUp = upgradeRank()
    
        if datetime.now() >= endTime - timedelta(seconds=20):
            print("Almost done with dive, taking final screenshot.")
            createFullScreenShot("" + datetime.now().strftime("%Y%m%d_%H%M%S") +"_final_dive_280_210_120_30.png")
            break
    
    print("Dive complete.")

bestDive()
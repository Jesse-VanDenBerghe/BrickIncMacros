from adb import *
from ochestrator import *
from upgrades import *
from brick import *
from rank import *

def dive():
    while True:

        for _ in range(3):
            autoFire()
            ensureUpgradesClosed()
            upgradeWeapons()
            upgradeResearch()
            upgradeFields()

            upgradeAllUpgrades()

        upgradeRank()

        wait()


dive()
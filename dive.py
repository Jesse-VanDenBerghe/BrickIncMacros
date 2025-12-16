from adb import *
from ochestrator import *
from upgrades import *
from brick import *

def dive():
    while True:

        autoFire()
        ensureUpgradesClosed()
        upgradeWeapons()
        upgradeResearch()
        upgradeFields()

        upgradeAllUpgrades()

        wait()


dive()
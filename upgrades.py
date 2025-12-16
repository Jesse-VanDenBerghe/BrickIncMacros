from adb import *
from ochestrator import *

TOGGLE_UPGRADES = 360, 2770

atUpgrades = False
def toggleUpgrades():
    global atUpgrades
    tapAt(*TOGGLE_UPGRADES)
    wait(.2)
    atUpgrades = not atUpgrades

def ensureUpgradesOpen():
    global atUpgrades
    if not atUpgrades:
        toggleUpgrades()

def ensureUpgradesClosed():
    global atUpgrades
    if atUpgrades:
        toggleUpgrades()

def upgradeAllUpgrades():
    ensureUpgradesOpen()
    
    upgradeSouls()
    upgradeScience()
    upgradeDimensions()

    ensureUpgradesClosed()

TO_SOUL_MENU = 1080, 670
CLOSE_SOUL_MENU = 100, 2580
TO_SOUL_ALTAR = 400, 2570
UPGRADE_SOUL_ALTAR = 680, 1100
TO_SOUL_UPGRADES = 730, 2570
UPGRADE_SOUL_UPGRADES = 790, 920
TO_SOUL_ENHANCEMENTS = 1100, 2570
UPGRADE_SOUL_ENHANCEMENTS = 790, 920

atSoulMenu = False
def ensureSoulMenuOpen():
    global atSoulMenu
    if not atSoulMenu:
        tapAt(*TO_SOUL_MENU)
        wait(WAIT_LONG)
        atSoulMenu = True


def closeSoulMenu():
    global atSoulMenu
    if atSoulMenu:
        tapAt(*CLOSE_SOUL_MENU)
        wait(WAIT_LONG)
        atSoulMenu = False

def upgradeSouls():
    ensureSoulMenuOpen()

    wait(WAIT_LONG)
    tapAt(*TO_SOUL_ALTAR)
    wait()
    tapAt(*UPGRADE_SOUL_ALTAR)
    wait(WAIT_LONG)

    tapAt(*TO_SOUL_UPGRADES)
    wait()
    rapidTap(*UPGRADE_SOUL_UPGRADES, 2, 3)
    wait(WAIT_LONG)

    tapAt(*TO_SOUL_ENHANCEMENTS)
    wait()
    rapidTap(*UPGRADE_SOUL_ENHANCEMENTS, 2, 3)
    wait(WAIT_LONG)

    closeSoulMenu()

TO_SCIENCE_MENU = 210, 1320
UPGRADE_SCIENCE = 800, 1300
UPGRADE_SCIENCE_ALL = 650, 1000
CLOSE_SCIENCE_MENU = 100, 2580

atScienceMenu = False
def ensureScienceMenuOpen():
    global atScienceMenu
    if not atScienceMenu:
        tapAt(*TO_SCIENCE_MENU)
        wait(WAIT_LONG)
        atScienceMenu = True

def closeScienceMenu():
    global atScienceMenu
    if atScienceMenu:
        tapAt(*CLOSE_SCIENCE_MENU)
        wait(WAIT_LONG)
        atScienceMenu = False

def upgradeScience():
    ensureScienceMenuOpen()

    rapidTap(*UPGRADE_SCIENCE, 3, 3)
    tapAt(*UPGRADE_SCIENCE_ALL)

    closeScienceMenu()

TO_DIMENSION_MENU = 650, 1300
UPGRADE_DIMENSIONS = 800, 920
CLOSE_DIMENSION_MENU = 100, 2580

atDimensionMenu = False
def ensureDimensionMenuOpen():
    global atDimensionMenu
    if not atDimensionMenu:
        tapAt(*TO_DIMENSION_MENU)
        wait(WAIT_LONG)
        atDimensionMenu = True

def closeDimensionMenu():
    global atDimensionMenu
    if atDimensionMenu:
        tapAt(*CLOSE_DIMENSION_MENU)
        wait(WAIT_LONG)
        atDimensionMenu = False

def upgradeDimensions():
    ensureDimensionMenuOpen()

    rapidTap(*UPGRADE_DIMENSIONS, 3, 3)

    closeDimensionMenu()
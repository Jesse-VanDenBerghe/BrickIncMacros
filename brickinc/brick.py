from utils.adb import *
from utils.ochestrator import *

AUTOFIRE = 625, 2750

TO_WEAPON_MENU = 855, 2570
WEAPON_BUY_ALL = 790, 1820
WEAPON_UPGRADE_ALL = 1010, 1820
WEAPON_EQUIP_ALL = 1150, 1820

TO_RESEARCH_MENU = 1000, 2570
RESEARCH_UPGRADE_ALL = 670, 1570
RESEARCH_UP = 90, 2570
RESEARCH_DOWN = 180, 2570
RESEARCH_1 = 1050, 2160
RESEARCH_2 = 1050, 1900
RESEARCH_3 = 1050, 1700

TO_FIELDS_MENU = 1180, 2570
FIELDS_UNLOCK_ASSIST = 824, 1570
FIELD_TO_LAST_SELECTABLE = 200, 2580
FIELD_SELECT_LAST_SELECTABLE = 700, 1850

def autoFire():
    rapidTap(*AUTOFIRE, 20, 1)
    wait(WAIT_MEDIUM)

def autoFireAlot():
    rapidTap(*AUTOFIRE, 30, 1)
    wait(WAIT_MEDIUM)

def upgradeWeapons():
    tapAt(*TO_WEAPON_MENU)
    wait()
    tapAt(*WEAPON_BUY_ALL)
    wait(WAIT_SHORT)
    tapAt(*WEAPON_UPGRADE_ALL)
    wait(WAIT_SHORT)
    tapAt(*WEAPON_EQUIP_ALL)
    wait(WAIT_SHORT)

def upgradeResearch():
    tapAt(*TO_RESEARCH_MENU)
    wait(WAIT_MEDIUM)
    tapAt(*RESEARCH_UPGRADE_ALL)
    wait(WAIT_SHORT)
    tapAt(*RESEARCH_UP)
    wait(WAIT_SHORT)
    tapAt(*RESEARCH_DOWN)
    wait(WAIT_MEDIUM)
    tapAt(*RESEARCH_1)
    wait(WAIT_SHORT)
    tapAt(*RESEARCH_2)
    wait(WAIT_SHORT)
    tapAt(*RESEARCH_3)
    wait(WAIT_SHORT)

    swipeUpAndHold(*RESEARCH_3, -550, 800, 200)

    tapAt(*RESEARCH_2)
    wait(WAIT_SHORT)
    tapAt(*RESEARCH_3)
    wait(WAIT_MEDIUM)

    tapAt(*RESEARCH_UPGRADE_ALL)
    wait(WAIT_MEDIUM)

def upgradeFields():
    tapAt(*TO_FIELDS_MENU)
    wait(WAIT_LONG)
    tapAt(*FIELDS_UNLOCK_ASSIST)
    wait(WAIT_SHORT)
    tapAt(*FIELD_TO_LAST_SELECTABLE)
    wait(WAIT_MEDIUM)
    tapAt(*FIELD_SELECT_LAST_SELECTABLE)
    wait(WAIT_SHORT)
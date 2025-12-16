from adb import *
from image import *
from ochestrator import *

TO_RANK_MENU = 640, 420
NEXT_RANK_UP_COLOR = (132,255,0)
PREV_RANK_UP = 300, 1000
NEXT_RANK_UP = 1000, 1000
NEXT_RANK_UP_INDICATOR = 1027, 1037
UPGRADE_RANK = 650, 1850

def checkForRankUp():
    screenshotFile = 'images/artifacts/next_rank_up.png'
    createFullScreenShot(screenshotFile)
    colorAtPixel = getColorAtPixel(screenshotFile, *NEXT_RANK_UP_INDICATOR)
    colorsAreMatching = areColorsMatching(colorAtPixel, NEXT_RANK_UP_COLOR, tolerance=30)
    return colorsAreMatching

atRankMenu = False
def ensureRankMenuOpen():
    global atRankMenu
    if not atRankMenu:
        tapAt(*TO_RANK_MENU)
        wait(WAIT_LONG)
        atRankMenu = True

def closeRankMenu():
    global atRankMenu
    if atRankMenu:
        tapAt(*TO_RANK_MENU)
        wait(WAIT_LONG)
        atRankMenu = False

def upgradeRank():
    ensureRankMenuOpen()

    rankUp = False

    # Some weird bug where the rank up indication doesn't show up unless you cycle through the rank ups
    tapAt(*NEXT_RANK_UP)
    wait(WAIT_MEDIUM)
    tapAt(*PREV_RANK_UP)
    wait(WAIT_LONG)

    while checkForRankUp():
        rankUp = True
        wait(WAIT_MEDIUM)
        tapAt(*NEXT_RANK_UP)
        wait(WAIT_LONG)
    
    if rankUp:
        tapAt(*UPGRADE_RANK)
        wait(WAIT_LONG)

    closeRankMenu()

from utils.adb import *
from utils.image import *
from utils.ochestrator import *
from enum import Enum
from PIL import Image

TO_RANK_MENU = 640, 420
NEXT_RANK_UP_COLOR = (132,255,0)
PREV_RANK_UP = 300, 1000
PREV_RANK_UP_INDICATOR = 344, 1037
CURRENT_RANK_UP_INDICATOR = 710, 1058
NEXT_RANK_UP = 1000, 1000
NEXT_RANK_UP_INDICATOR = 1027, 1037
UPGRADE_RANK = 650, 1850

class RankState(Enum):
    PREV_RANK_UP = 1
    CURRENT_RANK_UP = 2
    NEXT_RANK_UP = 3

class RankUp(Enum):
    BIG_RANK_UP = 1
    SMALL_RANK_UP = 2
    NO_RANK_UP = 3

def checkForRankUp() -> RankState | None:
    rankUp = None

    screenshotFile = 'images/artifacts/next_rank_up.png'

    createFullScreenShot(screenshotFile)
    img = Image.open(screenshotFile).convert('RGB')
    
    if areColorsMatching(getColorAtPixelFromImage(img, *NEXT_RANK_UP_INDICATOR), NEXT_RANK_UP_COLOR, tolerance=30):
        rankUp = RankState.NEXT_RANK_UP
    elif areColorsMatching(getColorAtPixelFromImage(img, *CURRENT_RANK_UP_INDICATOR), NEXT_RANK_UP_COLOR, tolerance=30):
        rankUp = RankState.CURRENT_RANK_UP
    elif areColorsMatching(getColorAtPixelFromImage(img, *PREV_RANK_UP_INDICATOR), NEXT_RANK_UP_COLOR, tolerance=30):
        rankUp = RankState.PREV_RANK_UP
    else:
        rankUp = None
        
    print(f'checkForRankUp: {rankUp}')
    return rankUp

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

def upgradeRank() -> RankUp:
    ensureRankMenuOpen()

    rankUpIsSelected = False
    bigUpgradeAttempted = False
    while not rankUpIsSelected:
        tapAt(*NEXT_RANK_UP)
        wait(WAIT_MEDIUM)
        tapAt(*NEXT_RANK_UP)
        wait(WAIT_MEDIUM)

        state = checkForRankUp()
        if state == RankState.PREV_RANK_UP:
            tapAt(*PREV_RANK_UP)
            wait(WAIT_MEDIUM)
            rankUpIsSelected = True
        elif state == RankState.CURRENT_RANK_UP:
            rankUpIsSelected = True
        elif state == RankState.NEXT_RANK_UP:
            bigUpgradeAttempted = True
            pass
        elif state is None:
            break
    
    if rankUpIsSelected:
        tapAt(*UPGRADE_RANK)
        wait(WAIT_MEDIUM)

    closeRankMenu()
    if bigUpgradeAttempted:
        return RankUp.BIG_RANK_UP
    elif rankUpIsSelected:
        return RankUp.SMALL_RANK_UP
    else:
        return RankUp.NO_RANK_UP

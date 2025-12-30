from utils.adb import tapAt, createFullScreenShot
from utils.logger import log, logh1
from utils.image import areColorsMatching, getColorAtPixelFromImage
from utils.ochestrator import wait, WAIT_MEDIUM, WAIT_LONG
from enum import Enum
from PIL import Image

TO_RANK_MENU = 640, 420
NEXT_RANK_UP_COLOR = (132, 255, 0)
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


def ensureRankMenuOpen(atRankMenu: bool):
    log(1, "Making sure Rank is open")
    if not atRankMenu:
        log(2, "Opening Rank ...")
        tapAt(*TO_RANK_MENU)
        wait(WAIT_LONG)
        return True
    else:
        log(2, "!! Rank was already closed")
        return False


def closeRankMenu(atRankMenu: bool):
    log(1, "Making sure Rank is closed")
    if atRankMenu:
        log(2, "Closing Rank...")
        tapAt(*TO_RANK_MENU)
        wait(WAIT_LONG)
        return False
    else:
        log(2, "!! Rank was already closed")
        return True


def upgradeRank() -> RankUp:
    logh1("Rank up")
    atRankMenu = ensureRankMenuOpen(False)

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
        atRankMenu = False
    else:
        atRankMenu = closeRankMenu(atRankMenu)

    if bigUpgradeAttempted:
        return RankUp.BIG_RANK_UP
    elif rankUpIsSelected:
        return RankUp.SMALL_RANK_UP
    else:
        return RankUp.NO_RANK_UP

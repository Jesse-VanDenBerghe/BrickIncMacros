
from enum import Enum
from utils.adb import *
from utils.ochestrator import *
from utils.stack import *
import asyncio

class Abilities(Enum):
    GOLDEN_PAINT = (1, 2, 216, 822)
    OUTPUT_AMPLIFICATION = (2, 2, 467, 813)
    DEEP_DIVE = (3, 2, 714, 803)
    GREEDY_HAND = (4, 3, 213, 1214)
    ADRENALIN_BOOSRTER = (5, 3, 712, 1189)
    ELECTRIC_BRAIN = (6, 3, 959, 1194)

    def __init__(self, code, cost, x, y):
        self.code = code
        self.cost = cost
        self.x = x
        self.y = y

abilityBuyStack = Stack([
    Abilities.DEEP_DIVE,
    Abilities.ADRENALIN_BOOSRTER,
    Abilities.ELECTRIC_BRAIN,
    Abilities.OUTPUT_AMPLIFICATION,
    Abilities.GREEDY_HAND,
    Abilities.GOLDEN_PAINT
])

TO_ABILITY_MENU = 1191, 1221
BUY_ABILITY = 912, 2388
CLOSE_ABILITY_MENU = 700, 280

atAbilityMenu = False
def ensureAbilityMenuOpen():
    global atAbilityMenu
    if not atAbilityMenu:
        tapAt(*TO_ABILITY_MENU)
        wait(WAIT_LONG)
        atAbilityMenu = True

def closeAbilityMenu():
    global atAbilityMenu
    if atAbilityMenu:
        tapAt(*CLOSE_ABILITY_MENU)
        wait(WAIT_LONG)
        atAbilityMenu = False

AP = 0
ap_stop_flag = None

def incrementAP():
    import threading
    global ap_stop_flag
    ap_stop_flag = threading.Event()
    
    def _increment():
        global AP
        print("Starting AP incrementer task.")
        while not ap_stop_flag.is_set():
            sleep(10)
            AP += 1
            print(f"Incrementing AP by 1, total AP now: {AP}")
    
    thread = threading.Thread(target=_increment, daemon=True)
    thread.start()
    return thread

def stopAPIncrementer():
    global ap_stop_flag
    if ap_stop_flag:
        ap_stop_flag.set()

def buyAbilities():
    global AP
    while not abilityBuyStack.is_empty():
        nextAbility = abilityBuyStack.peek()
        print(f"Next ability to buy: {nextAbility.name} costing {nextAbility.cost} AP, current AP: {AP}")
        if AP >= nextAbility.cost:
            ensureAbilityMenuOpen()
            swipeUp(nextAbility.x, nextAbility.y + 400, -400, 500)
            AP -= nextAbility.cost
            abilityBuyStack.pop()
            wait(WAIT_MEDIUM)
            buyAbility(nextAbility.code, nextAbility.x, nextAbility.y)
            closeAbilityMenu()
        else:
            break


def buyAbility(code, x, y):
    print(f"Buying ability {code} at ({x}, {y})")
    tapAt(x, y)
    wait(WAIT_MEDIUM)
    tapAt(*BUY_ABILITY)
    wait(WAIT_MEDIUM)
from time import sleep

WAIT_SHORT = 0.05
WAIT_MEDIUM = 0.2
WAIT_LONG = 0.5

def wait(seconds = WAIT_MEDIUM):
    sleep(seconds)
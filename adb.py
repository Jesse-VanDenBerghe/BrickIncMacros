import subprocess
import random
from time import sleep

def list_adb_devices():
    try:
        output = subprocess.check_output(['adb', 'devices']).decode('utf-8')
        lines = output.split('\n')[1:]  # Skip the first line
        devices = [
            line.split('\t')[0]
            for line in lines
            if line.strip() and not line.strip().startswith('*')
        ]
        return devices
    except Exception as error:
        print(f'Error listing adb devices: {error}')
        return []
    
def rapidTap(x, y, count, interval_ms):
    try:
        for _ in range(count):
            randomizedLocation = x + random.randint(-5, 5), y + random.randint(-5, 5)
            tapAt(*randomizedLocation)
            randomized_interval = interval_ms + (interval_ms * 0.1 * (0.5 - random.random()))
            sleep(randomized_interval / 1000)
    except Exception as error:
        print(f'Error performing rapid tap at ({x}, {y}): {error}')
    
def tapAt(x, y):
    try:
        subprocess.run(['adb', 'shell', 'input', 'tap', str(x), str(y)], check=True)
    except Exception as error:
        print(f'Error performing tap at ({x}, {y}): {error}')

def holdAt(x, y, duration_ms):
    try:
        subprocess.run(['adb', 'shell', 'input', 'swipe', str(x), str(y), str(x), str(y), str(duration_ms)], check=True)
    except Exception as error:
        print(f'Error performing hold at ({x}, {y}) for {duration_ms} ms: {error}')
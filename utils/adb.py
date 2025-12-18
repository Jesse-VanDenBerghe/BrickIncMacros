import subprocess
import random
from time import sleep
from PIL import Image

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

def swipeFromTo(x1, y1, x2, y2, duration_ms):
    try:
        subprocess.run(['adb', 'shell', 'input', 'swipe', str(x1), str(y1), str(x2), str(y2), str(duration_ms)], check=True)
    except Exception as error:
        print(f'Error performing swipe from ({x1}, {y1}) to ({x2}, {y2}): {error}')

def swipeUp(x, y, distance, duration_ms):
    try:
        end_y = y - distance
        subprocess.run(['adb', 'shell', 'input', 'swipe', str(x), str(y), str(x), str(end_y), str(duration_ms)], check=True)
    except Exception as error:
        print(f'Error performing swipe up at ({x}, {y}) for distance {distance}: {error}')

def swipeUpAndHold(x, y, distance, swipe_duration_ms, hold_duration_ms):
    try:
        end_y = y - distance
        subprocess.run(['adb', 'shell', 'input', 'swipe', str(x), str(y), str(x), str(end_y), str(swipe_duration_ms)], check=True)
        sleep(0.05)
        subprocess.run(['adb', 'shell', 'input', 'swipe', str(x), str(end_y), str(x), str(end_y), str(hold_duration_ms)], check=True)
    except Exception as error:
        print(f'Error performing swipe and hold at ({x}, {y}) for distance {distance}: {error}')

def holdAt(x, y, duration_ms):
    try:
        subprocess.run(['adb', 'shell', 'input', 'swipe', str(x), str(y), str(x), str(y), str(duration_ms)], check=True)
    except Exception as error:
        print(f'Error performing hold at ({x}, {y}) for {duration_ms} ms: {error}')

def createScreenShotBetweenXandY(x1, y1, x2, y2, output_file='screenshot.png'):
    try:
        subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screenshot.png'], check=True)
        subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', output_file], check=True)
        img = Image.open(output_file)
        cropped_img = img.crop((x1, y1, x2, y2))
        cropped_img.save(output_file)
    except Exception as error:
        print(f'Error creating screenshot between ({x1}, {y1}) and ({x2}, {y2}): {error}')

def createFullScreenShot(output_file='screenshot.png'):
    try:
        subprocess.run(['adb', 'shell', 'screencap', '-p', '/sdcard/screenshot.png'], check=True)
        subprocess.run(['adb', 'pull', '/sdcard/screenshot.png', output_file], check=True)
    except Exception as error:
        print(f'Error creating full screenshot: {error}')
import math, time, winsound, cv2, easyocr, pyautogui, keyboard
import pyscreenshot as ImageGrab
import numpy as np
from matplotlib import pyplot as plt

def split(word):
    return [char for char in word]

# find mouse location
def mouse(x):
    for i in range(x):
        time.sleep(3)
        winsound.Beep(700, 300)
        pos = pyautogui.position()
        print(pos)
        winsound.Beep(900, 300)


def pr(p):
    keyboard.press(str(p))
    time.sleep(float(0.2))
    keyboard.release(str(p))
    time.sleep(float(0.3))


# grab screenshot of coords
def findCoords():
    keyboard.wait('space')
    winsound.Beep(700, 300)
    im = ImageGrab.grab(bbox=(100, 3, 330, 25))  # X1,Y1,X2,Y2 WHOLE
    im.save("coords.png")
    winsound.Beep(900, 300)

# ocr from image
def runOCR():
    global word
    global result
    img = 'coords.png'
    reader = easyocr.Reader(['en'], gpu=True)
    result = reader.readtext(img, detail=0)
    print(result)
    word = split(str(result))
    print(word)
    winsound.Beep(900, 150)
    winsound.Beep(900, 150)

def keyEntryHornet():
    global word
    keyboard.wait('space')
    winsound.Beep(700, 600)
    z = int(1)
    keyboard.press('`') # UFC
    time.sleep(float(0.2))
    keyboard.release('`')
    time.sleep(float(0.3))

    keyboard.press('.') # POSN
    time.sleep(float(0.2))
    keyboard.release('.')
    time.sleep(float(0.3))

    keyboard.press('2') # North
    time.sleep(float(0.5))
    keyboard.release('2')
    print('pressed North')
    for x in word:
        y = x.isnumeric()
        if y == True:
            time.sleep(float(0.15))
            #print('z =', z) # track step in list
            if z != 7 and z != 13:
                if z == 3 and int(x) == int(8):
                    print('Found an "8" in the 3rd digit, skipping.')
                else:
                    press = str(x)
                    keyboard.press_and_release(press)
                    z = z + 1
                    print('pressed', x)

            elif z == 7:
                keyboard.press_and_release('enter')
                keyboard.press('6')
                time.sleep(float(0.5))
                keyboard.release('6')
                time.sleep(float(0.1))
                keyboard.press_and_release('6')
                time.sleep(float(0.3))
                print('pressed enter and east')
                press = str(x)
                keyboard.press_and_release(press)
                print('pressed', x)
                z = z + 1

            elif z == 13:
                keyboard.press_and_release('enter')
                print('pressed enter')
                time.sleep(float(0.2))
                keyboard.press('=') # ELEV
                time.sleep(float(0.5))
                keyboard.release('=')
                print('changed to ELEV')
                time.sleep(float(0.2))
                keyboard.press('.') # FEET
                time.sleep(float(0.5))
                keyboard.release('.')
                time.sleep(float(0.3))
                press = str(x)
                keyboard.press_and_release(press)
                print('pressed', x)
                z = z + 1

            else:
                print('Skipping valid number', x)
        else:
            print(x+' is not a number. Skipping')

    time.sleep(0.5)
    keyboard.press_and_release('enter') # Enter after elevation
    print('pressed final enter')
    print(result)
    winsound.Beep(900, 150)
    winsound.Beep(900, 150)

def keyEntryTomcat():
    global word
    keyboard.wait('space')
    winsound.Beep(700, 600)
    z = int(1)
    keyboard.press('q') # Switch to TAC
    time.sleep(float(0.2))
    keyboard.release('q')
    time.sleep(float(2))

    keyboard.press('`') # WYPT 1
    time.sleep(float(0.2))
    keyboard.release('`')
    time.sleep(float(0.5))

    keyboard.press_and_release('.') # Clear
    time.sleep(float(0.2))
    keyboard.press_and_release('1') # Lat
    time.sleep(float(0.2))
    keyboard.press_and_release('=') # N/E

    for x in word:
        y = x.isnumeric()
        if y == True:
            time.sleep(float(0.3))
            #print('z =', z) # track step in list
            if z != 7 and z != 13:
                if z == 3 and int(x) == int(8):
                    print('Found an "8" in the 3rd digit, skipping.')
                else:
                    press = str(x)
                    keyboard.press_and_release(press)
                    z = z + 1
                    print('pressed', x)

            elif z == 7:
                keyboard.press_and_release('enter')
                keyboard.press_and_release('.') # Clear
                keyboard.press_and_release('6') # Lon
                keyboard.press_and_release('=') # N/E
                keyboard.press_and_release('0') # 0 for 6 digit CHANGE IF NEEDED
                print('pressed enter and east')
                press = str(x)
                keyboard.press_and_release(press)
                print('pressed', x)
                z = z + 1

            elif z == 13:
                keyboard.press_and_release('enter')
                print('pressed enter')
                time.sleep(float(0.2))
                keyboard.press_and_release('4') # ALT
                press = str(x)
                keyboard.press_and_release(press)
                print('pressed', x)
                z = z + 1

            else:
                print('Skipping valid number', x)
        else:
            print(x+' is not a number. Skipping')

    time.sleep(0.5)
    keyboard.press_and_release('enter') # Enter after elevation
    print('pressed final enter')
    print(result)
    winsound.Beep(900, 150)
    winsound.Beep(900, 150)


print("[1] F/A-18C")
print("[2] F-14B")
selAC = input("Select Aircraft: ")
if selAC == "1":
    while True:
        keyboard.wait('[')
        print('Waiting for coords')
        winsound.Beep(500, 200)
        #mouse(6)
        findCoords()
        runOCR()
        keyEntryHornet()
        if keyboard.is_pressed("]"):
            print("] pressed, ending program")
            break

elif selAC == "2":
    while True:
        keyboard.wait('[')
        print('Waiting for coords')
        winsound.Beep(500, 200)
        #mouse(6)
        findCoords()
        runOCR()
        keyEntryTomcat()
        if keyboard.is_pressed("]"):
            print("] pressed, ending program")
            break

else:
    print("Error: Invalid Aircraft Input.")

print(result)
input("\nEnd of line")

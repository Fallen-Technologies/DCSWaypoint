# DCS Waypoint Creator
# © 2021 AIBS,LLC
version = "2.6"

import sys, os, shutil, glob
os.system("git pull")

def split(word):
    return [char for char in word]

# find mouse location
def mouse(x):
    for i in range(x):
        time.sleep(5)
        winsound.Beep(700, 300)
        pos = pyautogui.position()
        print(pos)
        winsound.Beep(900, 300)

# press and release a key
def pr(p):
    keyboard.press(str(p))
    time.sleep(float(0.1))
    keyboard.release(str(p))
    time.sleep(float(0.1))


# grab screenshot of coords
def findCoords():
    keyboard.wait('space')
    winsound.Beep(700, 300)
    im = ImageGrab.grab(bbox=(100, 3, 330, 25))  # X1,Y1,X2,Y2 box
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

# hornet hsi data entry
def keyEntryHornet():
    global word
    keyboard.wait('space')
    winsound.Beep(700, 600)
    z = int(1)
    keyboard.press('`') # UFC
    time.sleep(float(0.2))
    keyboard.release('`')
    time.sleep(float(0.1))

    keyboard.press('.') # POSN
    time.sleep(float(0.2))
    keyboard.release('.')
    time.sleep(float(0.1))

    keyboard.press('2') # North
    time.sleep(float(0.3))
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
                keyboard.press('6') # East
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
                time.sleep(float(0.2))
                keyboard.release('=')
                print('changed to ELEV')
                time.sleep(float(0.1))
                keyboard.press('.') # FEET
                time.sleep(float(0.2))
                keyboard.release('.')
                time.sleep(float(0.1))
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

# tomcat tac data entry wypt 1
def keyEntryTomcat():
    global word
    keyboard.wait('space')
    winsound.Beep(700, 600)
    z = int(1)
    pr('q') # Switch to TAC
    time.sleep(float(1))
    pr('`') # WYPT 1
    pr('.') # Clear
    pr('1') # Lat
    pr('=') # N/E

    for x in word:
        y = x.isnumeric()
        if y == True:
            #print('z =', z) # track step in list
            if z != 7 and z != 13:
                if z == 3 and int(x) == int(8):
                    print('Found an "8" in the 3rd digit, skipping.')
                else:
                    press = str(x)
                    pr(press)
                    z = z + 1
                    print('pressed', x)

            elif z == 7:
                pr('enter')
                pr('.') # Clear
                pr('6') # Lon
                pr('=') # N/E
                pr('0') # 0 for 6 digit CHANGE IF NEEDED
                print('pressed enter and east')
                press = str(x)
                pr(press)
                print('pressed', x)
                z = z + 1

            elif z == 13:
                pr('enter')
                print('pressed enter')
                pr('4') # ALT
                press = str(x)
                pr(press)
                print('pressed', x)
                z = z + 1

            else:
                print('Skipping valid number', x)
        else:
            print(x+' is not a number. Skipping')

    pr('enter') # Enter after elevation
    print('pressed final enter')
    print(result)
    winsound.Beep(900, 150)
    winsound.Beep(900, 150)


print("[0] Screen Coords Finder")
print("[1] F/A-18C")
print("[2] F-14B")
print("[3] F-16C (in development)")
selAC = input("Select Aircraft: ")
print("Running...")
if selAC == "0":
    posCount = input("Find how many coords?: ")
    keyboard.wait('space')
    mouse(int(posCount))

elif selAC == "1":
    import math, time, winsound, cv2, easyocr, pyautogui, keyboard
    import pyscreenshot as ImageGrab
    import numpy as np
    from matplotlib import pyplot as plt
    print("\nready\n")
    while True:
        keyboard.wait('[')
        print('Waiting for coords')
        winsound.Beep(500, 200)
        #mouse(6)
        findCoords()
        runOCR()
        keyEntryHornet()
        print(result)

elif selAC == "2":
    import math, time, winsound, cv2, easyocr, pyautogui, keyboard
    import pyscreenshot as ImageGrab
    import numpy as np
    from matplotlib import pyplot as plt
    print("\nready\n")
    while True:
        keyboard.wait('[')
        print('Waiting for coords')
        winsound.Beep(500, 200)
        #mouse(6)
        findCoords()
        runOCR()
        keyEntryTomcat()
        print(result)

else:
    print("Error: Invalid Aircraft Input.")

input("\nEnd of line")

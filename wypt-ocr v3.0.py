# DCS Waypoint Creator
# © 2021 AIBS,LLC

import sys, os, shutil, glob, time

# pull updates
print("Checking for updates...")
os.system("git pull")
time.sleep(2)
os.system("cls")

# create res.txt if non-existent
file_name = 'res.txt'
c = open(file_name, 'a+')  # open file in append mode
c.close()

# change res
def changeRes():
    global res, resf
    print("[1] 1920x1080")
    print("[2] 2560x1440")
    selres = input("What resolution are you running?: ")
    if selres == "1":
        c = open("res.txt", 'w')
        c.write('1920x1080')
        c.close()
        res = "1080"
        resf = "1920x1080"
        print("\nResolution set!")
        time.sleep(2)
        os.system("cls")
    elif selres == "2":
        c = open("res.txt", 'w')
        c.write('2560x1440')
        c.close()
        res = "1440"
        resf = "2560x1440"
        print("\nResolution set!")
        time.sleep(2)
        os.system("cls")
    else:
        input("Invalid input! Please restart the program.")
        exit()

# Check res settings
if '1920x1080' in open(file_name).read():
    res = "1080"
    resf = "1920x1080"
elif '2560x1440' in open(file_name).read():
    res = "1440"
    resf = "2560x1440"
else:
    print("<< == DCS Waypoint Creator == >>\n© 2021 AIBS,LLC\n")
    print("Resolution setting not found\n")
    changeRes()


def split(word):
    return [char for char in word]

# find mouse location
def mouse(x):
    time.sleep(5)
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
    global res
    keyboard.wait('space')
    winsound.Beep(700, 300)
    if res == "1080":
        im = ImageGrab.grab(bbox=(116, 7, 305, 25)) # X1,Y1,X2,Y2 box
        im.save("coords.png")
    elif res == "1440":
        im = ImageGrab.grab(bbox=(100, 3, 330, 25)) # X1,Y1,X2,Y2 box
        im.save("coords.png")
    winsound.Beep(900, 300)

# ocr from image
def runOCR():
    global word, result
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
    print('\nfinished')
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
    print('\nfinished')
    winsound.Beep(900, 150)
    winsound.Beep(900, 150)
print("<< == DCS Waypoint Creator == >>\n© 2021 AIBS,LLC\n")
print("Current Resolution:",resf,"\n")
print("-----<< Aircraft Selection >>-----")
print("[0] Change Resolution")
print("[1] F/A-18C")
print("[2] F-14B")
print("[3] F-16C (coming soon...)")
selAC = input("\nSelect Aircraft: ")
if selAC == "find":
    import winsound, pyautogui, keyboard
    posCount = input("Find how many coords?: ")
    mouse(int(posCount))

elif selAC == "0":
    changeRes()
    print("Program Restart Required")

elif selAC == "1":
    print("Running...")
    import math, winsound, cv2, easyocr, pyautogui, keyboard
    import pyscreenshot as ImageGrab
    import numpy as np
    from matplotlib import pyplot as plt
    print("\nready\n")
    while True:
        keyboard.wait('[')
        print('Waiting for coords')
        winsound.Beep(500, 200)
        findCoords()
        runOCR()
        keyEntryHornet()
        print(result)

elif selAC == "2":
    print("Running...")
    import math, winsound, cv2, easyocr, pyautogui, keyboard
    import pyscreenshot as ImageGrab
    import numpy as np
    from matplotlib import pyplot as plt
    print("\nready\n")
    while True:
        keyboard.wait('[')
        print('Waiting for coords')
        winsound.Beep(500, 200)
        findCoords()
        runOCR()
        keyEntryTomcat()
        print(result)

elif selAC == "3":
    print("\nI said: Coming... Soon...")
    print("Someone can't read smh")

else:
    print("Error: Invalid Aircraft Input.")

input("\nEnd of line")

import sys, os, shutil, glob

print("=== DCS Waypoint Creator Updater ===")
print("[1] Update Files")
print("[2] First Time Setup")
sel = input()
if sel == "1":
    if os.path.exists("/keybinds"):
        os.rmdir("/keybinds")
    print("Updating...")
    os.system("git pull")
    print("Done")


elif sel == "2":
    os.system("pip install pip --upgrade")
    os.system("pip install opencv-python")
    os.system("pip install easyocr")
    os.system("pip install pyautogui")
    os.system("pip install keyboard")
    os.system("pip install numpy")
    os.system("pip install matplotlib")
    os.system("pip install pyscreenshot")


else:
    print("Invalid Entry")


# End of line
input("\n\nEnd of Line - Press Enter to Exit\n")
os.system('cls')
exec(open("updater.py").read())

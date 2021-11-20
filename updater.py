import sys, os, shutil, glob

print("=== DCS Waypoint Creator Updater ===")
print("[1] Update Files")
print("[2] First Time Setup")
sel = input()
if sel == "1":
    os.remove("./keybinds")
    print("Cloning keybinds...")
    os.system("git clone https://github.com/TristanPFox/DCSWaypoint.git")
    os.system("git pull https://github.com/TristanPFox/DCSWaypoint.git")


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

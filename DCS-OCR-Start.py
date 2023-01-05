# DCS Waypoint Creator
# © 2023 AIBS,LLC
# https://discord.gg/fallen-angels
import os
try:
    import pyAesCrypt, time, requests
    from getmac import get_mac_address as gma
    from pathlib import Path
except ImportError:
    os.system("pip install -r requirements.txt")
    print("\n\nA NEW UPDATE has been Installed!\n Exit and Relaunch to Apply Update...")
    input("")
    exit()

mID = str(gma())
lic = Path('LICENSE.FALLEN')
LIC_SERVER_URL = "https://lic.zipmunks.com"

if lic.is_file():
    key = open(lic).read()
    if len(key) != 24:
        print('ERROR: Invalid License File\nTry Deleting LICENSE.FALLEN and re-entering your key')
        input()
        exit()
    print('Valid License File Found!')
else:
    print("<< == DCS Waypoint Creator == >>\n© 2023 AIBS,LLC\nhttps://discord.gg/fallen-angels\n")
    print("Paste License Key Below!")
    print("Key Format: xxxx-xxxx-xxxx-xxxx-xxxx\n")
    key = input()
    if len(key) != 24:
        print('Invalid Entry')
        input()
        exit()
key2 = key
print("Connecting to Fallen Licensing Servers...")
response = requests.get(f"{LIC_SERVER_URL}/devapi/v1/dcs_check?lic={key2}&ma={mID}")
r = response.json()
if r["data"] == "False":
    (f"\n\nERROR: INVALID LICENSE\nContact us at discord.gg/fallen-angels if you are having issues...")
    input("")
    exit()
print("Server Acknowledged License.")
key = r["data"]
print("Starting program...")
bufferSize = 64 * 1024
my_file = Path("wypt_ocr.py.aes")
# update
versionCurrent = open('version.txt').read()
import update
versionFound = open('version.txt').read()
if versionCurrent == versionFound:
    # already on latest version
    time.sleep(1)
else:
    print("A NEW UPDATE has been Installed!\n Exit and Relaunch to Apply Update...")
    input("")
    exit()
os.system("cls")
try:
    if my_file.is_file():
        pyAesCrypt.decryptFile("wypt_ocr.py.aes", "wypt_ocr.py", key, bufferSize)
        try:
            import wypt_ocr
        except Exception:
            import os
            os.remove('wypt_ocr.py')
            print("\nSomething went wrong.")
            input("")
            exit()
except ValueError:
    print(f"\n\nERROR: INVALID LICENSE\nContact us at discord.gg/fallen-angels if you are having issues...")

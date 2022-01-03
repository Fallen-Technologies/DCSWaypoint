# DCS Waypoint Creator
# © 2021 AIBS,LLC
# https://discord.gg/fallen-angels

import socket, os, pyAesCrypt, time
from pathlib import Path
lic = Path('LICENSE.FALLEN')
if lic.is_file():
    key = open(lic).read()
    print('Valid License Found!')
    time.sleep(0.5)
else:
    print("<< == DCS Waypoint Creator == >>\n© 2021 AIBS,LLC\nhttps://discord.gg/fallen-angels\n")
    print("Paste License Key Below!")
    print("Key Format: xxxx-xxxx-xxxx-xxxx-xxxx\n")
    key = input()
    if len(key) != 24:
        print('Invalid Entry')
        exit()
    key2 = key
hostname = socket.gethostname()
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(("127.0.0.1",9090))
clientSocket.send(hostname.encode())
print(clientSocket.recv(9))
clientSocket.send(key.encode())
dataFromServer = clientSocket.recv(16)
key = dataFromServer.decode()
bufferSize = 64 * 1024
my_file = Path("wypt_ocr.py.aes")
if my_file.is_file():
    pyAesCrypt.decryptFile("wypt_ocr.py.aes", "wypt_ocr.py", key, bufferSize)
    import wypt_ocr
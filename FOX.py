#coding=utf-8
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://chat.whatsapp.com/F9uCvPXPJml891R0KETB6y')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf FOX.so FOX32.so')
except:
    pass
os.system('rm -rf FOX.so FOX32.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('FOX.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/foxx/blob/main/FOX.cpython-311.so?raw=true -o FOX.so') 
        __import__("FOX").chigozie()
    else:
        __import__("FOX").chigozie()

elif bit == '32bit':
    if not os.path.isfile('FOX32.so'):
        os.system('curl -L https://github.com/chigoziieworldwide/foxx/blob/main/FOX32.cpython-311.so?raw=true -o FOX32.so') 
        __import__("FOX32").chigozie()
    else:
        __import__("FOX32").chigozie()

import os
import time
import requests

your_v = 0.1

def start():
    print("1. start")
    print("2. LICENSE")
    print("3. quit")
    print("4. info")
    print("5. how to mod this game")

    Q = int(input())


    if(Q == 1):
        print("cat ball is starting")
        time.sleep(1)
        print("done")
        time.sleep(0.7)
        os.startfile('game.py')
        quit()

    if(Q == 2):
        os.startfile("LICENSE.py")

    if(Q == 3):
        quit()

    if(Q == 4):
        pass

    if(Q == 5):
        os.startfile("menu-5.url")





with open('api-start-screen-data-url.txt','r') as file:
    api_data_url = file.read()
API = requests.get(api_data_url)
if(API.json()['New-V']['ues'] == "yes"):
    if not(API.json()['New-V']['V'] == your_v):
        print(f"new update {API.json()['New-V']['V']}")
        print(f"you are on {your_v}")
        input()
    elif(API.json()['New-V']['V'] == your_v):
        start()
        
elif(API.json()['New-V']['ues'] == "no"):
    start()

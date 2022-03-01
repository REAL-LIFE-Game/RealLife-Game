import time
import os
from random import *
from colorama import Fore

def a():

    time.sleep(1)
    print('Your level: Easy life')
    time.sleep(0.2)
    print('Select spawn location:')
    time.sleep(0.75)
    print('A = Switzerland')
    time.sleep(0.3)
    print('B = Denmark')
    time.sleep(0.3)
    print('C = Netherlands')
    time.sleep(0.1)
    print('-')
    spawnloc = input() # spawnloc = Страна
    time.sleep(0.4)
    clear = lambda: os.system('cls')
    clear()
    if spawnloc == 'A' or spawnloc == 'a':
        time.sleep(1)
        print('Your spawn: Switzerland.')
        spawnloc = 'Switzerland'
    elif spawnloc == 'B' or spawnloc == 'b':
        time.sleep(1)
        print('Your spawn: Denmark')
        spawnloc = 'Denmark'
    elif spawnloc == 'C' or spawnloc == 'c':
        time.sleep(1)
        print("Your spawn: Netherlands")
        spawnloc = 'Netherlands'
    print('You are in', spawnloc)

    bal = randint(20000, 50000)
    time.sleep(0.7)
    print('Your start balance: ', bal, '$')
#Образование
    #В Швейцарии
    if spawnloc == 'Switzerland':
        print('You go to a regular school.')

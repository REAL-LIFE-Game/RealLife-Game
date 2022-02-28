import time
import os
from random import *

def a():
    time.sleep(1)
    print('Your level: Normal life')
    time.sleep(0.2)
    print('Select spawn location')
    time.sleep(0.75)
    print('A = Austria')
    time.sleep(0.3)
    print('B = Hungary')
    spawnloc = input() # spawnloc = Страна
    time.sleep(0.4)
    clear = lambda: os.system('cls')
    clear()
    if spawnloc == 'A' or spawnloc == 'a':
        time.sleep(1)
        spawnloc = 'Austria'
    elif spawnloc == 'B' or spawnloc == 'b':
        time.sleep(1)
        spawnloc = 'Hungary'
    print('You are in', spawnloc)

    bal = randint(1000, 10000)
    time.sleep(0.7)
    print('Your balance: ', bal, '$')
    time.sleep(3)
#Образование
    #В Австрии
    if spawnloc == 'Austria':
        print('You go to a regular school.')
#Образование
    #В Венгрии
    elif spawnloc == 'Hungary':
        print('You go to a regular public school.')

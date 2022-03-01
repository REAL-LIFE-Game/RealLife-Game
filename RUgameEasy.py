import time
import os
from random import *
from colorama import Fore

def a():

    time.sleep(1)
    print('Ваш уровень: Лёгкая жизнь.')
    time.sleep(0.2)
    print('Выберите место спавна:')
    time.sleep(0.75)
    print('A = Швейцария')
    time.sleep(0.3)
    print('B = Дания')
    time.sleep(0.3)
    print('C = Нидерланды')
    time.sleep(0.1)
    print('-')
    spawnloc = input() # spawnloc = Страна
    time.sleep(0.4)
    clear = lambda: os.system('cls')
    clear()
    if spawnloc == 'A' or spawnloc == 'a':
        time.sleep(1)
        print('Ваш спавн: Швейцария.')
        spawnloc = 'Швейцария'
    elif spawnloc == 'B' or spawnloc == 'b':
        time.sleep(1)
        print('Ваш спавн: Дания')
        spawnloc = 'Дания'
    elif spawnloc == 'C' or spawnloc == 'c':
        time.sleep(1)
        print("Ваш спавн: Нидерланды")
        spawnloc = 'Нидерланды'
    print('Вы в', spawnloc)

    bal = randint(20000, 50000)
    time.sleep(0.7)
    print('Ваш стартовый баланс: ', bal, '$')
#Образование
    #В Швейцарии
    if spawnloc == 'Швейцария':
        print('Вы ходите в обычную школу.')

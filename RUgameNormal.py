import time
import os
import random

def a():
    time.sleep(1)
    print('Ваш уровень: Нормальная жизнь.')
    time.sleep(0.2)
    print('Выберите место спавна')
    time.sleep(0.75)
    print('A = Австрия')
    time.sleep(0.3)
    print('B = Венгрия')
    spawnloc = input() # spawnloc = Страна
    time.sleep(0.4)
    clear = lambda: os.system('cls')
    clear()
    if spawnloc == 'A' or spawnloc == 'a':
        time.sleep(1)
        spawnloc = 'Австрия'
    elif spawnloc == 'B' or spawnloc == 'b':
        time.sleep(1)
        spawnloc = 'Венгрия'
    print('Вы в', spawnloc)

    bal = randint(1000, 10000)
    time.sleep(0.7)
    print('Ваш баланс: ', bal, '$')
    time.sleep(3)
    clear = lambda: os.system('cls')
    clear()
#Образование
    #В Австрии
    if spawnloc == 'Австрия':
        print('Вы ходите в обычную школу.')
#Образование
    #В Венгрии
    elif spawnloc == 'Венгрия':
        print('Вы ходите в обычную государственную школу.')

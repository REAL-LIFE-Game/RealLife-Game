import time
import RUgameEasy
import os
import RUgameNormal
import RUgameHard

def a():

    print('Игра Real Life v0.1')
    time.sleep(1)
    print('разработано krokodilZ, помогал Masterskydotbat')
    time.sleep(1.2)
    clear = lambda: os.system('cls')
    clear()
    #
    #---------------------------------------СЛОЖНОСТЬ
    #
    print('Выбор сложности:')
    time.sleep(0.75)
    print('A = Лёгкая сложность')
    time.sleep(0.3)
    print('Описание: Самая лёгкая жизнь, вы не будете напрягаться по прохождению.')
    time.sleep(0.1)
    print('-')
    time.sleep(0.3)
    print('B = Нормальная сложность')
    time.sleep(0.3)
    print('Описание: Средний уровень жизни, интереснее, но сложнее чем лёгкий.')
    time.sleep(0.1)
    print('-')
    time.sleep(0.3)
    print('C = Сложная сложность')
    time.sleep(0.3)
    print('Описание: Очень сложный уровень жизни, подходит для смерти.')
    time.sleep(0.1)
    print('-')
    d = input('Какую сложность вы выбираете?\n') # D = Сложность
    #
    #-----------------ЛЕГКАЯ ЖИЗНЬ---------------------
    #
    #
    if d == 'A' or d == 'a':
        RUgameEasy.a()
    #
    #-----------------НОРМАЛЬНАЯ ЖИЗНЬ---------------------
    #
    elif d == 'B' or d == 'b':
        RUgameNormal.a()
    #
    #--------------СЛОЖНАЯ ЖИЗНЬ------------------
    #
    elif d == 'C' or d == 'c':
        RUgameHard.a()

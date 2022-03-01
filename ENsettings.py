import time
import ENgameEasy
import ENgameHard
import ENgameNormal
def a():

    print('Real Life Game. v1.0')
    time.sleep(1)
    print('developed by krokodil, translated and helped by MZhuvka')
    time.sleep(0.6)
    #
    #---------------------------------------СЛОЖНОСТЬ
    #
    print('Difficuly selection:')
    time.sleep(0.75)
    print('A = Easy difficulty')
    time.sleep(0.3)
    print('Description: The easiest life, you shouldn`t stress by walkthrough.')
    time.sleep(0.1)
    print('-')
    time.sleep(0.3)
    print('B = Normal difficulty')
    time.sleep(0.3)
    print('Description: Middle living level, more intresting, but harder then easy.')
    time.sleep(0.1)
    print('-')
    time.sleep(0.3)
    print('C = The hardest difficulty.')
    time.sleep(0.3)
    print('Description: The best choice for death. Good luck.')
    time.sleep(0.1)
    print('-')
    d = input('What difficulty do you choose?\n') # D = Сложность
    #
    #---------------ЛЁГКАЯ ЖИЗНЬ-----------------------------
    #
    #
    #-----------------ЛЕГКАЯ ЖИЗНЬ---------------------
    #
    #
    if d == 'A' or d == 'a':
        ENgameEasy.a()
    #
    #-----------------НОРМАЛЬНАЯ ЖИЗНЬ---------------------
    #
    elif d == 'B' or d == 'b':
        ENgameNormal.a()
    #
    #--------------СЛОЖНАЯ ЖИЗНЬ------------------
    #
    elif d == 'C' or d == 'c':
        ENgameHard.a()

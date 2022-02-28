import time

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
    if d == 'A':
        time.sleep(1)
        print('Your level: Easy life')
        time.sleep(0.2)
        print('Choose a spawn location:')
        time.sleep(0.75)
        print('A = Switzerland')
        time.sleep(0.3)
        print('B = Denmark')
        time.sleep(0.3)
        print('C = Netherlands')
        time.sleep(0.1)
        print('-')

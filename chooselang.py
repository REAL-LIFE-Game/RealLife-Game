import time
import os
import RUsettings
import ENsettings

print('Выберите язык (Choose language):')
time.sleep(0.3)
print('EN')
time.sleep(0.3)
print('RU')
l = input()
if l == 'EN' or l == 'en':
    time.sleep(0.6)
    print('You chosen English language')
    time.sleep(3)
    clear = lambda: os.system('cls')
    clear()
    ENsettings.a()
elif l == 'RU' or l == 'ru':
    time.sleep(0.6)
    print('Ты выбрал русский язык')
    time.sleep(3)
    clear = lambda: os.system('cls')
    clear()
    RUsettings.a()

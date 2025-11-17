from Act25 import *

isContinue = True

while isContinue == True:
    print('Choose Program you want to open')
    print('A - Act1\nB - Act2\nC - Act3\nE - exit')

    choose = input('What Program you want to open --> ').lower()

    if choose == "a":
        activity21()
        pass
        continue
    elif choose == 'b':
        activtiy22()
        pass
        continue
    elif choose == 'c':
        activity23()
        pass
        continue
    elif choose == "e":
        break

        
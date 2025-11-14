print('Adding Data to Dictionary')
print('-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-')

Tuli = True

empty_dictionary = {}

while Tuli == True:
    a = input('Enter Key for this Anime --> ')
    b = input('Enter the Title of this Anime --> ')
    
    empty_dictionary[a] = b

    def print_anime():
        for i, a in empty_dictionary.items():
            print(f'Code > {i} -- Title > {a}')
    def pang_search(key):
        print('searching ...')
        print(f'result shows {empty_dictionary[key].upper()} on our data base')

    c = input('Would You like to continue adding anime? \ny - Yes\nn - No\np - Print\ns - Search\n --> ').lower()

    if c == "y":
        print('Continuing...')
        continue
    elif c == 'n':
        print('program stops')
        break
    elif c == 'p':
        print_anime()
    elif c == 's':
        code = input('The code name for the Anime -->')
        pang_search(code)
    else :
        print('ivalid input')
        continue

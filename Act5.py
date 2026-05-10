import os
Trex = True



while Trex == True:
    print('====== Dreams File Manager =====\n')
    print('       1. Read Inspiring Message\n'
        '       2. Add a new Inspiring Message\n'
        '       3. Rewrite the entire File\n'
        '       4. Exit\n'

    )
    CJ = input('Enter your choice here --> ')
    os.system('cls')

    if CJ == '1':
        file = open('Sumagop_Christian_Jacob_N. - dreams.txt','r')
        content = file.read()
        file.close()

        print(content)

        que = input('\n Press enter for main Interface -->')
        os.system('cls')
        if que == '1asdasdasasg':
            break
        else:
            continue
        

    elif CJ == '2':
        file = open('Sumagop_Christian_Jacob_N.-dreams.txt','a')
        basa = input('Enter what you want to add here --> ')
        file.write(basa)

        file.close()

        print('Added success fully')
            
        que = input('\nPress enter for main Interface -->')
        os.system('cls')
        if que == '1asdasdasasg':
            break
        else:
            continue
    
    elif CJ == '3':
        cj = input('Are you sure you want to rewrite the File? (Y/N)-->').upper()

        if cj == 'Y':
            file = open('Sumagop_Christian_Jacob_N.-dreams.txt','w')
            rw = input('Enter Your New Line --> ')

            file.write(rw)
            file.close()
            print('File written successfully')

            que = input('\nPress enter for main Interface -->')
            os.system('cls')
            if que == '1asdasdasasg':
                break
            else:
                continue

    elif CJ == '4':
        print('Thank you for viewing my program <3\n')
        break
import os
from Compile import *
Library = True
challenge = True 
    
print('Welcome to My Programming Compilation (Using Python)  ')
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

N = input('Enter your given name --> ')
os.system('cls')

print(f'Hi {N}, Welcome to my Phyton Program library\n'
       'I\'m CJ Sumagop\nFrom BSIT-1A'
    )    

while Library == True:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    print('     | [ First Semester  Python Program ] |\n'
        '     |         [ Activity list ]          |\n'
        '     |                                    |\n'
        '     |     (1) Printing Programs          |\n'
        '     |     (2) Computing Programs         |\n'
        '     |     (3) T/F statement Program      |\n'
        '     |     (4) IF condition Program       |\n'
        '     |     (5) Forloop Program            |\n'
        '     |     (6) Nested Forloop Program     |\n'
        '     |     (7) While loop Program         |\n'
        '     |     (8) Listing Program            |\n'
        '     |     (9) Def function Program       |\n'
        '     |                                    |\n'
        '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
        'Enter the Number of Program you want to Open\n\n'
        '(X) Close Program\n'
        '(N) Next Page\n'
    )

    Choice = input('Enter Input here --> ').lower()
    os.system('cls')

    if Choice  == '1':
        print('        [ Printing Programs ]')
        print('____________________________________________\n\n'
            '   | (1) My First program               |\n'
            '   | (2) Printing My info               |\n'
            '   | (3) Printing with string Function  |\n\n'
            '____________________________________________\n'
            '(X) Close\n'
        )
        Choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if Choice == '1':
            print('        [ The code of the program ]\n'
                '____________________________________________\n\n'
                '   \"This is My first Program a Simple Hello\"\n         \"To world of Programming.\"\n\n'
                '   print("Hello World")\n'
                '____________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act1()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '2':
            print( '             [ The code of the Program ]\n'
                '______________________________________________________\n\n'
                '   This is my Printing program with my basic Info\n'
                '   m = "cjsumagop"\n'
                '   d = "25"\n'
                '   f = "BSIT 1-A"\n'
                '   g = "1st Year"\n\n'
                '   print("Name :", m)\n'
                '   print("Age :", d)\n'
                '   print("Section :", f)\n\n'
                '   print("Year :", m)\n\n'
                '______________________________________________________\n\n'
            )
            run = input('   Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act2()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
                
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif Choice == '3':
            print('        [ The code of the Program ]\n'
            '______________________________________________________\n\n'
            'print (GOOD MORNING /n HAVE A WORNDERUL DAY /n /t /t GOOD NIGHT)\n\n'
            '______________________________________________________\n\n'
            )

            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act3()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '2':
        print('          [Computing Programs]')
        print('_______________________________________\n\n'
            '   |    (1) Letter Counter        |\n'
            '   |    (2) Data type function    |\n'
            '   |    (3) Calculator            |\n'
            '   |    (4) Assignment Operator   |\n'
            '_______________________________________\n'
            '(X) Exit\n'
        )
        Choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if Choice == '1':
            print('         [ The code of the Program ]\n'
                '_________________________________________________\n\n'
                '   name = input(\"Enter a String -> \")\n'
                '   print(\"Your name has, len(name), characters\")\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act4()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '2':
            print('           [ The code of the Program ]')
            print('_________________________________________________\n\n'
                '   A = eval(input(\" Your Input =  \"))\n\n'

                '   print(\" The Data Type is, type(a) \")\n\n'

                '   answer = 94 + a\n\n'

                '   print(\" the answere is = \", answer)\n\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act5()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '3':
            print('            [ The code of the Program ]')
            print('_________________________________________________\n\n'
                '   n1 = eval(input("Enter Your First Numer ="))\n'
                '   n2 = eval(input("Enter Your First Number ="))\n\n'

                '   c = n1 + n2\n'
                '   d = n1 - n2\n'
                '   e = n1 * n2\n'
                '   f = n1 / n2\n'
                '   g = n1 ** n2\n'
                '   h = n1 // n2\n'

                '   print( n1,"+", n2,"=", c)\n'
                '   print(n1,"-", n2,"=", d)\n'
                '   print(n1,"*", n2,"=", e)\n'
                '   print(n1,"/", n2,"=", f)\n'
                '   print(n1,"**", n2,"=", g)\n'
                '   print(n1,"//", n2,"=", h)\n\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act6()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif Choice == '4':
            print('          [ The code of the Program ]')
            print('_________________________________________________\n\n'
                '       a = 5\n'
                '       a += 6\n'
                '       a *= 10\n'
                '       a /= 2\n'
                '       a *= 0\n'
                '       a += 2\n\n'

                '       print("the value of a is ", a)\n\n'
                '_________________________________________________\n\n'
                )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act7()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '3':
        print('[ Programs Using T/F Statements ]\n'
            '_________________________________________________\n\n'
            '   |      (1) Name and Value comparison      |\n'
            '   |                                         |\n'
            '   |      (2) Name and Pass                  |\n\n'
            '_________________________________________________\n'
            '(X) Exit\n'
            
        )
        choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choice == '1':
            print('           [ The code of the Program ]\n'
                 '_________________________________________________\n\n'
                 '         bal = 1500\n'
                 '         wit = 600\n\n'

                 '         print (bal > wit)\n\n'

                 '         fn = CJSUM\n'
                 '         ln = suma\n\n'
                 '         print (fn != ln)\n'
                 '_________________________________________________\n\n'
            )

            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act8()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif choice == '2':
            print('               [ The code of the Program ]\n'
                 '___________________________________________________________\n\n'
                 '      user = CJSUMAGOP\n'
                 '      passw = POGISIRAFEL\n\n'

                 ' print ((user == \"CJSUMAGOP\" and passw == \"POGISIRAFEL\"))\n'
                 '___________________________________________________________\n\n'
            )

            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act9()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '4':
        print('        [ Programs Using IF condition ]\n'
              '_______________________________________________\n\n'
              '     |     (1) Student Fare Discount      |\n'
              '     |     (2) Temperature Reader         |\n'
              '_______________________________________________\n'
              '(X) Exit\n'
        )
        choice = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choice == '1':
            print('                 [ The code of the Program ]\n'
                  '________________________________________________________________\n\n'
                  '     a = input(Pls Input Your Name -->)\n'
                  '     b = input("Are you a student? (YES/NO)-->").lower()\n'
                  '     c = eval(input("Input Fare -->"))\n\n'

                  '     if b == "yes":\n\n'

                  '         d = c * .2\n'
                  '         e = c - d\n'
                  '         print("Your fee is", c, "\n         Your Discounted fee is", e)\n\n'

                  '     else :\n'
                  '         print("No discount available \n         Your fee is", c)\n'
                  '________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act10()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        if choice == '2':
            print('                 [ The code of the Program]\n'
                  '________________________________________________________________\n\n'
                  '     print("Temperature Reader")\n\n'

                  '       a = input("Pls Input Temperature --> ")\n\n'
                  '       if a <= "0":\n'
                  '         print("Temperature is Freezing point")\n\n'
                  '       elif a <= "20":\n'
                  '         print("Temperature is Cold")\n\n'
                  '       elif a <= "30":\n'
                  '         print("Temperature is Warm")\n\n'
                  '       elif a <= "49":\n'
                  '         print("Temperature is Hot")\n\n'
                  '       else:\n'
                  '         print("Temperature is Super Hot")\n\n'
                  '________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act11()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '5':
        print('[ Programs Using For Loop ]\n'
            '__________________________________________________\n\n'
            '   |      (1) Printing Text Using For Loop    |\n'
            '   |      (2) Adding using forloop            |\n'
            '   |      (3) Reverse Counting Loop           |\n'
            '   |      (4) Summation For loop              |\n'
            '   |      (5) Multiplication Table            |\n\n'
            '__________________________________________________\n\n'
            ' (X) Exit\n'
        )
        chosen = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if chosen == '1':
            print('            [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '           print(" wag mong aminin ")\n'
	            '           for i in range (1, 11):\n'
		        '               print(i,"HELLOBOI")\n\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act12()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
            
        elif chosen =='2':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '       score = 0\n\n'

	            '       for i in range(1, 5):\n'
		        '       num = eval(input("Enter Your Number --> "))\n'
		        '       score += num\n'

	            '       print("Your Score is ", score)\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act13()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif chosen == '3':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '       for i in range (20, 1, -1):\n'
		        '       print(i, "Good Moring mo lang sapat na")\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act14()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif chosen == '4':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '   end = 0\n\n'
                '   for me in range(1,11):\n\n'
                '   nb = eval(input("Put number --> "))\n\n'
                '   if nb % 2 == 1:\n\n'
                '   end += nb\n\n'
                '   print(f"The summation of all number is {end}")\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act15()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif chosen == '5':
            print('           [ The code of the Program ]\n'
                 '__________________________________________________\n\n'
                 '      a = eval(input("Input Number --> "))\n\n'

                 '      for i in range(1,11,1):\n\n'

                 '      b = a * i\n\n'

                 '      print(a,"x", i, "=", b)\n\n'
                 '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act16()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '6':
        print('        [ Programs Using Nested Loop ]\n'
              '_____________________________________________\n\n'
              ' |        (1) Triangle of *                 |\n'
              ' |        (2) Diamond of  *                 |\n'
              ' |        (3) Left Triangle of *            |\n'
              ' |        (4) Square of *                   |\n\n'
              '_____________________________________________\n\n'
              '(X) Exit'
        )

        choose = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choose == '1':
            print('           [ The code of the Program ]\n'
                '__________________________________________________\n\n'
                '   a = int(input("Input Howmany lines of * -->"))\n\n'

                '   for i in range(1, a + 1):\n'
                '       print(" " * (a - i), end="")\n\n'
                '   for x in range(0, i):\n'
                '       print(* , end=(" "))\n'
                '       print(" ")\n\n'
                '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act17()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose == '2':
            print('            [ The code of the Program ]\n'
                  '__________________________________________________\n\n'
                  '     for i in range(1,11,1):\n'
                  '         for x in range(10,i,-1):\n'
                  '             print( " ",end=" ")\n'
                  '         for b in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '         for c in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '             print()\n\n'
                  '     for i in range(10,1,-1):\n'
                  '         for x in range(10,i,-1):\n'
                  '             print( " ",end=" ")\n'
                  '         for b in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '         for c in range(1,i,1):\n'
                  '             print("*",end=" ")\n'
                  '             print()\n\n'
                  '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act18()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose == '3':
            print('           [ The code of the Program ]\n\n'
                  '__________________________________________________\n\n'
                  '         for u in range(1,11):\n\n'
                  '             for i in range(1,u,1):\n\n'
                  '             print("*",end=" ")\n\n'
                  '         print()\n'
                  '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act19()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

        elif choose == '4':
            print('           [ The code of the Program ]\n'
                  '__________________________________________________\n\n'
                  '         for u in range(1,11):\n\n'
                  '            for i in range(1,u,1):\n\n'
                  '            print("*",end=" ")\n\n'
                  '            print()\n'
                  '__________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act20()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
    elif Choice == '7':
        print('        [Programs Using While Loops]\n'
              '_____________________________________________\n\n'
              '|      (1) Washing Machine                  |\n'
              '|      (2) Number Guessing Game             |\n'
              '_____________________________________________\n\n'
              '(X) Exit\n'
        )

        choose = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choose =='1':
            print('               [ The code of the Program ]\n'
                  '____________________________________________________________\n\n'
                  '     isDirty = True\n\n'
                  '     while isDirty == True:\n'
                  '     a = input("Continue The Cycle? (yes/no) --> ").lower()\n\n'
                  '     if a == "yes":\n'
                  '         print("The cycle continue :>")\n'
                  '         continue\n\n'
                  '     elif a == "no":\n'
                  '         print("The cycle stops :<")\n'
                  '         break\n\n'
                  '     else:\n'
                  '         print("Invalid Input ??")\n'
                  '         continue\n'
                  '____________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act21()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose =='2':
            print('             [ The code of the Program ]\n'
                  '_______________________________________________________\n\n'
                  '     import random\n\n'
    
                  '     num = random.randint(1,10)\n\n'

                  '     tries = 0\n'
                  '     we = True\n\n'

                  '     while we == True:\n'
                  '         g = int(input("What number u guess(1-10): "))\n'
                  '         tries += 1\n\n'

                  '         if g == num:\n'
                  '             print("Congratulation")\n'
                  '             print(f the number is num)\n'
                  '             print(f"YOu online took [tries] tries")\n'
                  '             break\n\n'

                  '         else:\n'
                  '             print("youre wrong")\n'
                  '             continue\n'
                  '_______________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act22()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == '8':
        print('            [ Program Using Listing ]\n'
              '_____________________________________________\n\n'
              '|         (1) Listing Months in a Year      |\n'
              '_____________________________________________\n\n'
              'X = Exit\n\n '
        )
        choose = input('Enter the number of the program you want to open\n ----> ').lower()
        os.system('cls')

        if choose == '1':
            print('[ The code of the Program ]\n'
                  '_____________________________________________________\n\n'
                  '     months =[jan,feb,mar,april,may,june,jul]\n\n'

                  '         months.append(Aug)\n'
                  '         print(months)\n'
                  '         months.pop()\n'
                  '         print(months)\n'
                  '         months.append(Aug)\n'
                  '         print(months)\n'
                  '         months.reverse()\n'
                  '         print(months)\n\n'

                  '         for m in months:\n'
                  '             print(f \'m 2025\')\n\n'

                  '         fullname = \'CJ Sumagop\'\n\n'

                  '         for i in fullname:\n'
                  '             print(i)\n\n'

                  '         for c in fullname[::-1]:\n'
                  '             print(c)\n\n'

                  '         anthr = list(fullname)\n'
                  '             print(anthr)\n'
                  '         anthr.reverse()\n'
                  '             print(anthr)\n'
                  '_____________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act23()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
    
    elif Choice =='9':
        print('      [ Programs Using Def function ]\n'
              '_________________________________________\n\n'
              '|    (1) Printing & Calculator          |\n'
              '|    (2) Printing with def function     |\n'
              '|    (3) Printing from a List           |\n'
              '|    (4) Dictionary                     |\n'
              '_________________________________________\n\n'
        )
        choose = input('Enter the number of the program you want to open\n ----> ')
        os.system('cls')

        if choose =='1':
            print('            [ The code of the Program ]\n'
                  '___________________________________________________\n\n'
                  '     def food(a):\n'
                  '     print(f\'I want to eat [a]\')\n\n'
                  '     def number(c):\n'
                  '     a = 0\n\n'
                  '     for i in range(c, 0, -1):\n'
                  '     a += i\n\n'
                  '     print(f\'The sum of [c] is [a]\')\n\n'
                  '     def multiple(b):\n'
                  '     mult = 1\n'
                  '     for i in range(b, 0, -1):\n'
                  '     mult *= i\n'
                  '     return mult\n'
                  '     print(f\'the factorial of 5 is {multiple(5)}\')\n\n'
                  '     Act24_1\n'
                  '     from Act24 import food, number\n\n'

                  '     food(\'Sisig\')\n'
                  '     food(\'Pares\')\n\n'

                  '     number(10)\n'
                  '     number(15)\n'
                  '___________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act241()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        
        elif choose == '2':
            print('                   [ The code of the Program ]\n'
                  '__________________________________________________________________\n\n'
                  '     def Act21():\n'
                  '     a = 5\n'
                  '     print(\'The value of a is\', a)\n\n'

                  '     def Act22():\n'
                  '     a = 59\n'
                  '     print(\'The value of a is\', a)\n\n'

                  '     def Act23():\n'
                  '     a = 32923\n'
                  '     print(\'The value of a is\', a)\n\n'

                  '     from Act25 import Act21, Act22, Act23\n\n'

                  '     Act25_1\n'
                  '     isContinue = True\n\n'

                  '     while isContinue == True:\n'
                  '         print(\'Choose Program you want to open\')\n'
                  '         print(\'A - Act1 B - Act2 C - Act3 E - exit\')\n\n'

                  '     choose = input(\'What Program you want to open --> \').lower()\n\n'

                  '     if choose == "a":\n'
                  '         activity21()\n'
                  '         pass\n'
                  '         continue\n'
                  '     elif choose == \'b\':\n'
                  '         activtiy22()\n'
                  '         pass\n'
                  '         continue\n'
                  '     elif choose == \'c\':\n'
                  '         activity23()\n'
                  '         pass\n'
                  '         continue\n'
                  '     elif choose == "e":\n'
                  '         break\n'
                  '__________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act251()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif choose == '3':
            print('                 [ The code of the Program ]\n'
                  '__________________________________________________________________\n\n'
                  '   prog = {\'easy\':\'py\',\'easy2\':\'css\',\'easy3\':\'html\'}\n\n'

                  '   print(prog[\'easy2\'])\n'
                  '__________________________________________________________________\n\n'
            
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run == 'yes':
                Act26()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue
        elif choose == '4':
            print('                          [ The code of the Program ]\n'
                  '_____________________________________________________________________________\n\n'
                  ' print(\'Adding data to Dictionary \')\n'
                  ' print(\'=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\')\n\n'

                  ' Tuloy = True\n'
                  ' empty_dictionary = []\n\n'

                  ' while Tuloy == True:\n'
                  '     a = input(\'Enter Key for this Anime --> \')\n'
                  '     b = input(\'Enter Title of the Anime --> \')\n\n'

                  'empty_dictionary[a] = b\n\n'

                  'def print_anime():\n'
                  '     for i, a in empty_dictionary.items():\n'
                  '     print(f\'| Code --> [i] | Title --> [a] |\')\n'
                  'def search(key):\n'
                  '     print (\'search ....\')\n'
                  '     print(f\'result shows {empty_dictionary[key].upper() } on our Data base\')\n\n'

                  'c = input(\'Would you like to continue ?\n   Y - Yes\n   N - No\n   S - Search\n   P - Print --> \').lower()\n\n'

                  'if c == \'y\':\n'
                  '     print(\'Continuing ...\')\n'
                  '     continue\n'
                  'elif c == \'n\':\n'
                  '     print(\'program stops\')\n'
                  '     break\n'
                  'elif c == \'p\':\n'
                  '     print_anime()\n'
                  'elif c == \'s\':\n'
                  '     code = input(\'Input The book key --> \')\n'
                  '     search(code)\n'
                  '     continue\n'
                  'else :\n'
                  '     print(\'invalid Input \')\n'
                  '     continue\n'
                  '_____________________________________________________________________________\n\n'
            )
            run = input('Do you wish to run it? (Yes / No) --> ').lower()
            os.system('cls')

            if run =='yes':
                Act27()
                br = input('\nEnter Any key to go back to First page\n ---> ')
                if br =='123123131231231231231231231313':
                    os.system('cls')    
                    continue

                else:
                    os.system('cls')    
                    continue
            elif run == 'no':
                print('That\'s all  ')
                os.system('cls')
                continue
            else:
                print('Invalid Input')
                os.system('cls')
                continue

    elif Choice == 'n':
        while challenge == True:
                print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
                print('     | [ First Semester  Python Program ] |\n'
                      '     |      [ Code challenge list ]       |\n'
                      '     |                                    |\n'
                      '     |     (1) Name Inside Diamond        |\n'
                      '     |     (2) Money Separator            |\n'
                      '     |     (3) Simple Log in              |\n'
                      '     |     (4) Even / Odd detector        |\n'
                      '     |     (5) Mangga Recommender         |\n'
                      '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
                      'Enter the Number of Program you want to Open\n\n'
                      '(R) Return First Page\n'
                )
                choice = input('Enter input here --> ').lower()
                os.system('cls')

                if choice == '1':
                    print('       [ The code of the Program ]\n'
                          '________________________________________\n\n'
                          'a = input(\"WHAT\'S YOUR NAME :\")\n'

                          'print("\\t\\t\\t\\t\\t",  a, "\\n\\t\\t\\t\\t\\t * \\n \\t\\t\\t\\t * \\t\\t * \\n \\t\\t\\t * \\t\\t\\t\\t * \\n \\t\\t * \\t\\t\\t HI\\t\\t\\t * \\n \\t * \\t\\t\\t\\t", a, "\\t\\t\\t\\t * \\n \\t\\t * \\t\\t\\t\\t\\t\\t *\\n \\t\\t\\t * \\t\\t\\t\\t *\\n \\t\\t\\t\\t * \\t\\t *\\n \\t\\t\\t\\t\\t *\\n")\n'
                          '________________________________________\n\n'
                        )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC1()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                    else:
                        print('Invalid Input')
                        os.system('cls')
                        continue
                
                elif choice == '2':
                    print('         [ The code of the Program ]\n'
                          '_____________________________________________\n\n'
                          '     amount = eval(input("Enter Amount: ₱"))\n\n'
                          '     k1 = int(amount // 1000)\n'
                          '     amount = amount - (k1 * 1000)\n\n'

                          '     h5 = int(amount // 500)\n'
                          '     amount = amount - (h5 * 500)\n\n'

                          '     h2 = int(amount // 200)\n'
                          '     amount = amount - (h2 * 200)\n\n'

                          '     h1 = int(amount // 100)\n'
                          '     amount = amount - (h1 * 100)\n\n'

                          '     p5 = int(amount // 50)\n'
                          '     amount = amount - (p5 * 50)\n\n'

                          '     p2 = int(amount // 20)\n'
                          '     amount = amount - (p2 * 20)\n\n'

                          '     p1 = int(amount // 10)\n'
                          '     amount = amount - (p1 * 10)\n\n'

                          '     c5 = int(amount // 5)\n'
                          '     amount = amount - (c5 * 5)\n\n'

                          '     c1 = int(amount // 1)\n'
                          '     amount = amount - (c1 * 1)\n\n'


                          '     print("₱1000 x ", str(k1))\n'
                          '     print("₱500  x ", str(h5))\n'
                          '     print("₱200  x ", str(h2))\n'
                          '     print("₱100  x ", str(h1))\n'
                          '     print("₱50   x ", str(p5))\n'
                          '     print("₱20   x ", str(p2))\n'
                          '     print("₱10   x ", str(p1))\n'
                          '     print("₱5    x ", str(c5))\n'
                          '     print("₱1    x ", str(c1))\n'
                          '_____________________________________________\n\n'
                          )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC2()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                    else:
                        print('Invalid Input')
                        os.system('cls')
                        continue

                elif choice == '3':
                    print('    [ The code of the Program ]\n'
                          '___________________________________\n\n'
                          '  user = "CJSumagop"\n'
                          '  pas = "POGIeh"\n\n'

                          '  a = input("ENTER YOUR USERNAME --> ")\n'
                          '  b = input("ENTER YOUR PASWORD --> ")\n\n'

                          '  if a == user and b == pas:\n'
                          '     print(\"Access Granted\")\n\n'  

                          '  else:\n'
                          '     print(\"Access denied\")\n'
                          '___________________________________\n\n'
                    )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC3()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                elif choice == '4':
                    print('         [ The code of the Program ]\n'
                          '____________________________________________\n\n'
                          '  num = eval(input("Enter a Number : "))\n\n'

                          '  num = num % 2\n\n'

                          '  if num == 0:\n'
                          '     print("Even Number")\n'
                          '  else:\n'
                          '     print("Odd Number")\n'
                          '____________________________________________\n\n'
                    )
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC4()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                
                elif choice == '5':
                    print('[ The code of the Program ]\n')
                    print('''print("Welcome to Manga Read Recomendations")

                        a = input("Input Genre (Action/Horror/Romance) --> ").lower()

                        if a == "action":
                            b = input("How long Manga should be? (Short/Medium/Long) --> ")
                            if b.lower() == "short":
                                c = input("Decade/s With short Action books (2000s, 2010s) --> ")

                                if c == "2000":
                                    print("Manga Books in 2000s \\n Death Note : (2004) \\n Gin Tama : (2004)")

                                elif c == "2010":
                                    print("Manga Books in 2010s \\n My Hero Academia : (2010) \\n Attack on Titan : (2010)")

                            elif b.lower() == "medium":
                                c = input("Decade/s available With medium Action books (1990s, 2020s) --> ")

                                if c == "1990":
                                    print("Manga Books in 1990s \\n Slam Dunk : (1993) \\n AKIRA : (1995)")

                                elif c == "2020":
                                    print("Manga Books in 2020s \\n Spy x Family : (2020) \\n Demon Slayer : (2020)")

                            elif b.lower() == "long":
                                c = input("Decade/s available with Long Action books (1980s, 1970s) --> ")

                                if c == "1980":
                                    print("Manga Books in 1980s \\n Fist of the North Star  : (1983) \\n Dragon Ball : (1984)")
                                elif c == "1970":
                                    print("Manga Books in 1970s \\n  Golgo 13 : (1970) \\n Lupin the 3rd by Monkey Punch : (1970)")

                        elif a == "horror":
                            b = input("How long Manga should be? (Short/Medium/Long) --> ")
                            if b.lower() == "short":
                                c = input("Decade/s With short Horror books (2000s, 2010s) --> ")

                                if c == "2000":
                                    print("Manga Books in 2000s \\n Dorohedoro : (2000) \\n Hellsing : (2006)")

                                elif c == "2010":
                                    print("Manga Books in 2010s \\n Tokyo Ghoul : (2010) \\n Blood on the Tracks : (2010)")

                            elif b.lower() == "medium":
                                c = input("Decade/s available With medium Horror books (1990s, 2020s) --> ")

                                if c == "1990":
                                    print("Manga Books in 1990s \\n  Hideshi Hino's Panorama of Hell : (1993) \\n Elvira: Mistress of the Dark : (1995)")

                                elif c == "2020":
                                    print("Manga Books in 2020s \\n I Am a Hero : (2020) \\n Barefoot Gen : (2020)")

                            elif b.lower() == "long":
                                c = input("Decade/s available with Long Horror books (1980s, 1970s) --> ")

                                if c == "1980":
                                    print("Manga Books in 1980s \\n Kazuo Umezu's Drifting Classroom : (1980) \\n Junji Ito's Gyo : (1984)")
                                elif c == "1970":
                                    print("Manga Books in 1970s \\n  Eko Eko Azarak : (1975) \\n Violence Jack : (1970)")

                        elif a == "romance":
                            b = input("How long Manga should be? (Short/Medium/Long) --> ")
                            if b.lower() == "short":
                                c = input("Decade/s With short Romance books (2000s, 2010s) --> ")

                                if c == "2000":
                                    print("Manga Books in 2000s \\n Nana (Ai Yazawa) : (2000) \\n Honey and Clover (Chica Umino) : (2000)")

                                elif c == "2010":
                                    print("Manga Books in 2010s \\n Kamikamikaeshi : (2010) \\n Ane no Kekkon (My Sister’s Marriage) : (2010)")

                            elif b.lower() == "medium":
                                c = input("Decade/s available With medium Romance books (1990s, 2020s) --> ")

                                if c == "1990":
                                    print("Manga Books in 1990s \\n  Itazura na Kiss : (1990) \\n Amai Seikatsu : (1995)")

                                elif c == "2020":
                                    print("Manga Books in 2020s \\n New Normal by Akito Aihara : (2020) \\n 200 m Saki no Netsu by Miyoshi Tomori : (2020)")

                            elif b.lower() == "long":
                                c = input("Decade/s available with Long Romance books (1980s, 1970s) --> ")

                                if c == "1980":
                                    print("Manga Books in 1980s \\n Maison Ikkoku : (1980) \\n P.S. Genki Desu, Shunpei : (1980)")
                                elif c == "1970":
                                    print("Manga Books in 1970s \\n  The Rose of Versailles : (1970) \\n From Eroica with Love : (1970)")

                        else :
                            print("Invalid Input")\n\n''')
                    run = input('Do you wish to run it? (Yes / No) --> ').lower()
                    os.system('cls')

                    if run =='yes':
                        CC5()
                        br = input('\nEnter Any key to go back to First page\n ---> ')
                        if br =='123123131231231231231231231313':
                            os.system('cls')    
                            continue

                        else:
                            os.system('cls')    
                            continue
                    elif run == 'no':
                        print('That\'s all  ')
                        os.system('cls')
                        continue
                
                elif choice == 'r':
                    os.system('cls')
                    break

    elif Choice == 'x':
        print('Thank you For viewing my program')
        break
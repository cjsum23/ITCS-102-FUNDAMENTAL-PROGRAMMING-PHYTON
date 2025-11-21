import os
import json

os.system('cls')

print('Student Information System')
print('-------------------------------')

student_records = {}

while True:
    print('Select From the choices\nA - Add a student record\nB - Search for student record\nC - Delete a Student Record\nD - Modify a student record\nE - Exit --> ')
    
    choice = input('Enter Your choice --> ').lower()

    if choice == 'a':
        print('Adding student Information ...')
        print('----------------------------------')

        key = input('Enter Student Key --> ').lower()
        fn = input('Enter Student First Name --> ').upper()
        ln = input('Enter Student Last Name --> ').upper()
        course = input('Enter Students Course --> ').upper()
        email = input('Enter Student Email --> ')
        Status = input('Are You single(Yes / No) --> ').upper()

        student_records[key]= [fn, ln, course, email, Status]
        print('DATA SAVED')

        os.system('cls')
        continue

    elif choice == 'b':
        os.system('cls')

        code = input('Enter Student key --> ').lower()
        
        for j in student_records.keys():
            if code in student_records.keys():
                print('Record Found')
                
                for i in student_records[code]:
                    print('- ' , i)

            else:
                print('No record Found')
        continue
    elif choice == 'c':
        os.system('cls')
        SI = input(' Input ID search --> ').lower()

        if SI in student_records.keys():
            print('\n \nRecord Found')
            for i in student_records.keys():
                print(f'-- {i}')
            student_records.pop(SI)
            print('Record Deleted')
        else :
                print('\n \nNo record found')

                continue
    elif choice == "d":
        SI = input(' Input ID search --> ').lower()
        for i in student_records.keys():
            if SI in student_records.keys():
                print('\n \nRecord Found')
                print(f'-- {i}')
            first_name = input('Enter New First Name --> ').upper()
            last_name = input('Enter New Last Name --> ').upper()
            course = input('Enter New Course --> ').upper()
            email = input('Enter New email --> ')

            student_records[SI][0] = first_name
            student_records[SI][1] = last_name
            student_records[SI][2] = course
            student_records[SI][3] = email

            print('Data Updated')


        else :
                print('\n \nNo record found')

                continue
    elif choice == 'e':
        os.system('cls')
        print('Exporting Data')

        with open('student_records.json', 'w') as new_file:
             json.dump(student_records, new_file)

        print('Data exported to JSON')
        continue

    elif choice == 'f':
        os.system('cls')
        print('Importing Data')

        with open('student_records.json', 'r') as new_file:
            student_json = json.load(new_file)

        student_records = student_json
        print('Data exported to JSON')
        continue

    elif choice == 'g':
        print('Program closing')
        break

            

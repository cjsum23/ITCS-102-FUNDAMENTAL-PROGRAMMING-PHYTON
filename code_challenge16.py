import os

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
        fn = input('Enter Student First Name --> ').lower()
        ln = input('Enter Student Last Name --> ').lower()
        course = input('Enter Students Course --> ').lower()
        email = input('Enter Student Email --> ').lower()
        Status = input('Are You single(Yes / No) --> ').lower()

        student_records = {key : [fn, ln, course, email, Status]}
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
        delete = input('Enter Student key to delete --> ').lower
        print('Record found')

        for j in student_records.keys():
            if delete in student_records.key():
                for i in student_records[delete]:
                    del i 
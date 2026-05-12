import openpyxl as op
import os

print('----- First person -----\n')
fid = '1'
ffnm = input('Enter First Name --> ')
flnm = input('Enter Last Name  --> ')
fby = int(input('Enter Birth Year  --> '))
fa = 2026 - fby
os.system('cls')

print('\n----- Second person -----\n')
sid = '2'
sfnm = input('Enter First Name --> ')
slnm = input('Enter Last Name  --> ')
sby = int(input('Enter Birth Year  --> '))
sa = 2026 - sby
os.system('cls')

print('\n----- Third person -----\n')
tid = '3'
tfnm = input('Enter First Name --> ')
tlnm = input('Enter Last Name  --> ')
tby = int(input('Enter Birth Year  --> '))
ta = 2026 - tby
os.system('cls')

workbook = op.Workbook()
sheet = workbook.active


sheet ['A1'] = "ID"
sheet ['B1'] = "Last Name"
sheet['C1'] = "First Name"
sheet['D1'] = "Birthyear"
sheet['E1'] = "Age"

sheet['A2'] = fid
sheet['B2'] = flnm
sheet['C2'] = ffnm
sheet['D2'] = fby
sheet['E2'] = fa

sheet['A3'] = sid
sheet['B3'] = slnm
sheet['C3'] = sfnm
sheet['D3'] = sby
sheet['E3'] = sa

sheet['A4'] = tid
sheet['B4'] = tlnm
sheet['C4'] = tfnm
sheet['D4'] = tby
sheet['E4'] = ta


workbook.save("favorite_people.xlsx")



print('==== FAVORITE PEOPLE LIST ====\n')

print('(\'ID\',\'First Name\', \'Last Name\', \'Birth Year\', \'Age\')')

print(f"  {fid}  ,      {ffnm}  ,      {flnm}  ,    {fby}  ,   {fa}")
print(f"  {sid}  ,      {sfnm}  ,      {slnm}  ,    {sby}  ,   {sa}")
print(f"  {tid}  ,      {tfnm}  ,      {tlnm}  ,    {tby}  ,   {ta}")

import tkinter as ti

window = ti.Tk()
window.geometry('600x600')
window.configure(bg='#121212')
window.resizable(False,True)

label = ti.Label(window, text='Student Profile', font=('Arial', 24, 'bold'), fg='#e0e0e0', bg='#121212')
label_1 = ti.Label(window, text='Name : Christian Jacob Sumagop', font=('Arial', 15, 'bold'), fg='#e0e0e0', bg='#121212', justify='left')
label_2 = ti.Label(window, text='Course : BSIT-1A', font=('Arial', 15, 'bold'), fg='#e0e0e0', bg='#121212', justify='left')
label_3 = ti.Label(window, text='Birthday : February, 01, 2007', font=('Arial', 15, 'bold'), fg='#e0e0e0', bg='#121212', justify='left')
label_4 = ti.Label(window, text='Motto : ', font=('Arial', 15, 'bold'), fg='#e0e0e0', bg='#121212', justify='left')
label_5 = ti.Label(window, text='Success is how high you bounce \nwhen you hit bottom', font=('Arial', 15, 'bold'), fg='#e0e0e0', bg='#121212')

label.pack(pady=30)
label_1.pack(pady=30, anchor='nw')
label_2.pack(pady=30, anchor='nw')
label_3.pack(pady=30, anchor='nw')
label_4.pack(pady=20, anchor='nw')
label_5.pack(pady=20)
window.mainloop()
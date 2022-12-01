import matplotlib.pyplot as plt
import tkinter as tk
import re

def integrate():
    m=func.get()
    m=str(m)
    x=re.split("[+-]",m )
    k=re.search("^x\^\d", x[0]):
        print(k[-1])

    print(x)
    print(k)

def delete_entry():
    func.delete(-1)

def graph():
    x=

win = tk.Tk()
photo=tk.PhotoImage(file='icon.png')
win.iconphoto(False, photo)
win.config(bg='#9600FF')
win.title('Calculus1')
win.geometry('1340x670+5+10')
win.minsize(800,500)
win.maxsize(1340,670)

label_1=tk.Label(win, text='Graph', bg='#9600FF', fg='#FFF504', font=('Gotham',50))
label_1.grid(row=0, column=0)
label_2=tk.Label(win, text='Function', bg='#9600FF', fg='#FFF504', font=('Gotham',14))
label_2.grid(row=1, column=0)

button=tk.Button(win, text='Integrate', command=integrate, bg='#FAFF49',
                 activebackground='#9600FF')
button.grid(row=1, column=3)
button2=tk.Button(win, text='delete', command=delete_entry, bg='#FAFF49',
                 activebackground='#9600FF').grid(row=2, column=2)

func=tk.Entry(win)
func.grid(row=1, column=2)
win.mainloop()



from tkinter import *
import string
import random

def gen():
    username = t1.get()
    pass_len = int(t2.get())

    if username and pass_len:
        characters = string.ascii_letters + string.digits + string.punctuation
        
        pass_len = max(pass_len, 2)
        
        pass_word = ''.join(random.choice(characters) for _ in range(pass_len))
        
        t3.delete(0, END)
        t3.insert(0, pass_word)
    else:
        t3.delete(0, END)
        t3.insert(0, "Please enter username and password length")

window = Tk()
window.title("Password Generator")
window.geometry("600x500")

lb11 = Label(window, text="Enter user name")
lb12 = Label(window, text="Enter password length")
lb13 = Label(window, text="Generate password")

t1 = Entry()
t2 = Entry()
t3 = Entry()

b1 = Button(window, text='Generate', command=gen)

lb11.place(x=100, y=100)
lb12.place(x=100, y=150)
lb13.place(x=100, y=200)
t1.place(x=250, y=100)
t2.place(x=250, y=150)
t3.place(x=250, y=200)
b1.place(x=250, y=250)

window.mainloop()


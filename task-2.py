from tkinter import *
def add():
    t3.delete(0,'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1+num2
    t3.insert(END,str(result))
def sub():
    t3.delete(0,'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1-num2
    t3.insert(END,str(result))
def mul():
    t3.delete(0,'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1*num2
    t3.insert(END,str(result))

def div():
    t3.delete(0,'end')
    num1=int(t1.get())
    num2=int(t2.get())
    result=num1/num2
    t3.insert(END,str(result))

def clr():
    t1.delete(0,'end')
    t2.delete(0,'end')
    t3.delete(0,'end')
              
window=Tk()
window.title('CALCULATOR')
window.geometry("600x500")
lb11=Label(window , text = 'First Number')
lb12=Label(window , text = "Second Number")
lb13=Label(window , text = "Result")

t1=Entry()
t2=Entry()
t3=Entry()

lb11.place(x=100 , y=50)           
t1.place(x=200 , y=50)
lb12.place(x=100 , y=100)
t2.place(x=200 , y=100)

b1=Button(window , text = 'Addition', command = add)
b2=Button(window , text = 'Subtract' , command= sub)
b3=Button(window , text = 'Multiply' , command= mul)
b4=Button(window , text = 'Division' , command= div)
b5=Button(window , text="Clear" , command=clr)
b1.place(x=350 , y=50)
b2.place(x=350 , y=100)
b3.place(x=350 , y=150)
b4.place(x=300 , y=200)
b5.place(x=200 , y=200)

lb13.place(x=100 , y=150)
t3.place(x=200 , y= 150)
window.mainloop()

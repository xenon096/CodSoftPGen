import random
from tkinter import *


#password generator function
def generator():
    elements = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*()"
    passwd = ""
    for i in range(n.get()):
        passwd += random.choice(elements)
    password.set(passwd)    


#window creation
x=Tk()
x.geometry("400x150")
x.title('Password Generator')
password=StringVar()
n=IntVar()

#elements
l1=Label(x,text="Enter the number of characters:").grid(row=1,column=1)

#entry of input charecters
e1=Entry(x,textvariable=n).grid(row=1,column=2)

#Button for result
b1=Button(x, text='Generate',command=generator).grid(row=3,column=2)

#Showing Generated Password
e2=Entry(x,textvariable=password).grid(row=4,column=2)
x.mainloop()

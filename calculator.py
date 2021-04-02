from tkinter import *
import math
from tkinter import messagebox
import turtle
import os
root=Tk()

#------------------title

root.title("Calculator")
#-----------------Entrybox
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

#----------popup--

def popup():
    global mat
    mat="popup"
    #e1=Entry(root,width=35,borderwidth=5)
    #e1.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
    res=messagebox.askyesno("FGHJKL")
    Label(root,text=res).pack()

#----------------add number
def buttonadd(number):
    curr=e.get()
    e.delete(0,END)
    e.insert(0,str(curr)+str(number))

#----------------addition

def buttonadd2():
    first=e.get()
    global f_num
    global mat
    mat="ADD"
    f_num=int(first)
    e.delete(0,END)

#-----------------Multiple

def buttonm():
    first=e.get()
    global f_num
    global mat
    mat="mul"
    f_num=int(first)
    e.delete(0,END)

#-----------------Divide

def buttondiv():
    first=e.get()
    global f_num
    global mat
    mat="divide"
    f_num=int(first)
    e.delete(0,END)

#---------------Minus

def buttonminus():
    first=e.get()
    global f_num
    global mat
    mat="Minus"
    f_num=int(first)
    e.delete(0,END)

#--------------------Log
def logr():
    first=e.get()
    global f_num
    global mat
    mat="log"
    f_num=int(first)
    e.delete(0,END)

#----------------------mathmatics
def mathmatics():
    global mat
    mat="mathmatics"
    os.system('python image.py')



def open():
    first=e.get()
    global f_num
    global mat
    mat="circle"
    f_num=int(first)
    ar=3.14*f_num*f_num
    e.delete(0,END)
    t = turtle.Turtle()
    t.circle(f_num)
    t.write("Radius of Circle="+str(f_num),move=True)
    t.write("Area of Circle="+str(ar))
#-----------------count

def count1():
    first=e.get()
    global f_num
    global mat
    mat="count"
    f_num=int(first)

def count5():
    first=e.get()
    global f_num
    global mat
    mat="count1"
    f_num=int(first)






def power():
    first=e.get()
    global f_num
    global mat
    mat="power"
    f_num=int(first)
    e.delete(0,END)

#------------------------factorial

def fact():
    first=e.get()
    global f_num
    global mat
    mat="factorial"
    f_num=int(first)
    e.delete(0,END)

#-------------------squareroot
def square():
    first=e.get()
    global f_num
    global mat
    mat="squareroot"
    f_num=int(first)
    e.delete(0,END)

#------------------Cuberoot
def Cuberoot():
    first=e.get()
    global f_num
    global mat
    mat="cuberoot"
    f_num=int(first)
    e.delete(0,END)

def result():

#-----------------Multiple
    if mat=="mul":
        second=e.get()
        e.delete(0,END)
        e.insert(0,f_num*int(second))

#-----------------Divide

    elif mat=="divide":
        second=e.get()
        e.delete(0,END)
        e.insert(0,f_num / int(second))

#---------------Minus

    elif mat=="Minus":
        second=e.get()
        e.delete(0,END)
        e.insert(0,f_num-int(second))

#-----------power

    elif mat=="power":
        second=e.get()
        e.delete(0,END)
        e.insert(0,f_num**int(second))

#--------------factorial

    elif mat=="factorial":
        fact=1
        for j in range(1,f_num+1):
            fact*=j
        e.insert(0,fact)

#-----------------Squareroot

    elif mat=="squareroot":
        x=math.sqrt(f_num)
        e.insert(0,x)

#----------------Cuberoot

    elif mat=="cuberoot":
        y=(f_num)**(1/3)
        e.insert(0,y)

#-----------------log

    elif mat=="log":
        y=math.log(f_num)
        e.insert(0,y)

#---------------circle----

    elif mat=="circle":
        y=3.14*f_num*f_num
        e.insert(0,y)

#--------------------count5

    elif mat=="count":
        x=fact=1
        for j in range(1,f_num+1):
            fact*=j
        x=str(fact).count('0')
        e.delete(0,END)
        e.insert(0,x)

#--------------------count5


    elif mat=="count1":
        x=fact=1
        for j in range(1,f_num+1):
            fact*=j
        x=str(fact).count('5')
        e.delete(0,END)
        e.insert(0,x)

#----------------addition

    elif mat=="ADD":
        second=e.get()
        e.delete(0,END)
        e.insert(0,f_num+int(second))
    elif mat=="mathmatics":
        os.system('python image.py')

def clear():
    e.delete(0,END)

#==============================Addotion
btn=Button(root,text="1",padx=40,pady=20,command=lambda: buttonadd("1"))
btn.grid(row=1,column=0)
btn1=Button(root,text="2",padx=40,pady=20,command=lambda: buttonadd("2"))
btn1.grid(row=1,column=1)
btn2=Button(root,text="3",padx=40,pady=20,command=lambda: buttonadd("3"))
btn2.grid(row=1,column=2)

#-----------------------------multiply
btn3=Button(root,text="*",padx=40,pady=20,command=buttonm)
btn3.grid(row=1,column=3)
btn=Button(root,text="4",padx=40,pady=20,command=lambda: buttonadd("4"))
btn.grid(row=2,column=0)
btn1=Button(root,text="5",padx=40,pady=20,command=lambda: buttonadd("5"))
btn1.grid(row=2,column=1)
btn2=Button(root,text="6",padx=40,pady=20,command=lambda: buttonadd("6"))
btn2.grid(row=2,column=2)
#---------------------------Minus
btn3=Button(root,text="-",padx=40,pady=20,command=buttonminus)
btn3.grid(row=2,column=3)
btn=Button(root,text="7",padx=40,pady=20,command=lambda: buttonadd("7"))
btn.grid(row=3,column=0)
btn1=Button(root,text="8",padx=40,pady=20,command=lambda: buttonadd("8"))
btn1.grid(row=3,column=1)
btn2=Button(root,text="9",padx=40,pady=20,command=lambda: buttonadd("9"))
btn2.grid(row=3,column=2)
#------------------------divide
btn3=Button(root,text="/",padx=40,pady=20,command=buttondiv)
btn3.grid(row=3,column=3)
btn3=Button(root,text="0",padx=40,pady=20,command=lambda: buttonadd("0"))
btn3.grid(row=4,column=0)
#------------------------addition
btn3=Button(root,text="+",padx=40,pady=20,command=buttonadd2)
btn3.grid(row=4,column=1)
#------------------------equal to
btn3=Button(root,text="=",padx=90,pady=20,command=result)
btn3.grid(row=4,column=2,columnspan=2)
#------------------------Clear
btn3=Button(root,text="Clear",padx=40,pady=20,command=clear)
btn3.grid(row=0,column=3)
#----------------------squareroot
btn4=Button(root,text="X^Y",padx=40,pady=20,command=power)
btn4.grid(row=5,column=0)
#----------------------Factorial
btn5=Button(root,text="X!",padx=40,pady=20,command=fact)
btn5.grid(row=5,column=1)
#----------------------Squareroot
btn6=Button(root,text="√",padx=40,pady=20,command=square)
btn6.grid(row=5,column=2)
#----------------------Cuberoot
btn6=Button(root,text="3√",padx=40,pady=20,command=Cuberoot)
btn6.grid(row=5,column=3)

#-----------------------area
btn7=Button(root,text="Cir",padx=40,pady=20,command=open)
btn7.grid(row=6,column=0)
#------------------------log
btn8=Button(root,text="log",padx=40,pady=20,command=logr)
btn8.grid(row=6,column=1)
#------------------------count
btn9=Button(root,text="!C-0",padx=40,pady=20,command=count1)
btn9.grid(row=6,column=2)
#---------------------count5
btn10=Button(root,text="!C-5",padx=40,pady=20,command=count5)
btn10.grid(row=6,column=3)
#----------------------math
btn10=Button(root,text="Math",padx=40,pady=20,command=mathmatics)
btn10.grid(row=1,column=4)


root.mainloop()

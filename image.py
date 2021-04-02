from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("FGHJKLHG")


img=ImageTk.PhotoImage(Image.open("3-8.png"))
img1=ImageTk.PhotoImage(Image.open("CNX_Calc_Figure_01_03_013.jpeg"))
img2=ImageTk.PhotoImage(Image.open("E3QYaaFhta-trig_unitcircle.png"))
img3=ImageTk.PhotoImage(Image.open("Trigonometry-functions-graphs.png"))
img4=ImageTk.PhotoImage(Image.open("unitcircleMB2a.jpg"))
img5=ImageTk.PhotoImage(Image.open("unitcircleMBa.jpg"))
img6=ImageTk.PhotoImage(Image.open("xtrigonometrical-ratios-table.png.pagespeed.ic.MpPFp5rL1f.png"))
img7=ImageTk.PhotoImage(Image.open("xtrigonometricratiosofspecificangles9.png.pagespeed.ic.xeInLbj8i4.png"))
liglist=[img,img1,img2,img3,img4,img5,img6,img7]
lab=Label(image=img)
lab.grid(row=0,column=1,columnspan=3)

def forward(images_number):
    global lab
    global btnforw
    global btnback
    lab.grid_forget()
    lab=Label(image=liglist[images_number-1])
    btnforw=Button(root,text=">>",command=lambda:forward(images_number+1))
    btnback=Button(root,text="<<",command=lambda:back(images_number-1))
    if images_number==8:
        btnforw=Button(root,text=">>",state=DISABLED)
    lab.grid(row=0,column=1,columnspan=3)
    btnforw.grid(row=0,column=5)
    btnback.grid(row=0,column=0)


def back(images_number):
    global lab
    global btnforw
    global btnback
    lab.grid_forget()
    lab=Label(image=liglist[images_number-1])
    btnforw=Button(root,text=">>",command=lambda:forward(images_number+1))
    btnback=Button(root,text="<<",command=lambda:back(images_number-1))
    if images_number==1:
        btnback=Button(root,text="<<",state=DISABLED)
    lab.grid(row=0,column=1,columnspan=3)
    btnforw.grid(row=0,column=5)
    btnback.grid(row=0,column=0)

btnback=Button(root,text="<<",command=lambda:back(8))
btnquit2=Button(root,text="EXIT",command=root.quit)
btnforw=Button(root,text=">>",command=lambda:forward(2))
btnback.grid(row=0,column=0)
btnquit2.grid(row=1,column=2)
btnforw.grid(row=0,column=5)

root.mainloop()


# Python program to draw
# Rainbow Benzene
# using Turtle Programming
import turtle
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('black')
for x in range(360):
	t.pencolor(colors[x%6])
	t.width(x/100 + 1)
	t.forward(x)
	t.left(59)

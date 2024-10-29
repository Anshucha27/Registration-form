from tkinter import *
from PIL import ImageTk,Image

def selection():
 selection="You select the option"+ str(var.get())
 label.config(text= selection)

root=Tk()
var=IntVar()


root.title("Registration Form")
root.geometry("800x500")
root.resizable(False,False)
image=Image.open("form1.jpg")
image=image.resize((800,500),Image.LANCZOS)
img=ImageTk.PhotoImage(image)
lbl=Label(root,image=img)
lbl=lbl.pack()

lbl1=Label(root,text="REGISTRATION FORM",fg="black",font=("Arial 26 bold underline"))
lbl1.place(x=200,y=20)

lbl2=Label(root,text="NAME :",fg="black",font=("Arial 18 "))
lbl2.place(x=50,y=100)
e2=Entry(root,font=("Arial 15"))
e2.place(x=200,y=100)

lbl3=Label(root,text="EMAIL :",fg="black",font=("Arial 18 "))
lbl3.place(x=50,y=150)
e3=Entry(root,font=("Arial 15"))
e3.place(x=200,y=150)

lbl4=Label(root,text="MOBILE :",fg="black",font=("Arial 18 "))
lbl4.place(x=50,y=200)
e4=Entry(root,font=("Arial 15"))
e4.place(x=200,y=200)

lbl5=Label(root,text="GENDER :",fg="black",font=("Arial 18 "))
lbl5.place(x=50,y=250)

R1= Radiobutton(root,text="Male", variable=var,value= 1,command = selection)
R1.place(x=200,y=250)

R2= Radiobutton(root,text="FEMALE", variable=var,value= 2,command = selection)
R2.place(x=290,y=250)

R3= Radiobutton(root,text="OTHER", variable=var,value= 3,command = selection)
R3.place(x=400,y=250)

label=Label(root)
label.place(x=490,y=250)

options=StringVar()
options.set("Select")



dropdown=OptionMenu(root,options,"Lucknow","Delhi","Nodia","Patna","Agra")
dropdown.place(x=450,y=300)
e5=Entry(root,font=("Arial 15"))
e5.place(x=200,y=300)
def show():
 print(options.get())

btn=Button(root,text="SUBMIT",command=show)
btn.place(x=50,y=370)

root.mainloop()




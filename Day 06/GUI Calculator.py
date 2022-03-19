from tkinter import *
root=Tk()
root.geometry("250x350")
root.minsize(250,350)
root.maxsize(250,350)
root.title("Neya Calsi")
root.configure(bg="orange")

def click(event):
    global val
    text=event.widget.cget("text")
    if text=="=":
        if val.get().isdigit():
            value = int(val.get())
        else:
            try:
                value= eval(enter.get())

            except Exception as e:
                print(e)
                value="Error"
        val.set(value)
        enter.update()
    elif text =="C":
        val.set("")
        enter.update()
    else:
        val.set(val.get()+text)
        enter.update()
        pass


val=StringVar()
val.set("")
enter=Entry(root,textvariable=val,font="Helvetica 25 bold",bd=15,relief=SUNKEN)
enter.pack(fill=X,ipadx=4,padx=10,pady=10)

f=Frame(root,bg="black")
b=Button(f,text="9",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="8",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="7",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="+",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="6",pady=2,padx=3,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="5",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="4",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="-",pady=2,padx=5,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="3",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="2",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="1",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="*",pady=2,padx=3,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
f.pack()

f=Frame(root,bg="black")
b=Button(f,text="C",pady=2,padx=1,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="0",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="/",pady=2,padx=5,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
b=Button(f,text="=",pady=2,padx=2,bg="black",fg="white",font="Helvetica 20 bold")
b.bind ("<Button-1>",click)
b.pack(side=LEFT,padx=2,pady=2)
f.pack()

root.mainloop()
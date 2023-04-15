import tkinter
root=tkinter.Tk()
root.title("Registration Form")
root.geometry("500x700")
root.configure(bg= "yellow")

lab=tkinter.Label(root,text="Registration Form",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lab.place(x=60,y=40,height=50,width=380)

lab=tkinter.Label(root,text="User Name",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lab.place(x=60,y=130,height=50,width=380)


lab=tkinter.Label(root,text="Email",font=("Time New Roman",30,"bold"),bg="red",fg="white")
lab.place(x=60,y=200,height=50,width=380)





root.mainloop()
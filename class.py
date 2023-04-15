import tkinter 
root=tkinter.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="light green")
l1=tkinter.Label(root,text="Login Page",bg="black",fg="white",font="Arial 14 bold")
l1.pack()

l2=tkinter.Label(root,text="User Name",bg="light green",fg="white",font="Arial 14 ").pack()
e1=tkinter.Entry()
e1.pack()

l3=tkinter.Label(root,text="Password",fg="red",bg="light green",font="Arial 14").pack()
e2=tkinter.Entry()
e2.pack()
b1=tkinter.Button(root,text="Login",font="Arial 12 italic")
b1.pack()
b1=tkinter.Button(root,text="Cancel",font="Arial 12 italic")
b1.pack()

root.mainloop()


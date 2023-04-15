import tkinter
import tkinter.messagebox as Messagebox
from PIL import Image,ImageTk
root=tkinter.Tk()
root.title("Login Page")
root.geometry("400x300")
root.configure(bg="light yellow")
l1=tkinter.Label(root,text="Login Page",bg="black",fg="white",font="Arial 14 bold")
l1.pack()
image=Image.open("")
photo=ImageTk.PhotoImage(image)
p1=tkinter.Label(root,image=photo)
p1.place(x=0,y=0)
root.mainloop()
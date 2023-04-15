import tkinter 
import webbrowser
root=tkinter.Tk()
root.geometry("400x300")
root.title("webserver")

root.configure(bg="light pink")

def google():
    webbrowser.open("https://www.google.co.in")

def facebook():
        webbrowser.open("https://www.facebook.com")


def youtube():
    webbrowser.open("http://in.youtube.com/")
b1=tkinter.Button(root,text="Google",bg="yellow",fg="white",font="Arial 14 bold",command=google)
b1.place(x=10,y=100)

b2=tkinter.Button(root,text="Facebook",bg="yellow",fg="white",font="Arial 14 bold",command=facebook)
b2.place(x=10,y=150)

b3=tkinter.Button(root,text="Youtube",bg="yellow",fg="white",font="Arial 14 bold",command=youtube)
b3.place(x=10,y=200)

root.mainloop()
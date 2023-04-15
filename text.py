import tkinter 
import webbrowser
root=tkinter.Tk()
root.geometry("400x300")
root.title("webserver")
root.configure(bg="black")
def google():
      webbrowser.open("https://www.google.com")
def facebook():
      webbrowser.open("https://www.facebook.com")


def youtube():
   webbrowser.open("https://www.youtube.com/hashtag/youtuber")

b1=tkinter.Button(root,text="Google",bg=" red",fg=" green",font="Arial 14 bold",command=google)
b1.place(x=10,y=50)
b2=tkinter.Button(root,text="Facebook",bg="red",fg="green",font="Arial 14 bold",command=facebook)
b2.place(x=10,y=100)

b3=tkinter.Button(root,text="Youtube",bg="red",fg=" green",font="Arial 14 bold",command=youtube)
b3.place(x=10,y=150)


root.mainloop()
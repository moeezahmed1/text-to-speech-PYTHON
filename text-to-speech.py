import tkinter as tk
from tkinter import *
import pyttsx3


engine= pyttsx3.init()
def speaknow():
    engine.say(textv.get())
    engine.runAndWait()
    engine.stop()

root=Tk()

textv=StringVar()

obj = LabelFrame(root,text="Text To Speech" , font=20,bd=1)
obj.pack(fill='both',expand='yes',padx=10,pady=10)

lbl = Label(obj,text='Text' , font=30)

lbl.pack(side=tk.LEFT,padx=5)

text=Entry(obj,textvariable=textv,font=30,width=25,bd=5)
text.pack(side=tk.LEFT,padx=10)

btn=Button(obj,text='Speech', font=20,bg='blue',fg='white', command= speaknow )
btn.pack(side=tk.LEFT,padx=10)

#import icon
image_icon = PhotoImage(file="texttospeech.png")
root.iconphoto(False,image_icon)

#import logo
photo = PhotoImage(file="texttospeech.png")
myimage = Label(image=photo, background='#ffffff')
myimage.pack(padx=5,pady=5)


root.title("Text To Speech")
root.geometry('800x400')
root.resizable(False,False)


root.mainloop()

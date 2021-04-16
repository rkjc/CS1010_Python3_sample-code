import tkinter

def buttonColor(aButton, aColor):
    aButton.configure(background = aColor, highlightbackground = aColor, activebackground = aColor)

def doButton():
    label_1.configure(text = "you pushed the button")

bob = tkinter.Tk()
bob.geometry('200x100')

label_1 = tkinter.Label(bob, text="A Label")
label_1.pack()

button_1 = tkinter.Button(bob, text="A Button", command=doButton)
buttonColor(button_1, 'red')
button_1.pack()

bob.mainloop()
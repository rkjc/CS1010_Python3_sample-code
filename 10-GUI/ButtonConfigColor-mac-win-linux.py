import tkinter

def doButton():
    label_1.configure(text = "you pushed the button")

bob = tkinter.Tk()
bob.geometry('200x100')

label_1 = tkinter.Label(bob, text="A Label")
label_1.pack()

button_1 = tkinter.Button(bob, text="A Button", command=doButton)
# Special note for Button Colors
# windows and Linux need the 'background' setting
# MacOs needs the 'highlightbackground' setting (MacOs Big Sur may have broken this again)
# Linux needs the 'activebackground' setting to handle mouse-overs
button_1.configure(background = 'cyan', highlightbackground = 'cyan', activebackground = 'cyan')
button_1.pack()

bob.mainloop()
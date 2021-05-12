import tkinter


root = tkinter.Tk()
root.columnconfigure(0, minsize=100)
root.columnconfigure(1, minsize=200)

def doButton1():
    label_1.config(image=img01)


#images have to be .png, .jpg does not work.
img01 = tkinter.PhotoImage(file="images/Sciencecandoit.png")

img01_size_6 = img01.subsample(6)
img01_size_2 = img01.subsample(2)


label_1 = tkinter.Label(root, text="images")
label_1.grid(row=1, rowspan=3, column=1)


MyButton1 = tkinter.Button(root, image=img01_size_6, text="b1", bg="blue", width=100, height=100, command = lambda: doButton1())
MyButton1.grid(row=1, column=0)



root.mainloop()

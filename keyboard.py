from tkinter import *
from PIL import ImageTk,Image
from tkinter import font

root = Tk()
root.title('onscreen keyboard')
root.geometry('800x480')
bgImg = PhotoImage('1.jpg')
root.configure(background="blue")

MainFrame = Frame(root, bd=10, width=800, height= 160)
MainFrame.pack(side="bottom")
Row1Frame = Frame(MainFrame, width=800, height=40)
Row1Frame.pack()
Row2Frame = Frame(MainFrame, width=800, height=40)
Row2Frame.pack()
Row3Frame = Frame(MainFrame, width=800, height=40)
Row3Frame.pack()


# text input display
exp = " "
input = StringVar()
display = Entry(root, width=800, textvariable=input)
display.pack()

def press(letter):
    global exp
    if str(letter) == "CLEAR":
        newExp = exp[:-1]
        exp = newExp
        input.set(exp)
    elif str(letter) == "DONE":
        input.set("")
        Label(root, text=exp).pack()
        exp = ""
    else:
        exp = exp + str(letter)
        input.set(exp)

# top row
KEYS = [
    [("Q", 0),("W", 1),("E", 2),("R", 3),("T", 4),("Y", 5),("U", 6),("I", 7),("O", 8),("P", 9)],
    [("A", 0),("S", 1),("D", 2),("F", 3),("G", 4),("H", 5),("J", 6),("K", 7),("L", 8)],
    [("Z", 0),("X", 1),("C", 2),("V", 3),("B", 4),("N", 5),("M", 6), ("CLEAR", 7), ("DONE", 8)]
]
for i in range(len(KEYS)):
    for key, pos in KEYS[i]:
        if i == 0:
            Button(Row1Frame, width=5, text=key, command=lambda key=key: press(key)).grid(row=i, column=pos)
        if i == 1:
            Button(Row2Frame, width=5, text=key, command=lambda key=key: press(key)).grid(row=i, column=pos)
        if i == 2:
            Button(Row3Frame, width=5, text=key, command=lambda key=key: press(key)).grid(row=i, column=pos)
root.mainloop()



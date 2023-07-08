from customtkinter import *
from PIL import ImageTk,Image


root = CTk()
root.title('onscreen keyboard')
root.geometry('800x480')
root.configure(background="blue")

MainFrame = CTkFrame(root, height= 160, fg_color="black", border_width=0)
Row1Frame = CTkFrame(MainFrame, width=800, height=40, fg_color="black", border_width=0)
Row2Frame = CTkFrame(MainFrame, width=800, height=40, fg_color="black", border_width=0)
Row3Frame = CTkFrame(MainFrame, width=800, height=40, fg_color="black", border_width=0)

def keyboard_frames():
    MainFrame.pack(side="bottom", fill="x")
    Row1Frame.pack()
    Row2Frame.pack()
    Row3Frame.pack()
    for i in range(len(KEYS)):
        for key, pos in KEYS[i]:
            if i == 0:
                CTkButton(Row1Frame, width=70, font=('Quicksand', 16),text=key, command=lambda key=key: press(key)).grid(row=i, column=pos, padx=5, pady=5)
            if i == 1:
                CTkButton(Row2Frame, width=70, font=('Quicksand', 16),text=key, command=lambda key=key: press(key)).grid(row=i, column=pos, padx=5, pady=5)
            if i == 2:
                CTkButton(Row3Frame, width=70, font=('Quicksand', 16),text=key, command=lambda key=key: press(key)).grid(row=i, column=pos, padx=5, pady=5)


# text input display
exp = " "
input = StringVar()
display = CTkEntry(root, width=800, textvariable=input, insertontime=0)
display.pack()
display.bind("<Button-1>", lambda event: keyboard_frames())


def press(letter):
    global exp
    if str(letter) == "CLEAR":
        newExp = exp[:-1]
        exp = newExp
        input.set(exp)
    elif str(letter) == "DONE":
        input.set("")
        CTkLabel(root, text=exp).pack()
        exp = ""
        MainFrame.pack_forget()
        Row1Frame.pack_forget()
        Row2Frame.pack_forget()
        Row3Frame.pack_forget()
    else:
        exp = exp + str(letter)
        input.set(exp)

# top row
KEYS = [
    [("Q", 0),("W", 1),("E", 2),("R", 3),("T", 4),("Y", 5),("U", 6),("I", 7),("O", 8),("P", 9)],
    [("A", 0),("S", 1),("D", 2),("F", 3),("G", 4),("H", 5),("J", 6),("K", 7),("L", 8)],
    [("Z", 0),("X", 1),("C", 2),("V", 3),("B", 4),("N", 5),("M", 6), ("CLEAR", 7), ("DONE", 8)]
]

root.mainloop()



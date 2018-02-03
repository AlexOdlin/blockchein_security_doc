from tkinter import *
from random import *

def button_clicked():
    print(button['bg'])
    bg = '#%0x%0x%0x' % (int(random()*16), int(random()*16), int(random()*16))
    button['bg'] = bg
    button['activebackground'] = bg

root = Tk()
button = Button(root, command=button_clicked)
button.pack()
root.mainloop()
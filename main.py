from tkinter import *


def button_clicked():
    message = text1.get('1.0', END)
    if message[1] == '+':
        print(int(message[0]) + int(message[2]))
    elif message[1] == '*':
        print(int(message[0]) * int(message[2]))
    elif message[1] == '-':
        print(int(message[0]) - int(message[2]))
    elif message[1] == '/':
        print(int(message[0]) / int(message[2]))


root = Tk()

root.title('Test programm')
root.geometry('500x400+300+200')  # ширина=500, высота=400, x=300, y=200
root.resizable(False, False)  # размер окна может быть изменён только по горизонтали

label1 = Label(root, text='Hi! it\'s a programm!')
label1.pack()
text1 = Text(root, height=1, width=7, font='Arial 14')
text1.pack()
button = Button(root, text='push', command=button_clicked)
button.pack()

button.place(x=180, y=200, anchor=CENTER)
label1.place(x=80, y=20, anchor=CENTER)
text1.place(x=200, y=160, anchor=CENTER)

root.mainloop()

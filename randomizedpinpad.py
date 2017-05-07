from tkinter import *
from random import shuffle

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(row=0)
        self.create_widgets()

    def create_widgets(self):
        numberList = []
        i = 1

        self.title = Label(self, text="Randomized Pinpad")
        self.title.grid(row=0, columnspan=3)

        while i < 10:
            numberList.append(i)
            i = i + 1

        shuffle(numberList)

        self.button1 = Button(self)
        self.button1["text"] = numberList[0]
        self.button1.grid(row=1, column=0)
        self.button2 = Button(self)
        self.button2["text"] = numberList[1]
        self.button2.grid(row=1, column=1)
        self.button3 = Button(self)
        self.button3["text"] = numberList[2]
        self.button3.grid(row=1, column=2)
        self.button4 = Button(self)
        self.button4["text"] = numberList[3]
        self.button4.grid(row=2, column=0)
        self.button5 = Button(self)
        self.button5["text"] = numberList[4]
        self.button5.grid(row=2, column=1)
        self.button6 = Button(self)
        self.button6["text"] = numberList[5]
        self.button6.grid(row=2, column=2)
        self.button7 = Button(self)
        self.button7["text"] = numberList[6]
        self.button7.grid(row=3, column=0)
        self.button8 = Button(self)
        self.button8["text"] = numberList[7]
        self.button8.grid(row=3, column=1)
        self.button9 = Button(self)
        self.button9["text"] = numberList[8]
        self.button9.grid(row=3, column=2)


root = Tk()
app = Application(master=root)
app.mainloop()

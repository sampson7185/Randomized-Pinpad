from tkinter import *
from random import shuffle

class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.main_container = Frame(self, background="bisque")
        self.main_container.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.create_widgets()

    def create_widgets(self):
        numberList = []
        i = 1

        self.top_frame = Frame(self.main_container, background="green")
        self.bottom_frame = Frame(self.main_container, background="yellow")
        self.top_frame.grid(row=0, column=0, sticky="ew")
        self.bottom_frame.grid(row=1, column=0,sticky="nsew")
        self.main_container.grid_rowconfigure(1, weight=1)
        self.main_container.grid_columnconfigure(0, weight=1)

        self.title = Label(self.top_frame, text="Randomized Pinpad", font=("Times", 16, "bold"))
        self.title.grid(row=0, sticky="nsew")
        self.top_frame.grid_rowconfigure(0, weight=1)
        self.top_frame.grid_columnconfigure(0, weight=1)

        while i < 10:
            numberList.append(i)
            i = i + 1

        shuffle(numberList)

        self.button1 = Button(self.bottom_frame)
        self.button1["text"] = numberList[0]
        self.button1.grid(row=0, column=0, sticky="nsew")
        self.button2 = Button(self.bottom_frame)
        self.button2["text"] = numberList[1]
        self.button2.grid(row=0, column=1, sticky="nsew")
        self.button3 = Button(self.bottom_frame)
        self.button3["text"] = numberList[2]
        self.button3.grid(row=0, column=2, sticky="nsew")
        self.button4 = Button(self.bottom_frame)
        self.button4["text"] = numberList[3]
        self.button4.grid(row=1, column=0, sticky="nsew")
        self.button5 = Button(self.bottom_frame)
        self.button5["text"] = numberList[4]
        self.button5.grid(row=1, column=1, sticky="nsew")
        self.button6 = Button(self.bottom_frame)
        self.button6["text"] = numberList[5]
        self.button6.grid(row=1, column=2, sticky="nsew")
        self.button7 = Button(self.bottom_frame)
        self.button7["text"] = numberList[6]
        self.button7.grid(row=2, column=0, sticky="nsew")
        self.button8 = Button(self.bottom_frame)
        self.button8["text"] = numberList[7]
        self.button8.grid(row=2, column=1, sticky="nsew")
        self.button9 = Button(self.bottom_frame)
        self.button9["text"] = numberList[8]
        self.button9.grid(row=2, column=2, sticky="nsew")
        self.bottom_frame.grid_rowconfigure(0, weight=1)
        self.bottom_frame.grid_columnconfigure(0, weight=1)
        self.bottom_frame.grid_rowconfigure(1, weight=1)
        self.bottom_frame.grid_columnconfigure(1, weight=1)
        self.bottom_frame.grid_rowconfigure(2, weight=1)
        self.bottom_frame.grid_columnconfigure(2, weight=1)


root = Tk()
app = Application(master=root)
app.mainloop()

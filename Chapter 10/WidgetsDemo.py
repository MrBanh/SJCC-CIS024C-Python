from tkinter import *


class WidgetsDemo:
    def __init__(self):
        window = Tk()       # Create a window
        window.title("Widgets Demo")

        # Add a button, a check button, and a radio button to frame1
        frame1 = Frame(window)
        frame1.pack()
        self.v1 = IntVar()
        cbtnBold = Checkbutton(frame1, text="Bold", variable=self.v1, command=self.processCheckbutton)
        self.v2 = IntVar()
        rbtnRed = Radiobutton(frame1,text="Red", bg="red", variable=self.v2, value=1, command=self.processRadiobutton)
        rbtnYellow = Radiobutton(frame1,text="Yellow", bg="Yellow", variable=self.v2, value=2, command=self.processRadiobutton)
        cbtnBold.grid(row=1, column=1)
        rbtnRed.grid(row=1, column=2)
        rbtnYellow.grid(row=1, column=3)

        # Add label, entry, button, and message to frame2
        frame2 = Frame(window)
        frame2.pack()
        label = Label(frame2, text="Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable=self.name)
        btnGetName = Button(frame2, text="Get Name", command=self.processButton)
        message = Message(frame2, text="It is a widgets demo")
        label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btnGetName.grid(row=1, column=3)
        message.grid(row=1, column=4)

        # Add a text
        text = Text(window)     # Create a text add to the window
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your applications")

        window.mainloop()


    def processCheckbutton(self):
        print("check button is", "checked" if self.v1.get() == 1 else "unchecked")

    def processRadiobutton(self):
        print("Red" if self.v2.get() == 1 else "Yellow", "is selected")

    def processButton(self):
        print("Your name is", self.name.get())


WidgetsDemo()

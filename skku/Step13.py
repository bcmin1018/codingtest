from tkinter import *

class App(Frame):
    def __init__(self, window):
        super().__init__(window)
        self.pack(padx=20, pady=10)
        label = Label(self)
        label['text'] ='Hello, world!'
        label['bg'] = 'blue'
        label['fg'] = 'white'
        label.pack()


window = Tk()
window.title("hello")
window.geometry("200x100")
App(window)
window.mainloop()



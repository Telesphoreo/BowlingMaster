import tkinter as tk
from tkinter import ttk, Entry, StringVar

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        tk.configure(bg="black")

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bowling Master")
    MyFrame(root)
    root.mainloop()


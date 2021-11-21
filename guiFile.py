import tkinter as tk
from tkinter import ttk, Entry, StringVar

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.parent.configure(background='black')

        self.pack()
        tk.Button(self, height=3, text="Manage Teams", width=225, bg="purple", fg="white").grid(column=0, row=0, sticky=tk.E)
        tk.Button(self, height=3, text="Manage Players", width=225, bg="purple", fg="white").grid(column=0, row=1, sticky=tk.E)
        tk.Button(self, height=3, text="Manage Scores", width=225, bg="purple", fg="white").grid(column=0, row=2, sticky=tk.E)
        tk.Button(self, height=3, text="Other Options", width=225, bg="purple", fg="white").grid(column=0, row=3, sticky=tk.E)
        tk.Button(self, height=3, text="Show All Players", width=225, bg="purple", fg="white").grid(column=0, row=4, sticky=tk.E)
        tk.Button(self, height=3, text="About", width=225, bg="purple", fg="white").grid(column=0, row=5, sticky=tk.E)
        tk.Button(self, height=3, text="Exit", width=225, bg="purple", fg="white").grid(column=0, row=6, sticky=tk.E)


        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bowling Master")
    MyFrame(root)
    root.mainloop()


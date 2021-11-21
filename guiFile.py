import tkinter as tk
from tkinter import ttk, Entry, StringVar

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()
        ttk.Button(self, text="Manage Teams").grid(column=0, row=0, sticky=tk.E)
        ttk.Button(self, text="Manage Players").grid(column=0, row=1, sticky=tk.E)
        ttk.Button(self, text="Manage Scores").grid(column=0, row=2, sticky=tk.E)
        ttk.Button(self, text="Other Options").grid(column=0, row=3, sticky=tk.E)
        ttk.Button(self, text="Show All Players").grid(column=0, row=4, sticky=tk.E)
        ttk.Button(self, text="About").grid(column=0, row=5, sticky=tk.E)
        ttk.Button(self, text="Exit").grid(column=0, row=6, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bowling Master")
    MyFrame(root)
    root.mainloop()


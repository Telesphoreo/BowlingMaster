import tkinter as tk
from tkinter import ttk, Entry, Label, StringVar

class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.pack()


        self.miles = tk.StringVar()
        self.gallons = tk.StringVar()
        self.mpg = tk.StringVar()

        ttk.Label(self, text="Miles Driven:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Label(self, text="Gallons Used:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Label(self, text="MPG:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=30, textvariable=self.miles).grid(
            column=1, row=0)
        ttk.Entry(self, width=30, textvariable=self.gallons).grid(
            column=1, row=1)
        ttk.Entry(self, width=30, textvariable=self.mpg, state = "readonly").grid(
            column=1, row=2)
        ttk.Button(self, text="Calculate", command=self.calculator).grid(column=1, row=3, sticky=tk.E)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)
    def calculator(self):
        miles = float(self.miles.get())
        gallons = float(self.gallons.get())

        milespGallon = miles/gallons
        milespGallon = round(milespGallon, 2)
        self.mpg.set(milespGallon)
if __name__ == "__main__":
    root = tk.Tk()
    root.title("MPG Calculator")
    MyFrame(root)
    root.mainloop()


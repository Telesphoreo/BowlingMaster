import csv
import shutil
from prettytable import PrettyTable
from os.path import exists

filename="scores.csv"

class Points
    def __init__(self):
        self.initializeFile()

    def initializeFile(self):
        # Create the file if it doesn't exist already as a failsafe
        if not exists(filename):
            with open(filename, "x") as file:
                file.close()

    def addPoints(self):

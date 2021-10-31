import csv
from prettytable import PrettyTable
from os.path import exists
import pandas as pd

filename = "players.csv"


class Player:
    def __init__(self):
        pass

    # Create a new player
    def createPlayer(self, name):
        # [1, Name]]
        name = [self.generateId(), name]
        with open(filename, "a") as file:
            writer = csv.writer(file)
            writer.writerow(name)
        file.close()

    def deletePlayer(self, id):
        ihatepython = pd.read_csv(filename)

    # Method for generating an ID for each player
    def generateId(self):
        # Create the file if it doesn't exist already as a failsafe
        if not exists(filename):
            with open(filename, "x") as file:
                file.close()

        with open(filename, "r") as file:
            try:
                # Read the last line of the file
                last_line = file.readlines()[-1]
                # Split the IDs and names
                previousID = last_line.split(",")[0]
                # (Hopefully) convert it to an integer and add 1
                newID = int(previousID) + 1
                file.close()
                return newID
            # If this is the first player, return 1
            except IndexError:
                return "1"
            # Error, ID row is probably a string
            except ValueError:
                print("There was an error reading the file (Is there a string for the ID?)")

    # List every player
    def listPlayers(self):
        with open(filename, "r") as file:
            table = PrettyTable()
            # Header
            table.field_names = ["IDs", "Players"]
            reader = file.readlines()
            # Iterate through every player and add it to the table
            for lines in reader:
                ids = lines.split(",")[0]
                names = lines.split(",", )[1].strip("\n")
                table.add_row([ids, names])
        file.close()
        return table

    # Get a player's name from their ID
    def getName(self, id):
        with open(filename, "r") as file:
            reader = file.readlines()
            for lines in reader:
                # List of IDs
                if lines.split(",")[0] == id:
                    # Return the name
                    return lines.split(",")[1]
        file.close()

    def getID(self, name):
        with open(filename, "r") as file:
            reader = file.readlines()
            print(name)
            for lines in reader:
                print(lines.split(",")[1])
                if name == lines.split(",")[1]:
                    print(lines.split(",")[0])
                    return lines.split(",")[0]
        file.close()

def main():
    Player().deletePlayer("1")

if __name__ == '__main__':
    main()
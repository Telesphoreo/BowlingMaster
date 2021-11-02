import csv
import shutil
from prettytable import PrettyTable
from os.path import exists

filename = "players.csv"


class Player:
    def __init__(self):
        self.initializeFile()

    def initializeFile(self):
        # Create the file if it doesn't exist already as a failsafe
        if not exists(filename):
            with open(filename, "x") as file:
                file.close()

    # Create a new player
    def createPlayer(self, name):
        # [1, Name, 0]
        name = [self.generateId(), name]
        with open(filename, "a") as file:
            writer = csv.writer(file)
            writer.writerow(name)
        file.close()

    # now to move it back to its own csv file
    def deletePlayer(self, playerID):
        input = open(filename, "r")
        output = open("players_edited.csv", "w")
        writer = csv.writer(output)
        for row in csv.reader(input):
            if row[0] != str(playerID):
                writer.writerow(row)
        input.close()
        output.close()

        shutil.move("players_edited.csv", filename)

    # Method for generating an ID for each player
    def generateId(self):
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
                names = lines.split(",")[1].strip("\n")
                table.add_row([ids, names])
        file.close()
        return table

    # Get a player's name from their ID
    def getName(self, playerID):
        with open(filename, "r") as file:
            reader = file.readlines()
            for lines in reader:
                # List of IDs
                if lines.split(",")[0] == playerID:
                    # Return the name
                    return lines.split(",")[1]
        file.close()

    def getID(self, name):
        with open(filename, "r") as file:
            reader = file.readlines()
            for lines in reader:
                if name == lines.split(",")[1].strip("\n"):
                    return lines.split(",")[0]
        file.close()

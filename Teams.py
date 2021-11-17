import csv
from os.path import exists

filename = "teams.txt"


class Teams:
    def __init__(self, playerID):
        self.playerID = playerID
        self.initializeFile()

    def initializeFile(self):
        # Create the file if it doesn't exist already as a failsafe
        if not exists(filename):
            with open(filename, "x") as file:
                file.close()

    def createTeam(self, team_name):
        with open(filename, "a") as file:
            file.write(team_name + "\n")

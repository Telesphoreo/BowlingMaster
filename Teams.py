import csv
from os.path import exists

filename = "teams.txt"
players_csv = "players.csv"


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

    def addPlayer(self, team_name):
        reader = open(players_csv, "r")
        print("got to reader")
        with open(players_csv, "a") as file:
            writer = csv.writer(file)
            for lines in reader.readlines():
                columns = lines.split(",")
                print(columns)
                print(lines)
                if columns[0] == self.playerID:
                    list = {self.playerID : [columns[0], columns[1], team_name]}
                    data = list.get(lines, lines)
                    writer.writerow(data)

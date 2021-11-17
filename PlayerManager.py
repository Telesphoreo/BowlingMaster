import csv
import shutil
from prettytable import from_db_cursor
from os.path import exists
import sqlite3

connection = sqlite3.connect("players.db")
cursor = connection.cursor()


class Player:
    def __init__(self):
        self.initializeDatabase()

    def initializeDatabase(self):
        tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='players'"
        if not cursor.execute(tb_exists).fetchone():
            cursor.execute(
                "CREATE TABLE players (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, team TEXT, strikes_per_game "
                "INTEGER, total_score INTEGER)")
        connection.commit()

    # Create a new player
    def createPlayer(self, name):
        cursor.execute("INSERT INTO players VALUES (NULL, ?, NULL, NULL, NULL)", (name,))
        connection.commit()


    # Delete a player
    def deletePlayer(self, playerID):
        cursor.execute("DELETE FROM players WHERE id = ?", (playerID,))
        connection.commit()

'''
    # List every player
    def listPlayers(self):



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
'''
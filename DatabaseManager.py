import re
from prettytable import from_db_cursor
import sqlite3

connection = sqlite3.connect("players.db")
cursor = connection.cursor()


def stripTuple(string):
    return re.sub("[^0-9]", "", str(string))


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

    # List every player
    def listPlayers(self):
        cursor.execute("SELECT id, name, team FROM players")
        list = from_db_cursor(cursor)
        return list

    def getName(self, playerID):
        try:
            result = cursor.execute(
                "SELECT name FROM players WHERE id = ?",
                (playerID,)).fetchall()
            return stripTuple(result)
        except IndexError:
            print("No player with that ID could be found.")


class Teams:
    def __init__(self):
        self.initializeDatabase()

    # Initialize the teams table
    def initializeDatabase(self):
        tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='teams'"
        if not cursor.execute(tb_exists):
            cursor.execute(
                "CREATE TABLE teams (name TEXT)")
        connection.commit()

    # Create a new team
    def createTeam(self, team):
        cursor.execute("INSERT INTO teams VALUES (?)", (team,))
        connection.commit()

    # Delete a team
    def deleteTeam(self, team):
        cursor.execute("DELETE FROM teams WHERE id = ?", (team,))
        connection.commit()

    # List every team name
    def listTeams(self):
        cursor.execute("SELECT name FROM teams")
        list = from_db_cursor(cursor)
        return list

    def addPlayerToTeam(self, playerID, team):
        cursor.execute("UPDATE players SET team = ? WHERE id = ?", (team, playerID,))
        connection.commit()

    def removePlayerFromTeam(self, playerID):
        cursor.execute("UPDATE players SET team = NULL WHERE id = ?", (playerID,))
        connection.commit()


class Points:
    def __init__(self, playerID, points, strikes):
        self.playerID = playerID
        self.points = points
        self.strikes = strikes

    def setScore(self):
        # Fetch strikes and total score
        db_strikes = cursor.execute(
            "SELECT strikes_per_game FROM players WHERE id = ?",
            (self.playerID,)).fetchall()
        db_total = cursor.execute(
            "SELECT total_score FROM players WHERE id = ?",
            (self.playerID,)).fetchall()

        # Strip tuple from operation
        strip_strikes = stripTuple(db_strikes)
        strip_total = stripTuple(db_total)
        print(strip_strikes)

        # Probably need additional checks here
        if strip_strikes == "":
            strip_strikes = 0
        if int(self.strikes) > 12:
            raise ValueError("The amount of strikes cannot be more than 12!")
        if strip_total == "":
            strip_total = 0
        if int(self.points) > 300:
            raise ValueError("The score cannot be more than 300!")

        # Add more to current strikes and total score
        new_strikes = int(strip_strikes) + int(self.strikes)
        new_total = int(strip_total) + int(self.points)

        # Execute operation
        cursor.execute("UPDATE players SET strikes_per_game = ?, total_score = ? WHERE id = ?",
                       (new_strikes, new_total, self.playerID))
        connection.commit()


def main():
    Points(1, 300, 12).setScore()


main()

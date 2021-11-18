from prettytable import from_db_cursor
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

    # List every player
    def listPlayers(self):
        cursor.execute("SELECT id, name, team FROM players")
        list = from_db_cursor(cursor)
        return list

    def getName(self, playerID):
        rows = cursor.execute(
            "SELECT name FROM players WHERE id = ?",
            (playerID,)).fetchall()
        return rows


class Teams:
    def __init__(self):
        self.initializeDatabase()

    # Initialize the teams table
    def initializeDatabase(self):
        tb_exists = "SELECT name FROM sqlite_master WHERE type='table' AND name='teams'"
        if not cursor.execute(tb_exists).fetchone():
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

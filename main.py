import DatabaseManager
from DatabaseManager import Player
from DatabaseManager import Teams
from DatabaseManager import Points
import DateManager
from datetime import date
import tkinter as tk
from tkinter import ttk, Entry, StringVar, messagebox, NSEW

def displayManageTeamsWindow():
    print("1 - Add Team")
    print("2 - Remove Team")
    print("3 - List Teams")
    print("4 - Add Player to Team")
    print("5 - Remove Player from Team")
    print("6 - Back")
    while True:
        menu_option = input("Please enter a command: ")
        if menu_option == "1":
            def addTeam():
                team_name = input("Please enter a team name: ")
                Teams().createTeam(team_name)
            break
        elif menu_option == "2":
            def deleteTeam():
                team_name = input("Please enter the team name you would like to delete: ")
                Teams().deleteTeam(team_name)
            break
        elif menu_option == "3":
            print(Teams().listTeams())
            break
        elif menu_option == "4":
            playerID = input("Enter the ID of the player you would like to modify: ")
            team_name = input("Enter the name of the team you would like to assign to the player: ")
            Teams().addPlayerToTeam(playerID, team_name)
            print("Added", Player().getName(playerID), "to team", team_name)
            break
        elif menu_option == "5":
            playerID = input("Enter the ID of the player you would like to remove from a team: ")
            Teams().removePlayerFromTeam(playerID)
            print("Removed", Player().getName(playerID), "from their team.")
            break
        elif menu_option == "6":
            main()
            break
        else:
            print("You did not enter a valid command.")


def displayMangePlayersMenu():
    print("1 - Add Player")
    print("2 - Remove Player")
    print("3 - List Players")
    print("4 - Back")

    while True:
        menu_option = input("Please enter a command: ")
        if menu_option == "1":
            name = input("Enter your new player's name: ")
            Player().createPlayer(name)
            print("Added new player:", name)
            print("Returning to main menu...")
            main()
            break
        elif menu_option == "2":
            playerID = input("Enter the ID of the player you would like to delete: ")
            name = Player().getName(playerID)
            Player().deletePlayer(playerID)
            print("Deleted player:", name)
            print("Returning to main menu...")
            main()
            break
        elif menu_option == "3":
            print(Player().listPlayers())
            break
        elif menu_option == "4":
            main()
            break
        else:
            print("You did not enter a valid command (player)")
        break


def displayManageScoresMenu():
    print("1 - Update score for player")
    print("2 - Reset score for player")
    print("3 - List all scores")
    print("4 - Back")
    while True:
        menu_option = input("Please enter a command: ")
        if menu_option == "1":
            playerID = input("Please enter the player's ID: ")
            points = input("Please enter the total score from the game: ")
            strikes = input("Please enter the total amount of strikes from the game: ")
            try:
                Points(playerID, int(points), int(strikes)).setScore()
            except ValueError:
                print("You must enter a valid number for all fields!")
                break
        elif menu_option == "2":
            playerID = input("Please enter the player's ID: ")
            Points(playerID, 0, 0).setScore()
            print("The score for player", Player().getName(playerID), "has been reset!")
            break
        elif menu_option == "3":
            print(Player().listScores())
        elif menu_option == "4":
            main()
            break
        else:
            print("You did not enter a valid command (other options)")
        break


def displayOtherOptionsMenu():
    print("1 - Set next tournament")
    print("2 - Back")

    while True:
        menu_option = input("Please enter a command: ")
        if menu_option == "1":
            date_input = input("Enter the date of the next tournament (YYYY-MM-DD): ")
            if DateManager.setDate(date_input):
                print("Next game date set! Returning to main menu...")
                print()
                main()
                break
            else:
                # i know this is bad, someone else fix it
                displayOtherOptionsMenu()
                break
        elif menu_option == "2":
            main()
            break
        else:
            print("You did not enter a valid command (other options)")
        break


def main():
    print("Bowling Manager")
    print()
    print("Today is:", date.today())
    DateManager.readDate()
    print()
    print("1 - Manage Teams")
    print("2 - Manage Players")
    print("3 - Manage Scores")
    print("4 - Other options")
    print("5 - Show All Players")
    print("6 - Exit")
    menu_option = input("Please enter a command: ")
    while True:
        if menu_option == "1":
            displayManageTeamsWindow()
            break
        elif menu_option == "2":
            displayMangePlayersMenu()
            break
        elif menu_option == "3":
            displayManageScoresMenu()
            break
        elif menu_option == "4":
            displayOtherOptionsMenu()
            break
        elif menu_option == "5":
            print(Player().listEverything())
            break
        elif menu_option == "6":
            print("Exiting program...")
            DatabaseManager.close()
            break
        else:
            print("You did not enter a valid command.")
            main()
            break

#GUI
class MyFrame(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        MyFrame.grid(self, in_=root, row=1, column=0, columnspan=3, sticky=NSEW)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(1, weight=1)
        self.pack()

        tk.Button(self, command = self.TeamsButtons, text="Manage Teams", bg="purple", fg="white").grid(column=0, row=0)
        tk.Button(self, command = self.PlayerButtons, text="Manage Players", bg="purple", fg="white").grid(column=0, row=1)
        tk.Button(self, command = self.ScoreButtons, text="Manage Scores", bg="purple", fg="white").grid(column=0, row=2)
        tk.Button(self, text="Other Options", bg="purple", fg="white").grid(column=0, row=3)
        tk.Button(self, text="Show All Players", bg="purple", fg="white").grid(column=0, row=4)
        tk.Button(self, text="About", bg="purple", fg="white").grid(column=0, row=5)
        tk.Button(self, text="Exit", bg="purple", fg="white").grid(column=0, row=6)

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

        self.team_name = StringVar()
        self.playerID = StringVar()
        self.name = StringVar()

    #team button functions

    def TeamsButtons(self):
        ttk.Frame.__init__(self, padding="10 10 10 10")
        self.pack()
        ttk.Button(self, text="Add Team").grid(column=1, row=0, sticky=tk.W)#, command=lambda: Teams().createTeam(team_name))
        ttk.Button(self, text="Remove Team").grid(column=1, row=1)#, command=lambda: Teams().deleteTeam(team_name))
        ttk.Button(self, text="List Teams").grid(column=1, row=2)#, command=lambda: print(Teams().listTeams()))
        ttk.Button(self, text="Add Player to Team").grid(column=1, row=3)#, command=lambda: Teams().addPlayerToTeam(playerID, team_name))
        ttk.Button(self, text="Remove Player from Team").grid(column=1, row=4)#, command=lambda: Teams().removePlayerFromTeam(playerID))
        ttk.Button(self, text="Back").grid(column=1, row=5)#, command=lambda: main())```

    #player button functions

    def PlayerButtons(self, playerID, name):
        ttk.Button(self, text="Add Player", command=lambda: Player().createPlayer(name))
        ttk.Button(self, text="Remove Player", command=lambda: Player().deletePlayer(playerID))
        ttk.Button(self, text="List All Players", command=lambda: print(Player().listPlayers()))
        ttk.Button(self, text="Back", command=lambda: main())

    def ScoreButtons(self, playerID, points, strikes):
        ttk.Button(self, text="Update Player Score", command=lambda: Points(playerID, int(points), int(strikes)).setScore())


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Bowling Master")
    MyFrame(root)
    root.mainloop()




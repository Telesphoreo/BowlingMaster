import DatabaseManager
from DatabaseManager import Player
from DatabaseManager import Teams
from DatabaseManager import Points
import DateManager
from datetime import date


def returnToMainMenu():
    print("Returning to main menu...")
    main()


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
            team_name = input("Please enter a team name: ")
            Teams().createTeam(team_name)
            returnToMainMenu()
            break
        elif menu_option == "2":
            team_name = input("Please enter the team name you would like to delete: ")
            Teams().deleteTeam(team_name)
            returnToMainMenu()
            break
        elif menu_option == "3":
            print(Teams().listTeams())
            displayManageTeamsWindow()
            break
        elif menu_option == "4":
            playerID = input("Enter the ID of the player you would like to modify: ")
            team_name = input("Enter the name of the team you would like to assign to the player: ")
            Teams().addPlayerToTeam(playerID, team_name)
            print("Added", Player().getName(playerID), "to team", team_name)
            returnToMainMenu()
            break
        elif menu_option == "5":
            playerID = input("Enter the ID of the player you would like to remove from a team: ")
            Teams().removePlayerFromTeam(playerID)
            print("Removed", Player().getName(playerID), "from their team.")
            returnToMainMenu()
            break
        elif menu_option == "6":
            main()
            break
        else:
            print("You did not enter a valid command.")
            displayManageTeamsWindow()
            break


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
            returnToMainMenu()
            break
        elif menu_option == "2":
            playerID = input("Enter the ID of the player you would like to delete: ")
            name = Player().getName(playerID)
            Player().deletePlayer(playerID)
            print("Deleted player:", name)
            returnToMainMenu()
            break
        elif menu_option == "3":
            print(Player().listPlayers())
            displayMangePlayersMenu()
            break
        elif menu_option == "4":
            main()
            break
        else:
            print("You did not enter a valid command.")
            displayMangePlayersMenu()
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
                Points(playerID, int(points), int(strikes)).addScore()
                returnToMainMenu()
                break
            except ValueError:
                print("You must enter a valid number for all fields!")
                break
        elif menu_option == "2":
            playerID = input("Please enter the player's ID: ")
            Points(playerID, 0, 0).setScore()
            print("The score for player", Player().getName(playerID), "has been reset!")
            returnToMainMenu()
            break
        elif menu_option == "3":
            print(Player().listScores())
            displayManageScoresMenu()
            break
        elif menu_option == "4":
            main()
            break
        else:
            print("You did not enter a valid command.")
            displayManageScoresMenu()
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
                displayOtherOptionsMenu()
                break
        elif menu_option == "2":
            main()
            break
        else:
            print("You did not enter a valid command.")
            displayOtherOptionsMenu()
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
            main()
            break
        elif menu_option == "6":
            print("Exiting program...")
            DatabaseManager.close()
            break
        else:
            print("You did not enter a valid command.")
            main()
            break


if __name__ == "__main__":
    main()

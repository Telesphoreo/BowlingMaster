from DatabaseManager import Player
from DatabaseManager import Teams
from DatabaseManager import Points
import DateManager
from datetime import date


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
            break
        elif menu_option == "2":
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
            playerID = input("Pleae enter the player's ID: ")
            points = input("Pleae enter the total score from the game: ")
            strikes = input("Pleae enter the total amount of strikes from the game: ")
            Points(playerID, int(points), int(strikes)).setScore()
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
    print("Next game:", DateManager.readDate())
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
            break
        # This is an infinite loop
        else:
            print("You did not enter a valid command.")


if __name__ == "__main__":
    main()

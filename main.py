from DatabaseManager import Player
from DatabaseManager import Teams
from datetime import date
import DateManager


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
        elif menu_option == "4":
            id = input("Enter the ID of the player you would like to modify: ")
            team_name = input("Enter the name of the team you would like to assign to the player: ")
            Teams().addPlayerToTeam(id, team_name)
            print("Added", Player().getName(id), "to team", team_name)
        elif menu_option == "5":
            id = input("Enter the ID of the player you would like to remove from a team: ")
            Teams().removePlayerFromTeam(id)
            print("Removed", Player().getName(id), "from their team.")
        elif menu_option == "6":
            main()
            break
        else:
            print("You did not enter a valid command (teams)")


def displayMangePlayersMenu():
    print("1 - Add Player")
    print("2 - Remove Player")
    print("3 - List Players")
    print("4 - Back")

    while True:
        menu_option = input("Please enter a command: ")
        pm = Player()
        if menu_option == "1":
            name = input("Enter your new player's name: ")
            pm.createPlayer(name)
            print("Added new player:", name)
            break
        elif menu_option == "2":
            id = input("Enter the ID of the player you would like to delete: ")
            name = pm.getName(id)
            pm.deletePlayer(id)
            print("Deleted player:", name)
            break
        elif menu_option == "3":
            print(pm.listPlayers())
            pass
        elif menu_option == "4":
            main()
            break
        else:
            print("You did not enter a valid command (player)")
        break


def displayOtherOptions():
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
                displayOtherOptions()
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
    print("3 - Other options")
    print("4 - Exit")
    menu_option = input("Please enter a command: ")
    while True:
        if menu_option == "1":
            displayManageTeamsWindow()
            break
        elif menu_option == "2":
            displayMangePlayersMenu()
            break
        elif menu_option == "3":
            displayOtherOptions()
            break
        elif menu_option == "4":
            print("Exiting program")
            break
        else:
            print("You did not enter a valid command.")


if __name__ == "__main__":
    main()

from PlayerManager import Player
from Teams import Teams
from datetime import date
import DateManager

def displayManageTeamsWindow():
    print("1 - Add Team")
    print("2 - Remove Team")
    print("3 - List Teams")
    print("4 - Add Player to Team")
    print("5 - Remove Player from Team")
    print("6 - Back to Main Menu")
    while True:
        menu_option = input("Please enter a command: ")
        if menu_option == "1":
            team_name = input("Please enter a team name: ")
            Teams("doesn't matter lol").createTeam(team_name)
            break
        elif menu_option == "2":
            print("Got to removing a team")
            break
        elif menu_option == "3":
            print("Got to listing teams")
            break
        elif menu_option == "4":
            main()
        else:
            print("You did not enter a valid command (teams)")


def displayMangePlayersMenu():
    print("1 - Add Player")
    print("2 - Remove Player")
    print("3 - List Players")
    print("4 - Back to Main Menu")
    print("5 - Exit")

    while True:
        menu_option = input("Please enter a command: ")
        pm = Player()
        if menu_option == "1":
            name = input("Enter your new player's name: ")
            pm.createPlayer(name)
            print("Added new player:", name)
        elif menu_option == "2":
            print("Got to removing a player")
            break
        elif menu_option == "3":
            print(pm.listPlayers())
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

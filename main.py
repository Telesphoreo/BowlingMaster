from PlayerManager import Player


def displayManageTeamsWindow():
    print("1 - Add Team")
    print("2 - Remove Team")
    print("3 - List Teams")
    while True:
        menu_option = input("Please enter a command: ")
        if menu_option == "1":
            print("Got to adding a team")
            break
        elif menu_option == "2":
            print("Got to removing a team")
            break
        elif menu_option == "3":
            print("Got to listing teams")
            break


def displayMangePlayersMenu():
    print("1 - Add Player")
    print("2 - Remove Player")
    print("3 - List Players")
    print("4 - Back to Main Menu")

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



def main():
    print("Bowling Manager")
    print("1 - Manage Teams")
    print("2 - Manage Players")
    menu_option = input("Please enter a command: ")
    while True:
        if menu_option == "1":
            displayManageTeamsWindow()
            break
        elif menu_option == "2":
            displayMangePlayersMenu()
            break
        else:
            print("You did not enter a valid command.")


if __name__ == "__main__":
    main()

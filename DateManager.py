from datetime import date, datetime
import os


def setDate(fileDate):
    try:
        fileDate = datetime.strptime(fileDate, "%Y-%m-%d")
    except ValueError:
        print("Error: The date you entered did not match the required format.")
        return False
    if fileDate.date() <= date.today():
        print("Error: The date you specified is before today.")
        return False
    with open("options.txt", mode='w') as file:
        file.write(str(fileDate.date()))
        file.close()

    return True


def readDate():
    try:
        if os.path.getsize("options.txt") == 0:
            print("Next game: Not set")

        with open("options.txt", "r") as file:
            for lines in file.readlines():
                splitDate = lines.split("-")
                newDate = date(year=int(splitDate[0]), month=int(splitDate[1]), day=int(splitDate[2]))
                newDate.strftime("%Y-%m-%d")
                if newDate <= date.today():
                    print("The next game has already happened! Resetting date...")
                    writer = open("options.txt", "w")
                    writer.write("")
                    writer.close()
                    return
                else:
                    delta = newDate - date.today()
                    print("Next game:", str(newDate) + "\n" + "Days until next game:", delta.days, "days")
        file.close()
    except FileNotFoundError:
        print("Next game: Not set")


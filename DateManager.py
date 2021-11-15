from datetime import datetime


def setDate(date):
    date = datetime.strptime(date, "%Y-%m-%d")
    if date < date.today():
        print("Error: The date you specified is before today.")
        return False
    with open("options.txt", mode='w') as file:
        file.write(str(date))
        return True


def readDate():
    try:
        with open("options.txt", mode='r') as file:
            for lines in file.readlines():
                date_only = lines.split(" ")
                return date_only[0]
    except FileNotFoundError:
        return "Not set"

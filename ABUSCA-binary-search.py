import time

array = -1
pangalan = 1
numero = 2
quit = 3

def main():
    menu_display()
    choice = 0
    while choice != quit:
        choice = int(input("Enter Your Choice: "))
        if choice == pangalan:
            google = input("Enter the name that you want to search for: ")
            result = search(names, google)
            if search(names, google):
                print("SEARCHING..........\n")
                time.sleep(2)
                print("The name", google, "which is", result, "is found at position", array+1)
            else:
                print("The name", google, " is not found in the list")
        elif choice == numero:
            searchnumber = int(input("Enter the number that you want to search for between 1-20: "))
            result = search2(numbering, searchnumber)
            if search2(numbering, searchnumber):
                print("SEARCHING..........\n")
                time.sleep(2)
                print("The number", searchnumber, "which is", result, "is found at position", array+1)
            else:
                print("The number", searchnumber, " is not found in the list")
        elif choice == quit:
            print("Exiting the program")
        else:
            print("Error: Invalid selection")

def search(names, google):
    i = 0
    u = len(names) - 1

    while i <= u:
        gitna = (i + u) // 2

        if names[gitna] == google:
            globals()['array'] = gitna
            return True
        elif names[gitna] < google:
            i = gitna + 1
        else:
            u = gitna - 1
    return False

def search2(numbering, searchnumber):

    i = 0
    u = len(numbering)-1

    while i <= u:
        gitna = (i + u) // 2

        if numbering[gitna] == searchnumber:
            globals()['array'] = gitna
            return True
        elif numbering[gitna] < searchnumber:
            i = gitna + 1
        else:
            u = gitna - 1
    return False

names = [
    "Bea", "Catriona", "Charice", "Corazon", "Gladys", "Hilda", "Julia", "Kathryn", "Kristine", "Lea",
    "Liza", "Maine", "Maja", "Marian", "Maricel", "Mariel", "Nadine", "Nora", "Sandara"]

numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def menu_display():
    print("Select what you want to Binary Search.")
    print("1) Search for First Names")
    print("2) Search for a Number")
    print("3) Quit")

main()
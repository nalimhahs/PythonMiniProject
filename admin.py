from db import Admin, Game


def manageAdmin():

    print(
        "Welcome To the stadium ticket booking system!\nAdmin Menu\n"
        "1. Manage Ticketing \n"
        "2. Manage Games\n"
        "3. Exit\n"
    )

    choice = int(input("Enter your choice: "))

    if choice == 1:
        manageTickets()
    elif choice == 2:
        manageGames()
    elif choice == 3:
        print()
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageAdmin()


def manageTickets():
    print(
        "Welcome To the stadium ticket booking system!\nAdmin Menu\nManage Tickets\n"
        "1. View all bookings\n"
        "2. Remove ticket\n"
        "3. Edit ticket\n"
        "4. Reset\n"
        "5. Exit\n"
    )

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print()
    elif choice == 2:
        print()
    elif choice == 3:
        print()
    elif choice == 4:
        exit(0)
    elif choice == 5:
        exit(0)
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageTickets()


def manageGames():

    print(
        "Welcome To the stadium ticket booking system!\nAdmin Menu\nManage Games\n"
        "1. View all Games\n"
        "2. Add Game\n"
        "3. Remove Game\n"
        "4. Edit Game\n"
        "5. Reset\n"
        "6. Exit\n"
    )

    choice = int(input("Enter your choice: "))

    game = Game()

    if choice == 1:
        game.viewGames()

    elif choice == 2:
        gameName = input('Enter game Name: ')
        date = input('Enter game Date: ')
        time = input('Enter game Time: ')
        game.addGame(gameName,date,time)
    elif choice == 3:
        gID = input('Enter game ID to remove: ')
        game.removeGame(gID)
    elif choice == 4:
        gID = input('Enter game ID to Edit: ')
        game.editGame(gID) 
    elif choice == 5:
        game.resetTable()
    elif choice == 6:
        return
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageGames()

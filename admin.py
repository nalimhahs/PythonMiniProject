from db import Admin, Game, User


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
        return
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageAdmin()
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

    admin = Admin()

    if choice == 1:
        print('\nAll Bookings:\n')
        admin.viewAllUsersAdmin()
    elif choice == 2:
        bkNo = input('Enter ticket no to edit: ')
        user = User()
        if user.verify(bkNo) == 0:
            print('Invalid Booking Number: ')
            return 0
        else:
            admin.removeTicketAdmin()
    elif choice == 3:
        bkNo = input('Enter ticket no to edit: ')
        user = User()
        if user.verify(bkNo) == 0:
            print('Invalid Booking Number: ')
            return 0
        else:
            admin.editTicketAdmin(bkNo)
    elif choice == 4:
        exit(0)
    elif choice == 5:
        exit(0)
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageTickets()
    manageTickets()


def manageGames():

    print(
        "\n\nWelcome To the stadium ticket booking system!\nAdmin Menu\nManage Games\n"
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
        try: 
            game.removeGame(gID)
        except:
            print('\nGame not found!\n')
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
    manageGames()

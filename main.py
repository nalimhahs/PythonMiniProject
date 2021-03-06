from booking import book
from user import manageUser
from admin import manageAdmin

def mainMenu():

    print(
        "\n\nWelcome To the stadium ticket booking system!\n"
        "1. Book Tickets\n"
        "2. Manage my bookings\n"
        "3. Admin Login\n"
        "4. Exit\n"
    )
    try:
        choice = int(input("Enter your choice: "))
    except:
        print('\n\nThe Choice you entered is invalid!\nPlease Try Again!!\n')
        mainMenu()        

    if choice == 1:
        book()
    elif choice == 2:
        bkNo = input('Enter your Booking no: ')
        if manageUser(bkNo) == 0:
            print('\nInvalid Ticket Number!\n')
            mainMenu()
        else:
            pass
    elif choice == 3:
        manageAdmin()
    elif choice == 4:
        print('\n\nBye!\n\n')
        exit(0)
    else:
        print('\n\nThe Choice you entered is invalid!\nPlease Try Again!!\n')


while True:
    mainMenu()
from db import User

def manageUser(bkNo):

    user = User()

    if user.verify(bkNo) == 0:
        print('Invalid Booking Number: ')
        return 0


    print(
        "\n\nWelcome To the stadium ticket booking system!\nUser Menu\n"
        "1. View my booking\n"
        "2. Cancel ticket\n"
        "3. Edit details\n"
        "4. Back\n"
    )

    choice = int(input("Enter your choice: "))


    if choice == 1:
        user.viewUser(bkNo)
    elif choice == 2:
        user.removeTicket(bkNo)
        print('\nTicket deleted Sucessfully!\n')
        return 1
    elif choice == 3:
        user.editTicket(bkNo)
    elif choice == 4:
        return 1
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageUser(bkNo)

    manageUser(bkNo)

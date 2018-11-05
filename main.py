from booking import book
from user import manageUser
from admin import manageAdmin

def mainMenu():

    print(
        "Welcome To the stadium ticket booking system!\n"
        "1. Book Tickets\n"
        "2. Manage my bookings\n"
        "3. Admin Login\n"
        "4. Exit\n"
    )

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book()
    elif choice == 2:
        manageUser()
    elif choice == 3:
        manageAdmin()
    elif choice == 4:
        exit(0)
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')


while True:
    mainMenu()
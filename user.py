def manageUser():

    print(
        "Welcome To the stadium ticket booking system!\nUser Menu\n"
        "1. View my bookings\n"
        "2. Cancel ticket\n"
        "3. Edit details\n"
        "4. Back\n"
    )

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print()
    elif choice == 2:
        print()
    elif choice == 3:
        print()
    elif choice == 4:
        return
    else:
        print('The Choice you entered is invalid!\nPlease Try Again!!\n')
        manageUser()

from db import User, Game

def getSeatType():

    seatTypes = ['A', 'B', 'C', 'D']
    sType = input(
        'Enter your seat class\n'
        'A - A/C VIP Lounge ------------------------ 200\n'
        'B -                                         100\n'
        'C -                                         50\n'
        'D -                                         25\n'
        'Your Choice: '
    )
    if sType not in seatTypes:
        print('The Seat Class you entered is invalid!\nPlease Try Again!!\n')
        getSeatType()
    
    return sType


def getMatch():

    game = Game()
    mID = int(input('Enter match you want to book for: '))
    game.gameVerify(mID)
    if game.gameVerify(mID):
        print('The match id you entered is invalid!\nPlease Try Again!!\n')
        getMatch()

    return mID

def getSeat(user, sType,matchID):

    seatNo = int(input("Enter your required seat no: "))
    if user.checkSeat(seatNo,sType,matchID):
        print('Yaay seat available!')
        return seatNo
    else:
        print('The seat number you asked for is already booked!!\nTry another seat.\n')


def book():

    user = User()
    name = input('Enter your Name: ')
    age = int(input('Enter your age: '))
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    sType = getSeatType()
    matchID = getMatch()
    seatNo = getSeat(user, sType, matchID)
    print('Getting your ticket ready...')
    ticketNo = user.addTicket(matchID,name,age,phone,email,sType,seatNo)
    print(
        'Done\n'
        'Here is your ticket number: ' + str(ticketNo) +
        '\nKeep it safe for further uses.\n'
    )
    



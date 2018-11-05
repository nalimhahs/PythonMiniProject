from db import *


seatTypes = ['A', 'B', 'C', 'D']


def getSeatType():

    sType = input(
        'Enter your seat class\n'
        'A - A/C VIP Lounge ------------------------ 200\n'
        'B -                                         100\n'
        'C -                                         50\n'
        'D -                                         25\n'
        'Your Choice: '
    )
    if sType not in seatTypes:
        print('The Seat Class you entered is invalid!\nPlease Try Again!!')
        getSeatType()
    
    return sType


def getMatch():

    mID = input('Enter match you want to book for: ')
    if gameVerify(mID):
        print('The match id you entered is invalid!\nPlease Try Again!!')
        getMatch()

    return mID

def getSeat(sType,matchID):

    seatNo = input("Enter your required seat no: ")
    if checkSeat(seatNo,sType,matchID):
        print('Yaay seat available!')
        return seatNo
    else:
        print('The seat number you asked for is already booked!!\nTry another seat.')


def getData():

    name = input('Enter your Name: ')
    age = int(input('Enter your age: '))
    email = input('Enter your Email: ')
    phone = input('Enter your Phone: ')
    sType = getSeatType()
    matchID = getMatch()
    seatNo = getSeat(sType,matchID)
    addTicket(matchID,name,age,phone,email,sType,seatNo)
    



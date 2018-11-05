
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

    #read data base
    #get match id
    matchID = []
    mID = input('Enter match you want to book for: ')
    if mID not in matchID:
        print('The match id you entered is invalid!\nPlease Try Again!!')
        getMatch()

    return mID


def getData():

    name = input('Enter your Name: ')
    age = int(input('Enter your age: '))
    sType = getSeatType()
    matchID = getMatch()
    



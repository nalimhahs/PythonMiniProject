import sqlite3


#Create a DB
db = sqlite3.connect('test.db')  #Create a new database after test case!!
cursor = db.cursor()


"""
#Create a table

print("Opened database successfully")

db.execute('''CREATE TABLE tickets
         (TICKETNO      TEXT     PRIMARY KEY     NOT NULL,
         GAMEID         INT     SECONDARY KEY   NOT NULL,
         NAME           TEXT                    NOT NULL,
         AGE            INT                     NOT NULL,
         PHONE          INT                     NOT NULL,
         EMAIL          EMAIL                   NOT NULL,
         SEATCLASS      CHAR                    IN("A","B","C","D"),
         SEATNO         INT                     NOT NULL);''')

print ("Table created successfully")

"""



def addTicket(gameId, name, age, phone, email, seatClass, seatNo):
    ticketNo = str(gameId) + seatClass + str(seatNo) 
    cursor.execute('''INSERT INTO tickets (TICKETNO, GAMEID, NAME, AGE, PHONE, EMAIL, SEATCLASS, SEATNO) 
                     VALUES(?,?,?,?,?,?,?,?)''', (ticketNo, gameId, name, age, phone, email, seatClass, seatNo))
    db.commit()
    return ticketNo


def editTicket(tkNo):
    print(
        "What do want to edit?\n"
        "1. Name\n"
        "2. Age\n"
        "3. Phone\n"
        "4. Email\n"
        "5. Back\n"
    )

    choice = int(input("Enter your choice: "))

    if choice == 1:
        cursor.execute('''UPDATE tickets SET NAME = ? WHERE id = ?''', (input('Enter new name: '),tkNo))
    elif choice == 2:
        cursor.execute('''UPDATE tickets SET AGE = ? WHERE id = ?''', (int(input('Enter new Age: ')),tkNo)) 
    elif choice == 3:
        cursor.execute('''UPDATE tickets SET PHONE = ? WHERE id = ?''', (int(input('Enter new Phone: ')),tkNo))
    elif choice == 4:
        cursor.execute('''UPDATE tickets SET EMAIL = ? WHERE id = ?''', (input('Enter new Email: '),tkNo))
    elif choice == 5:
        return
    else:
        print('Invalid Choice!')
        editTicket(tkNo)

    if input('Are you sure you want to update? (Y/N)') == 'Y':
        db.commit()
    else:
        print('Not Updated!')
        db.rollback()

def removeTicket(tkNo):
    cursor.execute('''DELETE FROM tickets WHERE TICKETNO = ?''', (tkNo))
    if input('Are you sure? (Y/N)') == 'Y':
        db.commit()
    else:
        print('Not deleted!')
        db.rollback()

def viewUser(bkNo):
    cursor.execute('''SELECT * FROM tickets WHERE TICKETNO = ?''', (bkNo))
    for row in cursor:
        #parse data later...
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))


def checkSeat(seatNo, sType, matchID):
    cursor.execute('''SELECT SEATNO FROM tickets WHERE SEATNO = ? AND SEATCLASS  = ? AND GAMEID = ? ''', (seatNo, sType, matchID))
    for row in cursor:
        if row[0] == seatNo:
            return 1
        else:
            return 0


###########################################################################
#                                                                         #
#                                                                         #
#                                                                         #
#                             ADMIN Powers :)                             #
#                                                                         #
#                                                                         #
#                                                                         #
###########################################################################


def viewAllUsersAdmin():
    cursor.execute('''SELECT * FROM tickets''')
    for row in cursor:
        #parse data later...
        print('{0} : {1}, {2}'.format(row[0], row[1], row[2]))



def removeTicketAdmin():
    bkNo = input('Enter booking no to modify: ')
    cursor.execute('''DELETE FROM tickets WHERE TICKETNO = ?''', (bkNo))
    if input('Are you sure? (Y/N)') == 'Y':
        db.commit()
    else:
        print('Not deleted!')
        db.rollback()

def editTicketAdmin(bkNo):
    cursor.execute('''UPDATE tickets SET phone = ? WHERE id = ?''', (0,bkNo))
    if input('Are you sure? (Y/N)') == 'Y':
        db.commit()
    else:
        print('Not Updated!')
        db.rollback()

def resetAdmin():
    cursor.execute('''DROP TABLE tickets''')
    if input('DYWTC?(Y/N): ') == 'Y':
        db.commit()
    else:
        db.rollback()


####################################################################################


#                                  Game Menu


####################################################################################


"""
#Create a table

print("Opened database successfully")

db.execute('''CREATE TABLE gameTable
         (GAMEID       INT      PRIMARY KEY     NOT NULL,
         GAMENAME      TEXT                     NOT NULL,
         DATE          INT                      NOT NULL,
         TIME          CHAR(50)                 NOT NULL;''')

print ("Table created successfully")

"""


def addGame(gameName, date, time):
    cursor.execute('''INSERT INTO gameTable(GAMENAME, DATE, TIME) 
                     VALUES(?,?,?,?)''', (gameName,date,time))
    db.commit()


def editGame(gameId):
    cursor.execute('''UPDATE gameTable SET phone = ? WHERE id = ?''', (0,gameId))
    if input('Are you sure? (Y/N)') == 'Y':
        db.commit()
    else:
        print('Not Updated!')
        db.rollback()

def removeGame(gameId):
    cursor.execute('''DELETE FROM gameTable WHERE GAMENO = ?''', (gameId))
    if input('Are you sure? (Y/N)') == 'Y':
        db.commit()
    else:
        print('Not deleted!')
        db.rollback()

def viewGames():
    cursor.execute('''SELECT * FROM gameTable ''', ())
    for row in cursor:
        print('ID: {0}\nName: {1}\nDate: {2}\tTime: {3}'.format(row[0], row[1], row[2],row[3]))

def gameVerify(gameId):
    cursor.execute('''SELECT GAMEID FROM gameTable WHERE GAMEID = ?''', (gameId))
    for row in cursor:
        if row[0] == gameId:
            return 1
        else:
            return 0


db.close()
import sqlite3

class User:

    def __init__(self):

        self.db = sqlite3.connect('test.db')  #Create a new database after test case!!
        try:
            self.db.execute('''CREATE TABLE tickets
                    (TICKETNO      TEXT     PRIMARY KEY     NOT NULL,
                    GAMEID         INT     SECONDARY KEY   NOT NULL,
                    NAME           TEXT                    NOT NULL,
                    AGE            INT                     NOT NULL,
                    PHONE          INT                     NOT NULL,
                    EMAIL          TEXT                    NOT NULL,
                    SEATCLASS      CHAR                    CHECK(SEATCLASS IN("A","B","C","D")),
                    SEATNO         INT                     NOT NULL);''')
        except:
            pass
        finally:
            self.cursor = self.db.cursor()

    def addTicket(self, gameId, name, age, phone, email, seatClass, seatNo):
        ticketNo = str(gameId) + seatClass + str(seatNo) 
        self.cursor.execute('''INSERT INTO tickets (TICKETNO, GAMEID, NAME, AGE, PHONE, EMAIL, SEATCLASS, SEATNO) 
                        VALUES(?,?,?,?,?,?,?,?)''', (ticketNo, gameId, name, age, phone, email, seatClass, seatNo,))
        self.db.commit()
        return ticketNo


    def editTicket(self, tkNo):
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
            self.cursor.execute('''UPDATE tickets SET NAME = ? WHERE id = ?''', (input('Enter new name: '),tkNo))
        elif choice == 2:
            self.cursor.execute('''UPDATE tickets SET AGE = ? WHERE id = ?''', (int(input('Enter new Age: ')),tkNo)) 
        elif choice == 3:
            self.cursor.execute('''UPDATE tickets SET PHONE = ? WHERE id = ?''', (int(input('Enter new Phone: ')),tkNo))
        elif choice == 4:
            self.cursor.execute('''UPDATE tickets SET EMAIL = ? WHERE id = ?''', (input('Enter new Email: '),tkNo))
        elif choice == 5:
            return
        else:
            print('Invalid Choice!')
            self.editTicket(tkNo)

        if input('Are you sure you want to update? (Y/N)') == 'Y':
            self.db.commit()
        else:
            print('Not Updated!')
            self.db.rollback()

    def removeTicket(self, tkNo):
        self.cursor.execute('''DELETE FROM tickets WHERE TICKETNO = ?''', (tkNo))
        if input('Are you sure? (Y/N)') == 'Y':
            self.db.commit()
        else:
            print('Not deleted!')
            self.db.rollback()
    def viewUser(self, bkNo):
        self.cursor.execute('''SELECT * FROM tickets WHERE TICKETNO = ?''', (bkNo,))
        for row in self.cursor:
            print(
                '\nTicket Number: {0}\nName: {1}\tAge: {2}\nPhone: {3}\nEmail: {4}\nSeat Class: {5}\tSeat Number: {6}'.format(row[0], row[2], row[3], row[4], row[5], row[6], row[7])
            )
            print('\nGame Details: \n')
            game = Game()
            game.viewGames(row[1])



    def checkSeat(self, seatNo, sType, matchID):
        self.cursor.execute('''SELECT SEATNO FROM tickets WHERE SEATNO = ? AND SEATCLASS  = ? AND GAMEID = ? ''', (seatNo, sType, matchID))
        for row in self.cursor:
            if row[0] == seatNo:
                return 1
            else:
                return 0

    def verify(self, ticketNo):
        self.cursor.execute('''SELECT TICKETNO FROM tickets WHERE TICKETNO = ?''', (ticketNo))
        for row in self.cursor:
            if row[0] == ticketNo:
                return 1
            else:
                return 0

    def __del__(self):
        self.db.close()


###########################################################################
###########################################################################


class Admin:

    def __init__(self):
        
        self.db = sqlite3.connect('test.db')  #Create a new database after test case!!
        try:
            self.db.execute('''CREATE TABLE tickets
                    (TICKETNO      TEXT     PRIMARY KEY     NOT NULL,
                    GAMEID         INT     SECONDARY KEY   NOT NULL,
                    NAME           TEXT                    NOT NULL,
                    AGE            INT                     NOT NULL,
                    PHONE          INT                     NOT NULL,
                    EMAIL          TEXT                    NOT NULL,
                    SEATCLASS      CHAR                    CHECK(SEATCLASS IN("A","B","C","D")),
                    SEATNO         INT                     NOT NULL);''')
        except:
            pass
        finally:
            self.cursor = self.db.cursor()


    def viewAllUsersAdmin(self):
        self.cursor.execute('''SELECT * FROM tickets''')
        for row in self.cursor:
            print(
                '\nTicket Number: {0}\nName: {1}\tAge: {2}\nPhone: {3}\nEmail: {4}\nSeat Class: {5}\tSeat Number: {6}'.format(row[0], row[2], row[3], row[4], row[5], row[6], row[7])
            )
            print('\nGame Details: \n')
            game = Game()
            game.viewGames(row[1])

    def removeTicketAdmin(self):
        bkNo = input('Enter booking no to Remove: ')
        self.cursor.execute('''DELETE FROM tickets WHERE TICKETNO = ?''', (bkNo))
        if input('Are you sure? (Y/N)') == 'Y':
            self.db.commit()
        else:
            print('Not deleted!')
            self.db.rollback()

    def editTicketAdmin(self, bkNo):
        self.cursor.execute('''UPDATE tickets SET phone = ? WHERE id = ?''', (0,bkNo))
        if input('Are you sure? (Y/N)') == 'Y':
            self.db.commit()
        else:
            print('Not Updated!')
            self.db.rollback()

    def resetAdmin(self):
        self.cursor.execute('''DROP TABLE tickets''')
        if input('DYWTC?(Y/N): ') == 'Y':
            self.db.commit()
        else:
            self.db.rollback()

    def __del__(self):
        self.db.close()


####################################################################################
####################################################################################


class Game:

    def __init__(self):

        self.db = sqlite3.connect('test.db') 
        try:
            self.db.execute('''CREATE TABLE gameTable
                (GAMEID       INTEGER      PRIMARY KEY     AUTOINCREMENT,
                GAMENAME      TEXT                     NOT NULL,
                DATE          TEXT                      NOT NULL,
                TIME          CHAR(7)                 NOT NULL);''')
        except:
            pass
        finally:
            self.cursor = self.db.cursor()

    def addGame(self, gameName, date, time):
        self.cursor.execute('''INSERT INTO gameTable(GAMENAME, DATE, TIME) 
                        VALUES(?,?,?)''', (gameName,date,time)) 
        self.db.commit()


    def editGame(self, gameId):
        
        if self.gameVerify(gameId) != 1:
            print('Invalid Game ID!')
            return

        print(
            "What do want to edit?\n"
            "1. Game Name\n"
            "2. Date\n"
            "3. Time\n"
            "4. Exit\n"
        )

        choice = int(input("Enter your choice: "))

        if choice == 1:
            self.cursor.execute('''UPDATE gameTable SET GAMENAME = ? WHERE GAMEID = ?''', (input('Enter new Game Name: '),gameId))
        elif choice == 2:
            self.cursor.execute('''UPDATE gameTable SET DATE = ? WHERE GAMEID = ?''', (int(input('Enter new Date: ')),gameId)) 
        elif choice == 3:
            self.cursor.execute('''UPDATE gameTable SET TIME = ? WHERE GAMEID = ?''', (int(input('Enter new Time: ')),gameId))
        elif choice == 4:
            return
        else:
            print('Invalid Choice!')
            self.editGame(gameId)

        if input('Are you sure you want to update? (Y/N)') == 'Y':
            self.db.commit()
        else:
            print('Not Updated!')
            self.db.rollback()

    def removeGame(self, gameId):
        self.cursor.execute('''DELETE FROM gameTable WHERE GAMEID = ?''', (gameId,))
        if input('Are you sure? (Y/N)') == 'Y':
            self.db.commit()
        else:
            print('Not deleted!')
            self.db.rollback()

    def viewGames(self, ID = 0):
        if ID != 0:
            self.cursor.execute('''SELECT * FROM gameTable WHERE GAMEID = ? ''',(ID,))
            for row in self.cursor:
                print('Game-ID: {0}\nName: {1}\nDate: {2}\tTime: {3}'.format(row[0], row[1], row[2],row[3]))
        else:        
            self.cursor.execute('''SELECT * FROM gameTable ''')
            for row in self.cursor:
                print('Game-ID: {0}\nName: {1}\nDate: {2}\tTime: {3}'.format(row[0], row[1], row[2],row[3]))

    def gameVerify(self, gameId):
        self.cursor.execute('''SELECT GAMEID FROM gameTable WHERE GAMEID = ?''', (gameId,))
        for row in self.cursor:
            if row[0] == gameId:
                return 1
            else:
                return 0

    def resetTable(self):
        self.cursor.execute('''DROP TABLE gameTable''')
        if input('DYWTC?(Y/N): ') == 'Y':
            self.db.commit()
        else:
            self.db.rollback()

    def __del__(self):
        self.db.close()



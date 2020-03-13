import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()


def main():
    q = 1
    try:
        initializeDataBase()
    except:
        pass
    while(q == 1):
        choice = userInput()
        if choice == 1:
            website = input('website => ')
            userName = input('user name => ')
            passwd = input('password => ')
            id = input('id => ')
            account = Account(
                website=website, userName=userName, passwd=passwd, id=id)
            addAccount(account)
        elif choice == 2:
            id = input('id => ')
            deleteAccount(id)
        elif choice == 3:
            website = input('website => ')
            account = Account(website=website)
            searchAccount(account)
        elif choice == 4:
            passwd = input('new password => ')
            id = input('account id => ')
            account = Account(passwd=passwd, id=id)
            updatePasswd(account)
        else:
            q = 0


def userInput():
    print('''
1 => add account
2 => delete account
3 => read all accounts
4 => update account
0 => quit
    ''')
    choice = int(input('choice => '))
    return choice


def initializeDataBase():
    c.execute('''CREATE TABLE accounts(
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            website TEXT NOT NULL,
            user_name TEXT NOT NULL,
            passwd TEXT NOT NULL)''')


def searchAccount(account):
    for row in c.execute('SELECT * FROM accounts where website = ?', [account.website]):
        print(row)


def addAccount(account):
    c.execute('INSERT INTO accounts VALUES (?,?,?,?)',
              [account.id, account.website, account.userName, account.passwd])
    conn.commit()


def updatePasswd(account):
    c.execute('''UPDATE accounts SET passwd = ?
                    WHERE account_id = ?''', [account.passwd, account.id])
    conn.commit()


def deleteAccount(id):
    c.execute('DELETE from accounts WHERE account_id = ?', [id])
    conn.commit()


class Account:
    def __init__(self, id=None, website=None, userName=None, passwd=None):
        self.id = id
        self.website = website
        self.userName = userName
        self.passwd = passwd


if __name__ == "__main__":
    main()
    conn.close()

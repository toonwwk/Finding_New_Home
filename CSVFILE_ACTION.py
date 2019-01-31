import abc
import csv
from tempfile import NamedTemporaryFile
import shutil
import base64
@abc.abstractmethod
class CsvFile(metaclass = abc.ABCMeta):
    def __init__(self, filename = '', headerfile = '', username = '', password = '', firstname = '', lastname = '', \
                 email = '', phone = '', cardnumber = '', cvv = '', tombnumber = '', nameontomb = '', service= ''):
        self.filename = filename
        self.headerfile = headerfile
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.phone = phone
        self.cardnumber = cardnumber
        self.cvv = cvv
        self.tombnumber = tombnumber
        self.nameontomb = nameontomb
        self.service = service

    @abc.abstractmethod
    def readFile(self):
        pass
    def writeFile(self):
        pass
    def updateFile(self):
        pass

class LoginFile(CsvFile):
    def __init__(self, filename = '', headerfile = '', username = '', password = ''):
        super().__init__(filename, headerfile, username, password)
    def checkLogin(self):

        check_login = False
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[0]] == self.username and row[self.headerfile[1]] == self.password):
                    print('login successfully')
                    check_login = True
                    break
        return check_login

    def readFile(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[0]] == self.username):
                    return row[self.headerfile[0]], row[self.headerfile[1]], row[self.headerfile[2]], \
                           row[self.headerfile[3]], row[self.headerfile[4]], row[self.headerfile[5]], \
                           row[self.headerfile[6]], row[self.headerfile[7]], row[self.headerfile[8]], \
                           row[self.headerfile[9]], row[self.headerfile[10]]

        return '','','','','','','','','none','none','nnnnnn'



class SignupFile(CsvFile):
    def __init__(self, newRow, filename = '', headerfile = '', username = '', password = '', firstname = '', \
                 lastname = '', email = '', phone = '', cardnumber = '', cvv = '', tombnumber = '', nameontomb = '', \
                 service = '',):
        super().__init__(filename, headerfile, username, password, firstname, lastname, email, phone, cardnumber, cvv, \
                         tombnumber, nameontomb, service)
        self.newRow = newRow

    def readFile(self):
        check = True
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[0]] == self.username):
                    check = False
        if(check):
            self.writeFile()
        return check

    def writeFile(self):
        with open(self.filename, 'a') as csvfile:
            csvfile.write(self.newRow)
        print('Signup successfully.')





class ManageAccountFile(CsvFile):
    def __init__(self, filename = '', headerfile = '', username = '', password = '', firstname = '', lastname = '', \
                 email = '', phone = '', cardnumber = '', cvv = '', tombnumber = '', nameontomb = '', service = ''):
        super().__init__(filename, headerfile, username, password, firstname, lastname, email, phone, cardnumber, cvv, \
                         tombnumber, nameontomb, service)

    def readFile(self):
        pass
    def writeFile(self):
        pass
    def updateFile(self):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(self.filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            writer = csv.DictWriter(tempfile, fieldnames=self.headerfile)

            for row in reader:
                if row[self.headerfile[0]] == self.username:
                    row[self.headerfile[0]] = str(self.username)
                    row[self.headerfile[1]] = str(self.password)
                    row[self.headerfile[2]] = str(self.firstname)
                    row[self.headerfile[3]] = str(self.lastname)
                    row[self.headerfile[4]] = str(self.email)
                    row[self.headerfile[5]] = str(self.phone)
                    row[self.headerfile[6]] = str(self.cardnumber)
                    row[self.headerfile[7]] = str(self.cvv)
                    row[self.headerfile[8]] = str(self.tombnumber)
                    row[self.headerfile[9]] = str(self.nameontomb)
                    row[self.headerfile[10]] = str(self.service)
                row = {'username': row['username'], 'password': row['password'], 'firstname': row['firstname'],
                       'lastname': row['lastname'], 'email': row['email'], 'phone': row['phone'],
                       'cardnumber': row['cardnumber'], 'cvv': row['cvv'], 'tombnumber': row['tombnumber'],
                       'nameontomb': row['nameontomb'], 'service': row['service']}
                if (row[self.headerfile[0]] != ''):
                    writer.writerow(row)
        shutil.move(tempfile.name, self.filename)

class BuyaTombFile(CsvFile):
    def __init__(self, filename, headerfile,username):
        super().__init__(filename, headerfile, username)

    def readFile(self):
        labelText=[]
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[1]] == '1'):
                    labelText.append(row[self.headerfile[0]])
                elif (row[self.headerfile[1]] == '0'):
                    labelText.append('S O L D')
        return labelText

class ConfirmFile(CsvFile):
    def __init__(self, filename, headerfile , username, cardnumber, cvv, tombnumber, nameontomb):
        super().__init__(filename, headerfile, username)
        self.cardnumber = cardnumber
        self.tombnumber = tombnumber
        self.cvv = cvv
        self.nameontomb = nameontomb

    def readFile(self):
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[0]] == self.tombnumber):
                    return row[self.headerfile[2]]
    def writeFile(self):
        pass
    def updateFile(self):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(self.filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            writer = csv.DictWriter(tempfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[0]] == self.tombnumber):
                    row[self.headerfile[1]] = '0'
                    temp = self.username.encode('ascii')
                    temp = base64.b64encode(temp)
                    temp = str(temp).replace('\'' , '')
                    row[self.headerfile[2]] = temp
                row = {'tombnumber': row['tombnumber'], 'available': row['available'], 'invitationcode': row['invitationcode']}
                if (row[self.headerfile[0]] != ''):
                    writer.writerow(row)
        shutil.move(tempfile.name, self.filename)

    def updateFile2(self):
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        header = ['username', 'password', 'firstname', 'lastname', 'email', 'phone', 'cardnumber', 'cvv', 'tombnumber',\
                  'nameontomb', 'service']
        with open('userinfo.csv', 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=header)
            writer = csv.DictWriter(tempfile, fieldnames=header)
            for row in reader:
                print(row[header[0]], self.username)
                if (row[header[0]] == self.username):
                    row[header[0]] = str(self.username)
                    row[header[6]] = str(self.cardnumber)
                    row[header[7]] = str(self.cvv)
                    row[header[8]] = str(self.tombnumber)
                    row[header[9]] = str(self.nameontomb)
                row = {'username': row['username'], 'password': row['password'], 'firstname': row['firstname'],
                       'lastname': row['lastname'], 'email': row['email'], 'phone': row['phone'],
                       'cardnumber': row['cardnumber'], 'cvv': row['cvv'], 'tombnumber': row['tombnumber'],
                       'nameontomb': row['nameontomb'], 'service': row['service']}
                if(row[header[0]] != ''):
                    writer.writerow(row)
        shutil.move(tempfile.name, 'userinfo.csv')


class TombManagementFile(CsvFile):
    def __init__(self, filename, headerfile, tombnumber):
        super().__init__(filename, headerfile)
        self.tombnumber = tombnumber

    def readFile(self):
        selecteddate = {}
        with open(self.filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[0]] == self.tombnumber):
                    try:
                        selecteddate[row[self.headerfile[2]]] += 1
                    except:
                        selecteddate[row[self.headerfile[2]]] = 1
        if len(selecteddate) ==  0:
            howmany = 0
        else:
            howmany = max(selecteddate.values())

        date = ''
        for a, b in selecteddate.items():
            if (b == howmany):
                date += (a)
                date += ' '
        return date, howmany

    def writeFile(self, newrow):
        pass

    def updateFile(self, username, choosedate):
        self.username = username
        self.choosedate = choosedate
        check = True
        tempfile = NamedTemporaryFile(mode='w', delete=False)
        with open(self.filename, 'r') as csvfile, tempfile:
            reader = csv.DictReader(csvfile, fieldnames=self.headerfile)
            writer = csv.DictWriter(tempfile, fieldnames=self.headerfile)
            for row in reader:
                if (row[self.headerfile[1]] == self.username):
                    row[self.headerfile[2]] = self.choosedate
                    check = False
                row = {'tombnumber': row['tombnumber'], 'username': row['username'], 'date': row['date']}
                writer.writerow(row)
        shutil.move(tempfile.name, self.filename)

        if(check):
            newrow = self.tombnumber+','+self.username+','+self.choosedate
            with open(self.filename, 'a') as csvfile:
                csvfile.write(newrow)

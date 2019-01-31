import sys
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from PyQt5.QtCore import *
from PyQt5.QtMultimedia import *
from CSVFILE_ACTION import LoginFile
from MENUBAR import UiMenubar
from CSVFILE_ACTION import SignupFile
from SENDINGEMAIL import SendingEmail
from INPUTVALIDATION import check_invalid_symbols
from INPUTVALIDATION import check_len
from INPUTVALIDATION import check_is_digit
from INPUTVALIDATION import check_len2

class StartWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        self.ui = uic.loadUi('START.ui', self)
        self.getusername.setPlaceholderText('username')
        self.getpassword.setPlaceholderText('password')
        self.login.clicked.connect(self.logincheck)
        self.signup.clicked.connect(self.signupclicked)
        self.forget.clicked.connect(self.forgetclicked)
        self.show()
    def logincheck(self):
        username = self.getusername.text()
        password = self.getpassword.text()
        header = ['username', 'password', 'firstname', 'lastname', 'email', 'phone', 'cardnumber', 'cvv', 'tombnumber',\
                  'nameontomb', 'service']
        check_login = LoginFile('userinfo.csv', header, str(username), str(password))

        if(check_login.checkLogin()):
            self.close()
            self.username, self.password, self.firstname, self.lastname, self.email, self.phone, self.cardnumber, \
            self.cvv, self.tombnumber, self.nameontomb, self.service = check_login.readFile()

            UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)
        else:
            self.popmessage.setText('username doesn\'t exist or password doesn\'t match')

    def signupclicked (self):
        self.close()
        UiSignup()

    def forgetclicked(self):
        UiRecover()

class UiSignup(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiSignup, self).__init__()
        self.ui = uic.loadUi('SIGNUP.ui', self)
        self.getusername.setPlaceholderText('username')
        self.getpassword.setPlaceholderText('password')
        self.getfirstname.setPlaceholderText('firstname')
        self.getlastname.setPlaceholderText('lastname')
        self.getemail.setPlaceholderText('e-mail : xxx@hotmail.com')
        self.getphone.setPlaceholderText('phone : 0888888888')

        self.show()
        self.complete.clicked.connect(self.check)
        self.back.clicked.connect(self.beBack)

    def beBack(self):
        self.close()
        StartWindow()
    def check(self):
        header = ['username', 'password', 'firstname', 'lastname', 'email', 'phone', 'cardnumber', 'cvv', 'tombnumber',
                  'nameontomb', 'service']

        newrow = self.getusername.text() + ',' + self.getpassword.text() + ',' + self.getfirstname.text() + ',' + \
                 self.getlastname.text() + ',' + self.getemail.text() + ',' + self.getphone.text() + ',' + 'none' + ','\
                 + 'none' + ',' + 'none' + ',' + 'none' + ',' + 'nnnnnn' + ',' + '\n'

        self.username = self.getusername.text()
        self.password = self.getpassword.text()
        self.firstname = self.getfirstname.text()
        self.lastname = self.getlastname.text()
        self.email = self.getemail.text()
        self.phone = self.getphone.text()
        self.cardnumber = 'none'
        self.cvv = 'none'
        self.tombnumber = 'none'
        self.nameontomb = 'none'
        self.service = 'nnnnnn'

        check_signup = SignupFile(newrow, 'userinfo.csv', header, self.username)

        if(check_len(self.username,6) and check_invalid_symbols(self.username) and check_is_digit(self.phone) and \
                check_len2(self.phone,10) and check_invalid_symbols(self.password) and check_invalid_symbols(self.firstname) \
                and check_invalid_symbols(self.lastname) and check_invalid_symbols(self.email) and self.password  != '' \
                and self.firstname != '' and self.lastname != '' and self.email!=''):
            if (check_signup.readFile()):
                self.close()
                UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                          self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)
            else:
                self.popmessage.setText('this username is unavailable try another one')
        else:
            self.popmessage.setText('please fill all form and don\'t include invalid symbol ex. , \\')
            if(not check_len(self.username,6)):
                self.popmessage.setText('your username must be at least 6 characters')

class UiRecover(QtWidgets.QMainWindow):
    def __init__(self):
        super(UiRecover, self).__init__()
        self.ui = uic.loadUi('SENDINGEMAIL.ui', self)
        self.getusername.setPlaceholderText('username')
        self.getemail.setPlaceholderText('e-mail')
        self.back.clicked.connect(self.beBack)
        self.confirm.clicked.connect(self.confirmisClicked)
        self.show()
    def beBack(self):
        self.close()
    def confirmisClicked(self):
        username = self.getusername.text()
        email = self.getemail.text()
        temp = LoginFile('userinfo.csv', ['username', 'password', 'firstname', 'lastname', 'email', 'phone', \
                                          'cardnumber', 'cvv', 'tombnumber', 'nameontomb', 'service'], username, '')
        temp, password, temp2, temp3, realemail, temp4, temp5, temp6, temp7, temp8, temp9 = temp.readFile()

        if(password == ''):
            self.popmessage.setText('this username doesn\'t exist')
        else:
            if(realemail == email):
                sendmail = SendingEmail(realemail, 'RECOVER YOUR PASSWORD', 'Your password is '+password)
                sendmail.sending()
                self.popmessage.setText('please check your email for the password')
            else:
                self.popmessage.setText('your e-mail isn\'t match')




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    playlist = QMediaPlaylist()
    url = QUrl.fromLocalFile("./SeeYouAgainGuzheng.mp3")
    playlist.addMedia(QMediaContent(url))
    playlist.setPlaybackMode(QMediaPlaylist.Loop)

    player = QMediaPlayer()
    player.setPlaylist(playlist)
    player.play()
    window = StartWindow()
    window.show()
    sys.exit(app.exec_())





import base64
from PyQt5 import QtGui, QtCore, QtWidgets, uic
from CSVFILE_ACTION import ManageAccountFile
from CSVFILE_ACTION import BuyaTombFile
from CSVFILE_ACTION import ConfirmFile
from CSVFILE_ACTION import TombManagementFile
from CSVFILE_ACTION import LoginFile
from SENDINGEMAIL import SendingEmail
from INPUTVALIDATION import check_invalid_symbols
from INPUTVALIDATION import check_is_digit
from INPUTVALIDATION import check_len2

class UiMenubar(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, service):
        super(UiMenubar, self).__init__()
        self.ui = uic.loadUi('MENUBAR.ui', self)
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
        self.show()

        self.quit.clicked.connect(self.quit_clicked)
        self.account.clicked.connect(self.account_clicked)
        self.buyhome.clicked.connect(self.buyatomb_clicked)
        self.servicebutton.clicked.connect(self.service_clicked)
        self.yourhome.clicked.connect(self.yourhome_clicked)
    def yourhome_clicked(self):
        self.close()
        UiTombManagement(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)
    def quit_clicked(self):
        self.close()

    def account_clicked(self):
        self.close()
        UiManageAccount(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

    def service_clicked(self):
        self.close()
        UiService(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

    def buyatomb_clicked(self):
        self.close()
        UiBuyaTomb(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

class UiManageAccount(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, service):
        super(UiManageAccount, self).__init__()
        self.ui = uic.loadUi('MANAGEACCOUNT.ui', self)
        self.show()
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
        self.header = ['username', 'password', 'firstname', 'lastname', 'email', 'phone', 'cardnumber', 'cvv', \
                       'tombnumber', 'nameontomb', 'service']

        self.updateusername.setText(self.username)
        self.updatepassword.setPlaceholderText(self.password)
        self.updatefirstname.setPlaceholderText(self.firstname)
        self.updatelastname.setPlaceholderText(self.lastname)
        self.updateemail.setPlaceholderText(self.email)
        self.updatephone.setPlaceholderText(self.phone)
        self.updatecardnumber.setPlaceholderText(self.cardnumber)
        self.updatecvv.setPlaceholderText(self.cvv)

        self.update.clicked.connect(self.updateinfo)
        self.back.clicked.connect(self.beBack)

    def updateinfo(self):
        check = True
        if len(self.updatepassword.text()) > 0 and check_invalid_symbols(self.updatepassword.text()):
            self.password = self.updatepassword.text()
        elif len(self.updatepassword.text()) == 0:
            pass
        else:
            check = False

        if len(self.updatefirstname.text()) > 0 and check_invalid_symbols(self.updatefirstname.text()):
            self.firstname = self.updatefirstname.text()
        elif len(self.updatefirstname.text()) == 0:
            pass
        else:
            check = False

        if len(self.updatelastname.text()) and check_invalid_symbols(self.updatelastname.text()) > 0:
            self.lastname = self.updatelastname.text()
        elif len(self.updatelastname.text()) == 0:
            pass
        else:
            check = False

        if len(self.updateemail.text()) > 0 and check_invalid_symbols(self.updateemail.text()):
            self.email = self.updateemail.text()
        elif len(self.updateemail.text()) == 0:
            pass
        else:
            check = False

        if len(self.updatephone.text()) == 10 and check_is_digit(self.updatephone.text()):
            self.phone = self.updatephone.text()
        elif len(self.updatephone.text()) == 0:
            pass
        else:
            check = False

        if len(self.updatecardnumber.text()) == 16 and check_is_digit(self.cardnumber):
            self.cardnumber = self.updatecardnumber.text()
        elif len(self.updatecardnumber.text()) == 0:
            pass
        else:
            check = False

        if len(self.updatecvv.text()) == 3 and check_is_digit(self.cvv):
            self.cvv = self.updatecvv.text()
        elif len(self.updatecvv.text()) == 0:
            pass
        else:
            check = False

        if(check):
            temp = ManageAccountFile('userinfo.csv', self.header, self.username, self.password, self.firstname, \
                                     self.lastname, self.email, self.phone, self.cardnumber, self.cvv, self.tombnumber, \
                                     self.nameontomb, self.service)
            temp.updateFile()
            self.beBack()
        else:
            self.popmessage.setText('your input is invalid')

    def beBack(self):
        self.close()
        UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, self.cardnumber, \
                  self.cvv, self.tombnumber, self.nameontomb, self.service)

class UiBuyaTomb(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, service):
        super(UiBuyaTomb, self).__init__()
        self.ui = uic.loadUi('BUYATOMB.ui', self)

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

        self.show()
        self.popmessage.setText('S E L E C T     Y O U R     T O M B')

        self.header = ['tombnumber', 'available', 'invitationcode']
        self.temp = BuyaTombFile('tombinfo.csv', self.header ,self.username)

        labelText = self.temp.readFile()

        self.A1.setText(labelText[0])
        self.A2.setText(labelText[1])
        self.A3.setText(labelText[2])
        self.A4.setText(labelText[3])
        self.A5.setText(labelText[4])
        self.A6.setText(labelText[5])
        self.A7.setText(labelText[6])
        self.A8.setText(labelText[7])
        self.A9.setText(labelText[8])
        self.A10.setText(labelText[9])
        self.A11.setText(labelText[10])
        self.B1.setText(labelText[11])
        self.B2.setText(labelText[12])
        self.B3.setText(labelText[13])
        self.B4.setText(labelText[14])
        self.B5.setText(labelText[15])
        self.B6.setText(labelText[16])
        self.B7.setText(labelText[17])

        self.A1.mousePressEvent = (lambda event, text=self.A1.text(), number = 'a1': self.mousePressEvent(event, text, number))
        self.A2.mousePressEvent = (lambda event, text=self.A2.text(), number = 'a2': self.mousePressEvent(event, text, number))
        self.A3.mousePressEvent = (lambda event, text=self.A3.text(), number = 'a3': self.mousePressEvent(event, text, number))
        self.A4.mousePressEvent = (lambda event, text=self.A4.text(), number = 'a4': self.mousePressEvent(event, text, number))
        self.A5.mousePressEvent = (lambda event, text=self.A5.text(), number = 'a5': self.mousePressEvent(event, text, number))
        self.A6.mousePressEvent = (lambda event, text=self.A6.text(), number = 'a6': self.mousePressEvent(event, text, number))
        self.A7.mousePressEvent = (lambda event, text=self.A7.text(), number = 'a7': self.mousePressEvent(event, text, number))
        self.A8.mousePressEvent = (lambda event, text=self.A8.text(), number = 'a8': self.mousePressEvent(event, text, number))
        self.A9.mousePressEvent = (lambda event, text=self.A9.text(), number = 'a9': self.mousePressEvent(event, text, number))
        self.A10.mousePressEvent = (lambda event, text=self.A10.text(), number = 'a10': self.mousePressEvent(event, text, number))
        self.A11.mousePressEvent = (lambda event, text=self.A11.text(), number = 'a11': self.mousePressEvent(event, text, number))
        self.B1.mousePressEvent = (lambda event, text=self.B1.text(), number = 'b1': self.mousePressEvent(event, text, number))
        self.B2.mousePressEvent = (lambda event, text=self.B2.text(), number = 'b2': self.mousePressEvent(event, text, number))
        self.B3.mousePressEvent = (lambda event, text=self.B3.text(), number = 'b3': self.mousePressEvent(event, text, number))
        self.B4.mousePressEvent = (lambda event, text=self.B4.text(), number = 'b4': self.mousePressEvent(event, text, number))
        self.B5.mousePressEvent = (lambda event, text=self.B5.text(), number = 'b5': self.mousePressEvent(event, text, number))
        self.B6.mousePressEvent = (lambda event, text=self.B6.text(), number = 'b6': self.mousePressEvent(event, text, number))
        self.B7.mousePressEvent = (lambda event, text=self.B7.text(), number = 'b7': self.mousePressEvent(event, text, number))
        self.bg.mousePressEvent = (lambda event, text='nothing', number = 'none': self.mousePressEvent(event, text, number))

        self.back.clicked.connect(self.beBack)

    def mousePressEvent(self, event, text, number):
        if text == 'nothing':
            pass
        elif (event.button() == QtCore.Qt.LeftButton or event.button() == QtCore.Qt.RightButton) and text != 'S O L D':
            if(self.tombnumber == 'none'):
                self.close()
                self.tombnumber = number
                UiConfirm(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)
            else:
                self.popmessage.setText('You already buy a tomb. If you need another one please signup for another account.')

        elif(event.button() == QtCore.Qt.LeftButton or event.button() == QtCore.Qt.RightButton) and text == 'S O L D':
            self.popmessage.setText('T h i s    t o m b    i s    u n a v a i l a b l e    p l e a s e    c h o o s e    a    n e w    o n e')
        #super(UiBuyaTomb, self).mousePressEvent(event, text, number)

    def beBack(self):
        self.close()
        UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, self.cardnumber, \
                  self.cvv, self.tombnumber, self.nameontomb, self.service)


class UiConfirm(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, service):
        super(UiConfirm, self).__init__()
        self.ui = uic.loadUi('CONFIRMATION.ui', self)
        self.show()
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
        self.showtombnumber.setText(' '+self.tombnumber)

        if(self.tombnumber == 'b7'):
            self.price = '450000'
            self.pic1.hide()
        elif(self.tombnumber[0] == 'a'):
            self.price = '250000'
            self.pic2.hide()
            self.second.hide()
            self.getname2.hide()
        else:
            self.price = '350000'
            self.pic1.hide()

        self.showprice.setText(' '+self.price)
        self.getnewcardnumber.setPlaceholderText(self.cardnumber)
        self.getnewcvv.setPlaceholderText(self.cvv)
        self.back.clicked.connect(self.beBack)
        self.confirm.clicked.connect(self.confirmisClicked)

    def confirmisClicked(self):
        name1 = self.getname1.text()
        name2 = self.getname2.text()
        check = False

        if(self.tombnumber[0] == 'b'):
            if((self.cardnumber == 'none' and self.getnewcardnumber.text() == '') \
                    or (self.getnewcvv.text() == '' and self.cvv == 'none') or name1 == '' or name2 == ''):
                self.popmessage.setText('Please fill all the information above')
            else:
                self.nameontomb = name1 + ' and ' + name2

                if self.getnewcardnumber.text() != '':
                    self.cardnumber = self.getnewcardnumber.text()
                    self.cvv = self.getnewcvv.text()
                check = True
        else:
            if((self.cardnumber == 'none' and self.getnewcardnumber.text() == '') \
                    or (self.getnewcvv.text() == '' and self.cvv == 'none') or name1 == ''):
                self.popmessage.setText('Please fill all the information above')
            else:
                self.nameontomb = name1

                if self.getnewcardnumber.text() != '':
                    self.cardnumber = self.getnewcardnumber.text()
                    self.cvv = self.getnewcvv.text()
                check = True
        if(check):
            temp = ConfirmFile('tombinfo.csv', ['tombnumber', 'available', 'invitationcode'], self.username, self.cardnumber, \
                               self.cvv, self.tombnumber, self.nameontomb)
            temp.updateFile()
            temp.updateFile2()
            self.close()
            UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

    def beBack(self):
        self.close()
        self.tombnumber = 'none'
        UiBuyaTomb(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, self.cardnumber, \
                  self.cvv, self.tombnumber, self.nameontomb, self.service)


class UiService(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, service):
        super(UiService, self).__init__()
        self.ui = uic.loadUi('SERVICE.ui', self)

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

        self.show()
        self.findtotalcost.clicked.connect(self.findTotalCostisClicked)
        self.confirm.clicked.connect(self.confirmisClicked)
        self.back.clicked.connect(self.beBack)
    def findTotalCostisClicked(self):
        self.totalcostText = 0
        self.serviceText = ''

        if self.food.isChecked():
            self.totalcostText += 9000
            self.serviceText += 'y'
        else:
            self.serviceText += 'n'

        if self.flower.isChecked():
            self.totalcostText += 5000
            self.serviceText += 'y'
        else:
            self.serviceText += 'n'

        if self.tent.isChecked():
            self.totalcostText += 5000
            self.serviceText += 'y'
        else:
            self.serviceText += 'n'

        if self.cleaning.isChecked():
            self.totalcostText += 9000
            self.serviceText += 'y'
        else:
            self.serviceText += 'n'

        if self.grass.isChecked():
            self.totalcostText += 5000
            self.serviceText += 'y'
        else:
            self.serviceText += 'n'

        if self.kongtek.isChecked():
            self.totalcostText += 6000
            self.serviceText += 'y'
        else:
            self.serviceText += 'n'
        self.totalcost.setText(str(self.totalcostText))

    def confirmisClicked(self):
        self.findTotalCostisClicked()
        check = True
        self.finalserviceText = ''

        if self.tombnumber != 'none':
            if self.service != 'nnnnnn':
                for i in range (len(self.service)):
                    #print(self.service[i], self.serviceText[i])
                    if (self.service[i] == 'y' and self.serviceText[i] == 'y'):
                        self.popmessage.setText('You add the same service. Please try again.')
                        check = False
                        break
                    else:
                        if (self.service[i] == 'y' or self.serviceText[i] == 'y'):
                            self.finalserviceText+='y'
                        else:
                            self.finalserviceText+='n'
            else:
                self.finalserviceText = self.serviceText
        else:
            self.popmessage.setText('You have to buy a tomb before adding any service')
            check = False



        if(check):
            self.close()
            UiConfirmService(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                             self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service, \
                             self.finalserviceText, self.totalcostText, self.serviceText)


    def beBack(self):
        self.close()
        UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, self.cardnumber, \
                  self.cvv, self.tombnumber, self.nameontomb, self.service)


class UiConfirmService(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, \
                 service, finalservice, price, showserviceText):

        super(UiConfirmService, self).__init__()

        self.ui = uic.loadUi('SERVICECONFIRMATION.ui', self)
        self.show()
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
        self.finalservice = finalservice
        self.price = price
        self.showserviceText = showserviceText

        self.showtombnumber.setText(' '+str(self.tombnumber))
        self.showprice.setText(' '+str(self.price))
        self.getnewcardnumber.setPlaceholderText(' '+str(self.cardnumber))
        self.getnewcvv.setPlaceholderText(' '+str(self.cvv))

        textshowservice = ''

        if self.showserviceText[0] == 'y':
            textshowservice += ' ANCESTOR  WORSHIP  WITH  FOOD\n'
        if self.showserviceText[1] == 'y':
            textshowservice += ' SPREADING   FLOWERS\n'
        if self.showserviceText[2] == 'y':
            textshowservice += ' PROVIDING   TENTS\n'
        if self.showserviceText[3] == 'y':
            textshowservice += ' TOMB   CLEANING\n'
        if self.showserviceText[4] == 'y':
            textshowservice += ' CUTTING   GRASS\n'
        if self.showserviceText[5] == 'y':
            textshowservice += ' KONG   TEK   RITE'

        self.showservice.setText(str(textshowservice))
        self.confirm.clicked.connect(self.confirmisClicked)
        self.back.clicked.connect(self.beBack)

    def confirmisClicked(self):
        if (self.getnewcardnumber.text() != '' and self.getnewcvv.text() != ''):
            self.cvv = self.getnewcvv.text()
            self.cardnumber = self.getnewcardnumber.text()

        if (self.cardnumber == 'none' or self.cvv == 'none'):
            self.popmessage.setText('Please fill all the information above')
        else:
            self.service = self.finalservice
            header = ['username', 'password', 'firstname', 'lastname', 'email', 'phone', 'cardnumber', 'cvv', \
                      'tombnumber', 'nameontomb', 'service']
            temp = ManageAccountFile('userinfo.csv', header,self.username, self.password, self.firstname, self.lastname, self.email, \
                                     self.phone, self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)
            temp.updateFile()

            self.close()
            UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                      self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

    def beBack(self):
        self.close()
        UiService(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                  self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)


class UiTombManagement(QtWidgets.QMainWindow):
    def __init__(self, username, password, firstname, lastname, email, phone, cardnumber, cvv, tombnumber, nameontomb, service):
        super(UiTombManagement, self).__init__()
        self.ui = uic.loadUi('TOMBMANAGEMENT.ui', self)

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

        if self.tombnumber != 'none':
            self.getinvitationcode.hide()
            temp = ConfirmFile('tombinfo.csv', ['tombnumber', 'available', 'invitationcode'], self.username, \
                               self.cardnumber, self.cvv, self.tombnumber, self.nameontomb)
            self.invitationcode = temp.readFile()
            self.showinvitationcode.setText('  '+str(self.invitationcode))

            temp2 = TombManagementFile('date.csv', ['tombnumber', 'username', 'date'], self.tombnumber)
            selecteddate, howmanypeople = temp2.readFile()
            selecteddate = ' '.join(selecteddate)
            if( howmanypeople>0 ):
                self.showdate.setText(' ' + selecteddate + '   ' + str(howmanypeople) + ' people')
            else:
                self.showdate.setText(' no one choose the date')
        else:
            self.showinvitationcode.hide()
            self.sendcode.hide()
            self.getinvitationcode.setPlaceholderText(' type your code here')
        self.getdate.setPlaceholderText(' DD/MM/YYYY')
        self.showtombnumber.setText(' '+self.tombnumber)
        self.shownameontomb.setText(' '+self.nameontomb.upper())

        textshowservice = ''
        if self.service[0] == 'y':
            textshowservice += 'ANCESTOR  WORSHIP  WITH  FOOD\n'
        if self.service[1] == 'y':
            textshowservice += 'SPREADING   FLOWERS\n'
        if self.service[2] == 'y':
            textshowservice += 'PROVIDING   TENTS\n'
        if self.service[3] == 'y':
            textshowservice += 'TOMB   CLEANING\n'
        if self.service[4] == 'y':
            textshowservice += 'CUTTING   GRASS\n'
        if self.service[5] == 'y':
            textshowservice += 'KONG   TEK   RITE'
        if textshowservice == '':
            textshowservice = ' NONE'
        self.showservice.setText(textshowservice)
        self.header = ['username', 'password', 'firstname', 'lastname', 'email', 'phone', 'cardnumber', 'cvv', 'tombnumber', 'nameontomb', 'service']
        self.back.clicked.connect(self.beBack)
        self.sendcode.clicked.connect(self.sendcodeisClicked)
        self.confirm.clicked.connect(self.confirmisClicked)
        self.show()
    def sendcodeisClicked(self):
        UiSendEmail(self.firstname, self.lastname, self.invitationcode)
    def beBack(self):
        self.close()
        UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                  self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

    def confirmisClicked(self):
        if self.tombnumber == 'none' and self.getdate.text() != '':
            self.popmessage2.setText('you not allow to choose date')
        elif self.tombnumber == 'none' and self.getinvitationcode.text() != '':
            try:
                temp = self.getinvitationcode.text()
                usercheck = temp[1::]
                usercheck = base64.b64decode(usercheck)
                usercheck = str(usercheck)
                usercheck = usercheck[2:-1]

                temp2 = LoginFile('userinfo.csv', self.header, usercheck, '')

                temp3, temp4, temp5, temp6, temp7, temp8, temp9, temp10, self.tombnumber, self.nameontomb, self.service = temp2.readFile()
                if self.tombnumber != 'none':
                    update = ManageAccountFile('userinfo.csv',self.header, self.username, self.password, self.firstname, self.lastname, self.email, \
                                               self.phone, self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)
                    update.updateFile()
                    self.close()
                    UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                              self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

                else:
                    self.popmessage.setText('not found this invitation code')
            except:
                self.popmessage.setText('not found this invitation code')

        elif self.tombnumber != 'none' and self.getdate.text() != '':
            self.user_selected_date = self.getdate.text()
            self.user_selected_date = self.user_selected_date.split('/')

            if(len(self.user_selected_date)!=3):
                self.popmessage2.setText('you input a valid date')
            elif(not(self.user_selected_date[0].isdigit() and  self.user_selected_date[1].isdigit()and  self.user_selected_date[2].isdigit())):
                self.popmessage2.setText('you input a valid date')
            elif(len(self.user_selected_date)==3 and (int(self.user_selected_date[0])>31 or int(self.user_selected_date[0])<1 or \
                    int(self.user_selected_date[1])>12 or int(self.user_selected_date[1])<1 or int(self.user_selected_date[2])<2019)):
                self.popmessage2.setText('you input a valid date')
            else:
                    temp = TombManagementFile('date.csv', ['tombnumber', 'username', 'date'], self.tombnumber)
                    temp.updateFile(self.username, str(self.getdate.text()))
                    self.close()
                    UiMenubar(self.username, self.password, self.firstname, self.lastname, self.email, self.phone, \
                              self.cardnumber, self.cvv, self.tombnumber, self.nameontomb, self.service)

class UiSendEmail(QtWidgets.QMainWindow):
    def __init__(self, firstname, lastname, invitationcode):
        super(UiSendEmail, self).__init__()
        self.ui = uic.loadUi('SENDINGEMAIL2.ui', self)
        self.firstname = firstname
        self.lastname = lastname
        self.invitationcode = invitationcode
        self.getemail.setPlaceholderText('e-mail')
        self.back.clicked.connect(self.beBack)
        self.confirm.clicked.connect(self.confirmisClicked)
        self.show()
    def beBack(self):
        self.close()
    def confirmisClicked(self):
        message = self.firstname+'  ' + self.lastname + ' invited you to join the home on Finding New Home\nYour invitation code is '+self.invitationcode
        sendmail = SendingEmail(self.getemail.text(), 'YOU HAVE INIVITED!!!!', message)
        sendmail.sending()
        self.popmessage.setText('already sent')

'''if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Ui_Menubar()
    window.show()
    sys.exit(app.exec_())'''

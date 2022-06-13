from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

try: 
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE user_account (
                        user_id integer PRIMARY KEY AUTOINCREMENT,
                        username text,
                        password text,
                UNIQUE (username, password) ON CONFLICT IGNORE)""")  

except:

    pass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1100, 700)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("#left_body{\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"#right_body{\n"
"    \n"
"    background-color: rgb(244, 244, 244);\n"
"    \n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.left_body = QtWidgets.QFrame(self.frame)
        self.left_body.setMaximumSize(QtCore.QSize(550, 16777215))
        self.left_body.setStyleSheet("#header_logo{\n"
"border:none;\n"
"}\n"
"#label{\n"
"color: rgb(76, 76, 76);\n"
"}\n"
"#username_field, #password_field{\n"
"border: none;\n"
"background-color: rgb(245, 245, 245);\n"
"border-radius: 10%;\n"
"padding: 10px;\n"
"\n"
"}\n"
"#label_2, #label_3, #label_4{\n"
"color: rgb(76, 76, 76);\n"
"}\n"
"#login_btn{\n"
"border: none;\n"
"background-color: rgb(52, 190, 130);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10%;\n"
"padding: 8px;\n"
"}\n"
"#login_btn:hover{\n"
"background-color: rgb(47, 171, 115);\n"
"}\n"
"#error_txt{\n"
"background-color: rgb(248, 215, 218);\n"
"color: rgb(114, 28, 36);\n"
"padding: 15px;\n"
"border-radius: 10%;\n"
"}\n"
"")
        self.left_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_body.setObjectName("left_body")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.left_body)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header_body = QtWidgets.QFrame(self.left_body)
        self.header_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_body.setObjectName("header_body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.header_body)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.header_logo = QtWidgets.QPushButton(self.header_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.header_logo.setFont(font)
        self.header_logo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.header_logo.setStyleSheet("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.header_logo.setIcon(icon)
        self.header_logo.setIconSize(QtCore.QSize(35, 35))
        self.header_logo.setObjectName("header_logo")
        self.horizontalLayout_3.addWidget(self.header_logo)
        self.verticalLayout_3.addWidget(self.header_body, 0, QtCore.Qt.AlignLeft)
        self.body_body = QtWidgets.QFrame(self.left_body)
        self.body_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_body.setObjectName("body_body")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.body_body)
        self.verticalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.error_body = QtWidgets.QFrame(self.body_body)
        self.error_body.setMaximumSize(QtCore.QSize(16777215, 100))
        self.error_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.error_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.error_body.setObjectName("error_body")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.error_body)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.error_txt = QtWidgets.QLabel(self.error_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.error_txt.setFont(font)
        self.error_txt.setAlignment(QtCore.Qt.AlignCenter)
        self.error_txt.setObjectName("error_txt")
        self.horizontalLayout_4.addWidget(self.error_txt)
        self.verticalLayout_7.addWidget(self.error_body)
        self.label_4 = QtWidgets.QLabel(self.body_body)
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4)
        self.form_body = QtWidgets.QFrame(self.body_body)
        self.form_body.setMaximumSize(QtCore.QSize(16777215, 235))
        self.form_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_body.setObjectName("form_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.form_body)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 20)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.form_body)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setContentsMargins(0, 20, 0, 0)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.username_field = QtWidgets.QLineEdit(self.frame_2)
        self.username_field.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(15)
        self.username_field.setFont(font)
        self.username_field.setObjectName("username_field")
        self.verticalLayout_4.addWidget(self.username_field)
        self.verticalLayout_6.addWidget(self.frame_2, 0, QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.form_body)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setContentsMargins(0, -1, 0, -1)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3, 0, QtCore.Qt.AlignBottom)
        self.password_field = QtWidgets.QLineEdit(self.frame_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(15)
        self.password_field.setFont(font)
        self.password_field.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_field.setObjectName("password_field")
        self.verticalLayout_5.addWidget(self.password_field)
        self.verticalLayout_6.addWidget(self.frame_3, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_7.addWidget(self.form_body, 0, QtCore.Qt.AlignTop)
        self.login_btn = QtWidgets.QPushButton(self.body_body)
        self.login_btn.setEnabled(True)
        self.login_btn.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.login_btn.setFont(font)
        self.login_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout_7.addWidget(self.login_btn)
        self.verticalLayout_3.addWidget(self.body_body, 0, QtCore.Qt.AlignVCenter)
        self.footer_body = QtWidgets.QFrame(self.left_body)
        self.footer_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_body.setObjectName("footer_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.footer_body)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.footer_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addWidget(self.footer_body)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 10)
        self.verticalLayout_3.setStretch(2, 1)
        self.horizontalLayout.addWidget(self.left_body)
        self.right_body = QtWidgets.QFrame(self.frame)
        self.right_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_body.setObjectName("right_body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.right_body)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.main_logo = QtWidgets.QLabel(self.right_body)
        self.main_logo.setMaximumSize(QtCore.QSize(200, 200))
        self.main_logo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"padding: 30px;\n"
"border-radius: 100%;")
        self.main_logo.setText("")
        self.main_logo.setPixmap(QtGui.QPixmap("img/logo.png"))
        self.main_logo.setScaledContents(True)
        self.main_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.main_logo.setWordWrap(False)
        self.main_logo.setObjectName("main_logo")
        self.verticalLayout_2.addWidget(self.main_logo, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.right_body)
        self.verticalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sales & Inventory Management System"))
        self.header_logo.setText(_translate("MainWindow", "  Sales & Inventory Management System"))
        self.error_txt.setText(_translate("MainWindow", "Error here..."))
        self.label_4.setText(_translate("MainWindow", "Login."))
        self.label_2.setText(_translate("MainWindow", "Username"))
        self.username_field.setPlaceholderText(_translate("MainWindow", "Enter your username"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.password_field.setPlaceholderText(_translate("MainWindow", "Enter your password"))
        self.login_btn.setText(_translate("MainWindow", "LOGIN "))
        self.label.setText(_translate("MainWindow", "© Sales & Inventory Management System "))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


        def __init__(self, parent=None):

                super(MainWindow, self).__init__(parent=parent)
                self.setupUi(self)
                self.ss()
                
                self.login_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        
                #buttons
                self.login_btn.clicked.connect(self.login_btn_funct)

                #text field changed
                self.username_field.textChanged.connect(self.username_field_changed)
                self.password_field.textChanged.connect(self.password_field_changed)
        def ss(self):

                self.error_body.hide()
                self.password_field.setEnabled(False)
                self.login_btn.setEnabled(False)

        def get_user(self):

                with conn:
                        c.execute(" SELECT * FROM user_account ")
                        return c.fetchall() 
                        
        def login_btn_funct(self):

                
                get_user = self.username_field.text()
                get_passwd = self.password_field.text()

                if not get_user and not get_passwd:

                        self.error_body.show()
                        self.label_4.hide()  
                        
                else:
                
                        get = self.get_user()
                        
                        user_id = []
                        username = []
                        password = []

                        for i in range(len(get)):

                                a = get[i]
                                user_id.append(a[0])
                                username.append(a[1])
                                password.append(a[2])
                        
                        try:

                                c.execute(" SELECT * FROM user_account WHERE username=:username", {'username': get_user })        

                                r = [s for s in username if s.startswith(get_user)]
                                result = r[0] if r else 'nomatch'
                                ind = username.index(get_user)
                                

                                if result == 'nomatch':

                                       
                                        self.error_txt.setText('Username or password is incorrect.')
                                        self.error_body.show()
                                        self.label_4.hide()  

                                else:

                                        if get_user == result and get_passwd == password[ind]:
                                                
                                        
                                                self.error_txt.setText('Successfully Login!')
                                                self.error_body.show()
                                                self.label_4.hide()  

                                
                                                        
                                        else:
                                                self.error_txt.setText('Username or password is incorrect.')
                                                self.error_body.show()
                                                self.label_4.hide()  
                                
                                                

                        except Exception as e:
                        

                                self.error_txt.setText('Username or password is incorrect.')
                                self.error_body.show()
                                self.label_4.hide()  

        def username_field_changed(self):

                self.error_body.hide()
                self.label_4.show() 

                get_user = self.username_field.text()

                if not get_user:

                        self.password_field.setEnabled(False)
                else:
                        self.password_field.setEnabled(True)

        def password_field_changed(self):

                self.error_body.hide()
                self.label_4.show()

                get_pass = self.password_field.text()

                if not get_pass:

                        self.login_btn.setEnabled(False)
                else:
                        self.login_btn.setEnabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())

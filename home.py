from PyQt5 import QtCore, QtGui, QtWidgets
from qtpy.QtCore import Qt
from PyQt5.QtCore import QTimer, QDateTime
import sqlite3

try: 
        conn = sqlite3.connect('db.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE user_account (
                        user_id integer PRIMARY KEY AUTOINCREMENT,
                        username text,
                        password text,
                UNIQUE (username, password) ON CONFLICT IGNORE)""")  

        c.execute("""CREATE TABLE new_sales (

                        cname text,
                        product text,
                        quantity integer,
                        price integer,
                        amount integer,
                        
                UNIQUE (cname, product) ON CONFLICT IGNORE)""")  
except:

    pass


cart = "img/chevron-down.svg"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1400, 900)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("#main_body{background-color: rgb(248, 248, 248);}\n"
"#date_time{color: rgb(112, 112, 112);}\n"
"\n"
"#profile_logo{\n"
"\n"
"border-radius: 25%;\n"
"}\n"
"#profile_logo:hover{\n"
"background-color: rgb(236, 236, 236);\n"
"}\n"
"#logout_btn{\n"
"padding: 4px;\n"
"border-radius: 22%;\n"
"}\n"
"#logout_btn:hover{\n"
"background-color: rgb(236, 236, 236);\n"
"\n"
"}\n"
"#menu, #menu2{\n"
"color: rgb(76, 76, 76);\n"
"border: none;\n"
"background-color:transparent;\n"
"padding: 5px;\n"
"}\n"
"#person_name{\n"
"color: rgb(76, 76, 76)\n"
"}\n"
"#person_role{\n"
"color: rgb(112, 112, 112)\n"
"}\n"
"#user_message2{\n"
"color: rgb(112, 112, 112);\n"
"}\n"
"#totals_sales_body{\n"
"background-color: rgb(47, 134, 166);\n"
"border-radius: 30%;\n"
"}\n"
"#totals_products_body,#totals_products_body_2, #totals_products_body_3, #totals_products_body_4{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 30%;\n"
"}\n"
"#label, #label_2{\n"
"color: white\n"
"}\n"
"\n"
"/*SIDEBAR MENU */\n"
"\n"
"QListWidget#menu, QListWidget#menu2{\n"
"background-color: transparent;\n"
"border: none;\n"
"margin-top: 10px;\n"
"\n"
"}\n"
"QListWidget#menu::item, QListWidget#menu2::item{\n"
"padding-right:10px;\n"
"border-radius: 15px;\n"
"padding: 5px;\n"
"\n"
"}\n"
"QListWidget#menu::item:hover, QListWidget#menu2::item:hover{\n"
"background-color: rgb(198, 198, 198);\n"
"font-weight: bold;\n"
"}\n"
"QListWidget#menu::item:selected, QListWidget#menu2::item:selected { \n"
"background-color: rgb(198, 198, 198);\n"
"font-weight: bold;\n"
"}\n"
"\n"
"/*SALES ORDER*/\n"
"\n"
"#sales_order_body{\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 30%;\n"
"}\n"
"#new_sales_order_btn{\n"
"background-color: rgb(47, 134, 166);\n"
"border-radius: 5%;\n"
"color: white;\n"
"padding: 5px;\n"
"}\n"
"#new_sales_order_btn:hover{\n"
"background-color: rgb(35, 102, 126);\n"
"}\n"
"\n"
"\n"
"#label_11{\n"
"color: rgb(76, 76, 76);\n"
"}\n"
"#label_12{\n"
"color: rgb(112, 112, 112);\n"
"}\n"
"#close_sales_order_btn{\n"
"background-color: transparent;\n"
"padding: 5px;\n"
"border-radius: 15%;\n"
"}\n"
"#close_sales_order_btn:hover{\n"
"background-color: rgb(214, 214, 214);\n"
"}\n"
"\n"
"/*NEW SALES ORDER*/\n"
"\n"
"\n"
"#pay_sales_order_btn, #add_to_list_sales_order_btn{\n"
"background-color: rgb(47, 134, 166);\n"
"border-radius: 5%;\n"
"color: white;\n"
"padding: 15px;\n"
"}\n"
"#pay_sales_order_btn:hover, #add_to_list_sales_order_btn:hover{\n"
"background-color: rgb(35, 102, 126);\n"
"}\n"
"\n"
"#delete_sales_order_btn{\n"
"background-color: rgb(216, 58, 86);\n"
"border-radius: 5%;\n"
"color: white;\n"
"padding: 15px;\n"
"}\n"
"#delete_sales_order_btn:hover{\n"
"background-color: rgb(191, 51, 76);\n"
"}\n"
"\n"
"#update_sales_order_btn{\n"
"background-color: rgb(52, 190, 130);\n"
"border-radius: 5%;\n"
"color: white;\n"
"padding: 15px;\n"
"}\n"
"#update_sales_order_btn:hover{\n"
"background-color: rgb(47, 171, 115);\n"
"}\n"
"\n"
"#new_sales_customers_name, #new_sales_product{\n"
"font-size: 20px;\n"
"}\n"
"\n"
"#label_14, #label_15, #label_16{\n"
"color: rgb(216, 58, 86);\n"
"}\n"
"QComboBox::editable\n"
"{\n"
"background-color : rgb(249, 249, 249);\n"
"border: none\n"
"}\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    color: black;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);\n"
"}\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.header_body = QtWidgets.QFrame(self.main_body)
        self.header_body.setStyleSheet("#header_logo{\n"
"border:none;\n"
"}\n"
"#label{\n"
"color: rgb(76, 76, 76);\n"
"}")
        self.header_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header_body.setObjectName("header_body")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header_body)
        self.horizontalLayout_2.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
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
        self.horizontalLayout_2.addWidget(self.header_logo, 0, QtCore.Qt.AlignLeft)
        self.profile_logo_body = QtWidgets.QFrame(self.header_body)
        self.profile_logo_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_logo_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_logo_body.setObjectName("profile_logo_body")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.profile_logo_body)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.profile_header_body = QtWidgets.QFrame(self.profile_logo_body)
        self.profile_header_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profile_header_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profile_header_body.setObjectName("profile_header_body")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.profile_header_body)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.profile_logo = QtWidgets.QPushButton(self.profile_header_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.profile_logo.setFont(font)
        self.profile_logo.setFocusPolicy(QtCore.Qt.NoFocus)
        self.profile_logo.setStyleSheet("")
        self.profile_logo.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/logo1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.profile_logo.setIcon(icon1)
        self.profile_logo.setIconSize(QtCore.QSize(50, 50))
        self.profile_logo.setObjectName("profile_logo")
        self.horizontalLayout.addWidget(self.profile_logo, 0, QtCore.Qt.AlignRight)
        self.person_details_body = QtWidgets.QFrame(self.profile_header_body)
        self.person_details_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.person_details_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.person_details_body.setObjectName("person_details_body")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.person_details_body)
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.person_name = QtWidgets.QLabel(self.person_details_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.person_name.setFont(font)
        self.person_name.setWordWrap(True)
        self.person_name.setObjectName("person_name")
        self.verticalLayout_4.addWidget(self.person_name)
        self.person_role = QtWidgets.QLabel(self.person_details_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setBold(False)
        font.setWeight(50)
        self.person_role.setFont(font)
        self.person_role.setWordWrap(True)
        self.person_role.setObjectName("person_role")
        self.verticalLayout_4.addWidget(self.person_role, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout.addWidget(self.person_details_body)
        self.horizontalLayout.setStretch(0, 8)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout_4.addWidget(self.profile_header_body)
        self.horizontalLayout_2.addWidget(self.profile_logo_body)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 4)
        self.verticalLayout_2.addWidget(self.header_body)
        self.body_body = QtWidgets.QFrame(self.main_body)
        self.body_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.body_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.body_body.setObjectName("body_body")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.body_body)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 20)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.menu_body = QtWidgets.QFrame(self.body_body)
        self.menu_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.menu_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.menu_body.setObjectName("menu_body")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.menu_body)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.menu = QtWidgets.QListWidget(self.menu_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menu.setFont(font)
        self.menu.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menu.setStyleSheet("")
        self.menu.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menu.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menu.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.menu.setIconSize(QtCore.QSize(30, 30))
        self.menu.setWordWrap(True)
        self.menu.setObjectName("menu")
        item = QtWidgets.QListWidgetItem()
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon2.addPixmap(QtGui.QPixmap("img/home.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon2)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/shopping-cart.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon3.addPixmap(QtGui.QPixmap("img/shopping-cart.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon3)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("img/package.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon4.addPixmap(QtGui.QPixmap("img/package.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon4)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("img/tag.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap("img/tag.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon5)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("img/truck.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon6.addPixmap(QtGui.QPixmap("img/truck.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon6)
        self.menu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("img/file-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon7.addPixmap(QtGui.QPixmap("img/file-text.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon7)
        self.menu.addItem(item)
        self.verticalLayout_3.addWidget(self.menu)
        self.menu2 = QtWidgets.QListWidget(self.menu_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.menu2.setFont(font)
        self.menu2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.menu2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menu2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.menu2.setIconSize(QtCore.QSize(30, 30))
        self.menu2.setFlow(QtWidgets.QListView.TopToBottom)
        self.menu2.setObjectName("menu2")
        item = QtWidgets.QListWidgetItem()
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("img/user.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon8.addPixmap(QtGui.QPixmap("img/user.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon8)
        self.menu2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("img/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon9.addPixmap(QtGui.QPixmap("img/settings.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon9)
        self.menu2.addItem(item)
        item = QtWidgets.QListWidgetItem()
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("img/log-out.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon10.addPixmap(QtGui.QPixmap("img/log-out.svg"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        item.setIcon(icon10)
        self.menu2.addItem(item)
        self.verticalLayout_3.addWidget(self.menu2)
        self.verticalLayout_3.setStretch(0, 7)
        self.verticalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.addWidget(self.menu_body)
        self.content_body = QtWidgets.QFrame(self.body_body)
        self.content_body.setStyleSheet("")
        self.content_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.content_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.content_body.setObjectName("content_body")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.content_body)
        self.verticalLayout_5.setContentsMargins(-1, -1, -1, 20)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.products_body = QtWidgets.QFrame(self.content_body)
        self.products_body.setMaximumSize(QtCore.QSize(0, 0))
        self.products_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.products_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.products_body.setObjectName("products_body")
        self.verticalLayout_5.addWidget(self.products_body)
        self.home_body = QtWidgets.QFrame(self.content_body)
        self.home_body.setMaximumSize(QtCore.QSize(0, 0))
        self.home_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_body.setObjectName("home_body")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.home_body)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.home_header_body = QtWidgets.QFrame(self.home_body)
        self.home_header_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_header_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_header_body.setObjectName("home_header_body")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.home_header_body)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(8)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.user_message = QtWidgets.QLabel(self.home_header_body)
        self.user_message.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.user_message.setWordWrap(True)
        self.user_message.setObjectName("user_message")
        self.verticalLayout_6.addWidget(self.user_message)
        self.user_message2 = QtWidgets.QLabel(self.home_header_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        self.user_message2.setFont(font)
        self.user_message2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.user_message2.setWordWrap(True)
        self.user_message2.setObjectName("user_message2")
        self.verticalLayout_6.addWidget(self.user_message2)
        self.home_content_body = QtWidgets.QFrame(self.home_header_body)
        self.home_content_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.home_content_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.home_content_body.setObjectName("home_content_body")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.home_content_body)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_2 = QtWidgets.QFrame(self.home_content_body)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_7.setContentsMargins(20, 20, 50, 20)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.totals_sales_body = QtWidgets.QFrame(self.frame_2)
        self.totals_sales_body.setStyleSheet("")
        self.totals_sales_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.totals_sales_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totals_sales_body.setObjectName("totals_sales_body")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.totals_sales_body)
        self.verticalLayout_8.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label = QtWidgets.QLabel(self.totals_sales_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_8.addWidget(self.label)
        self.frame_5 = QtWidgets.QFrame(self.totals_sales_body)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(40)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.verticalLayout_8.addWidget(self.frame_5)
        self.verticalLayout_8.setStretch(0, 1)
        self.verticalLayout_8.setStretch(1, 5)
        self.horizontalLayout_7.addWidget(self.totals_sales_body)
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout.setContentsMargins(15, 15, 15, 15)
        self.gridLayout.setSpacing(20)
        self.gridLayout.setObjectName("gridLayout")
        self.totals_products_body = QtWidgets.QFrame(self.frame_4)
        self.totals_products_body.setStyleSheet("#frame{background-color: rgb(47, 134, 166);\n"
"border-radius: 30%;}\n"
"#label, #label_2{color: white}\n"
"\n"
"")
        self.totals_products_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.totals_products_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totals_products_body.setObjectName("totals_products_body")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.totals_products_body)
        self.verticalLayout_9.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_3 = QtWidgets.QLabel(self.totals_products_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.frame_6 = QtWidgets.QFrame(self.totals_products_body)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        self.verticalLayout_9.addWidget(self.frame_6)
        self.verticalLayout_9.setStretch(0, 1)
        self.verticalLayout_9.setStretch(1, 2)
        self.gridLayout.addWidget(self.totals_products_body, 0, 0, 1, 1)
        self.totals_products_body_2 = QtWidgets.QFrame(self.frame_4)
        self.totals_products_body_2.setStyleSheet("#frame{background-color: rgb(47, 134, 166);\n"
"border-radius: 30%;}\n"
"#label, #label_2{color: white}\n"
"\n"
"")
        self.totals_products_body_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.totals_products_body_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totals_products_body_2.setObjectName("totals_products_body_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.totals_products_body_2)
        self.verticalLayout_11.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_5 = QtWidgets.QLabel(self.totals_products_body_2)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_11.addWidget(self.label_5)
        self.frame_7 = QtWidgets.QFrame(self.totals_products_body_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.verticalLayout_11.addWidget(self.frame_7)
        self.verticalLayout_11.setStretch(0, 1)
        self.verticalLayout_11.setStretch(1, 2)
        self.gridLayout.addWidget(self.totals_products_body_2, 0, 1, 1, 1)
        self.totals_products_body_3 = QtWidgets.QFrame(self.frame_4)
        self.totals_products_body_3.setStyleSheet("#frame{background-color: rgb(47, 134, 166);\n"
"border-radius: 30%;}\n"
"#label, #label_2{color: white}\n"
"\n"
"")
        self.totals_products_body_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.totals_products_body_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totals_products_body_3.setObjectName("totals_products_body_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.totals_products_body_3)
        self.verticalLayout_12.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_7 = QtWidgets.QLabel(self.totals_products_body_3)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_12.addWidget(self.label_7)
        self.frame_8 = QtWidgets.QFrame(self.totals_products_body_3)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setWordWrap(True)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.verticalLayout_12.addWidget(self.frame_8)
        self.verticalLayout_12.setStretch(0, 1)
        self.verticalLayout_12.setStretch(1, 2)
        self.gridLayout.addWidget(self.totals_products_body_3, 1, 0, 1, 1)
        self.totals_products_body_4 = QtWidgets.QFrame(self.frame_4)
        self.totals_products_body_4.setStyleSheet("#frame{background-color: rgb(47, 134, 166);\n"
"border-radius: 30%;}\n"
"#label, #label_2{color: white}\n"
"\n"
"")
        self.totals_products_body_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.totals_products_body_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.totals_products_body_4.setObjectName("totals_products_body_4")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.totals_products_body_4)
        self.verticalLayout_13.setContentsMargins(11, -1, -1, -1)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.totals_products_body_4)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_13.addWidget(self.label_9)
        self.frame_9 = QtWidgets.QFrame(self.totals_products_body_4)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_10 = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(22)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_10.addWidget(self.label_10)
        self.verticalLayout_13.addWidget(self.frame_9)
        self.verticalLayout_13.setStretch(0, 1)
        self.verticalLayout_13.setStretch(1, 2)
        self.gridLayout.addWidget(self.totals_products_body_4, 1, 1, 1, 1)
        self.horizontalLayout_7.addWidget(self.frame_4)
        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 2)
        self.verticalLayout_10.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.home_content_body)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_10.addWidget(self.frame_3)
        self.verticalLayout_10.setStretch(0, 3)
        self.verticalLayout_10.setStretch(1, 2)
        self.verticalLayout_6.addWidget(self.home_content_body)
        self.verticalLayout_6.setStretch(0, 1)
        self.verticalLayout_6.setStretch(2, 10)
        self.verticalLayout_7.addWidget(self.home_header_body)
        self.verticalLayout_7.setStretch(0, 2)
        self.verticalLayout_5.addWidget(self.home_body)
        self.sales_order_body = QtWidgets.QFrame(self.content_body)
        self.sales_order_body.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.sales_order_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sales_order_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sales_order_body.setObjectName("sales_order_body")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.sales_order_body)
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.sales_order_header_body = QtWidgets.QFrame(self.sales_order_body)
        self.sales_order_header_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sales_order_header_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sales_order_header_body.setObjectName("sales_order_header_body")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.sales_order_header_body)
        self.horizontalLayout_12.setContentsMargins(20, 15, 5, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.sales_order_header_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.frame = QtWidgets.QFrame(self.sales_order_header_body)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_11.setContentsMargins(0, 0, 15, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.new_sales_order_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.new_sales_order_btn.setFont(font)
        self.new_sales_order_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.new_sales_order_btn.setStyleSheet("padding: 7px;")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("img/plus 1.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.new_sales_order_btn.setIcon(icon11)
        self.new_sales_order_btn.setIconSize(QtCore.QSize(30, 30))
        self.new_sales_order_btn.setObjectName("new_sales_order_btn")
        self.horizontalLayout_11.addWidget(self.new_sales_order_btn, 0, QtCore.Qt.AlignRight)
        self.close_sales_order_btn = QtWidgets.QPushButton(self.frame)
        self.close_sales_order_btn.setMaximumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.close_sales_order_btn.setFont(font)
        self.close_sales_order_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.close_sales_order_btn.setStyleSheet("")
        self.close_sales_order_btn.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap("img/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close_sales_order_btn.setIcon(icon12)
        self.close_sales_order_btn.setIconSize(QtCore.QSize(30, 30))
        self.close_sales_order_btn.setObjectName("close_sales_order_btn")
        self.horizontalLayout_11.addWidget(self.close_sales_order_btn, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_12.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_12.setStretch(0, 5)
        self.horizontalLayout_12.setStretch(1, 2)
        self.verticalLayout_14.addWidget(self.sales_order_header_body)
        self.sales_order_body_body = QtWidgets.QFrame(self.sales_order_body)
        self.sales_order_body_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sales_order_body_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sales_order_body_body.setObjectName("sales_order_body_body")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.sales_order_body_body)
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.all_sales_order_body = QtWidgets.QFrame(self.sales_order_body_body)
        self.all_sales_order_body.setMaximumSize(QtCore.QSize(0, 0))
        self.all_sales_order_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.all_sales_order_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.all_sales_order_body.setObjectName("all_sales_order_body")
        self.verticalLayout_17 = QtWidgets.QVBoxLayout(self.all_sales_order_body)
        self.verticalLayout_17.setObjectName("verticalLayout_17")
        self.sales_order_table = QtWidgets.QTableWidget(self.all_sales_order_body)
        self.sales_order_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.sales_order_table.setStyleSheet("QTableWidget#sales_order_table{\n"
"color:rgb(84, 84, 84);\n"
"font: 12pt \"Open Sans\";\n"
"border: none;\n"
"\n"
"}\n"
"QTableWidget#sales_order_table::item{\n"
"padding-right:10px;\n"
"}\n"
"QTableWidget#sales_order_table::item:selected { \n"
"\n"
"background-color: #4C4C4C;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.sales_order_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.sales_order_table.setAlternatingRowColors(False)
        self.sales_order_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.sales_order_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.sales_order_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.sales_order_table.setShowGrid(True)
        self.sales_order_table.setGridStyle(QtCore.Qt.SolidLine)
        self.sales_order_table.setCornerButtonEnabled(True)
        self.sales_order_table.setObjectName("sales_order_table")
        self.sales_order_table.setColumnCount(4)
        self.sales_order_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.sales_order_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.sales_order_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.sales_order_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.sales_order_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.sales_order_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sales_order_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sales_order_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sales_order_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.sales_order_table.setItem(0, 3, item)
        self.sales_order_table.horizontalHeader().setVisible(True)
        self.sales_order_table.horizontalHeader().setDefaultSectionSize(200)
        self.sales_order_table.horizontalHeader().setMinimumSectionSize(100)
        self.sales_order_table.horizontalHeader().setSortIndicatorShown(True)
        self.sales_order_table.horizontalHeader().setStretchLastSection(True)
        self.sales_order_table.verticalHeader().setVisible(True)
        self.sales_order_table.verticalHeader().setCascadingSectionResizes(False)
        self.sales_order_table.verticalHeader().setHighlightSections(False)
        self.sales_order_table.verticalHeader().setSortIndicatorShown(True)
        self.sales_order_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_17.addWidget(self.sales_order_table)
        self.verticalLayout_16.addWidget(self.all_sales_order_body)
        self.new_sales_order_body = QtWidgets.QFrame(self.sales_order_body_body)
        self.new_sales_order_body.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.new_sales_order_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_sales_order_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_sales_order_body.setObjectName("new_sales_order_body")
        self.verticalLayout_18 = QtWidgets.QVBoxLayout(self.new_sales_order_body)
        self.verticalLayout_18.setObjectName("verticalLayout_18")
        self.frame_12 = QtWidgets.QFrame(self.new_sales_order_body)
        self.frame_12.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_12.setObjectName("frame_12")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.frame_12)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.new_sales_input_body = QtWidgets.QFrame(self.frame_12)
        self.new_sales_input_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.new_sales_input_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.new_sales_input_body.setObjectName("new_sales_input_body")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.new_sales_input_body)
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        self.frame_11 = QtWidgets.QFrame(self.new_sales_input_body)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.frame_17 = QtWidgets.QFrame(self.frame_11)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.label_14 = QtWidgets.QLabel(self.frame_17)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_17.addWidget(self.label_14)
        self.new_sales_customers_name = QtWidgets.QComboBox(self.frame_17)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.new_sales_customers_name.setFont(font)
        self.new_sales_customers_name.setFocusPolicy(QtCore.Qt.NoFocus)
        self.new_sales_customers_name.setStyleSheet("")
        self.new_sales_customers_name.setEditable(True)
        self.new_sales_customers_name.setCurrentText("")
        self.new_sales_customers_name.setFrame(False)
        self.new_sales_customers_name.setObjectName("new_sales_customers_name")
        self.new_sales_customers_name.addItem("")
        self.new_sales_customers_name.setItemText(0, "")
        self.horizontalLayout_17.addWidget(self.new_sales_customers_name)
        self.verticalLayout_21.addWidget(self.frame_17)
        self.frame_18 = QtWidgets.QFrame(self.frame_11)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        self.label_15 = QtWidgets.QLabel(self.frame_18)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_18.addWidget(self.label_15)
        self.new_sales_product = QtWidgets.QComboBox(self.frame_18)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.new_sales_product.setFont(font)
        self.new_sales_product.setEditable(True)
        self.new_sales_product.setCurrentText("")
        self.new_sales_product.setObjectName("new_sales_product")
        self.horizontalLayout_18.addWidget(self.new_sales_product)
        self.verticalLayout_21.addWidget(self.frame_18)
        self.frame_19 = QtWidgets.QFrame(self.frame_11)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.label_16 = QtWidgets.QLabel(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_19.addWidget(self.label_16)
        self.new_sales_quantity = QtWidgets.QSpinBox(self.frame_19)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        self.new_sales_quantity.setFont(font)
        self.new_sales_quantity.setMaximum(9999)
        self.new_sales_quantity.setObjectName("new_sales_quantity")
        self.horizontalLayout_19.addWidget(self.new_sales_quantity)
        self.verticalLayout_21.addWidget(self.frame_19)
        self.horizontalLayout_20.addWidget(self.frame_11)
        self.frame_20 = QtWidgets.QFrame(self.new_sales_input_body)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_21.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.add_to_list_sales_order_btn = QtWidgets.QPushButton(self.frame_20)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_to_list_sales_order_btn.setFont(font)
        self.add_to_list_sales_order_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.add_to_list_sales_order_btn.setStyleSheet("padding: 10px;")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap("img/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_to_list_sales_order_btn.setIcon(icon13)
        self.add_to_list_sales_order_btn.setIconSize(QtCore.QSize(30, 30))
        self.add_to_list_sales_order_btn.setObjectName("add_to_list_sales_order_btn")
        self.horizontalLayout_21.addWidget(self.add_to_list_sales_order_btn)
        self.horizontalLayout_20.addWidget(self.frame_20)
        self.horizontalLayout_14.addWidget(self.new_sales_input_body)
        self.frame_10 = QtWidgets.QFrame(self.frame_12)
        self.frame_10.setMaximumSize(QtCore.QSize(0, 0))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_14.addWidget(self.frame_10)
        self.verticalLayout_18.addWidget(self.frame_12)
        self.frame_13 = QtWidgets.QFrame(self.new_sales_order_body)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.verticalLayout_19 = QtWidgets.QVBoxLayout(self.frame_13)
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.frame_14 = QtWidgets.QFrame(self.frame_13)
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(self.frame_14)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.new_sales_order_pay_table = QtWidgets.QTableWidget(self.frame_14)
        self.new_sales_order_pay_table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.new_sales_order_pay_table.setStyleSheet("QTableWidget#new_sales_order_pay_table{\n"
"color:rgb(84, 84, 84);\n"
"font: 12pt \"Open Sans\";\n"
"\n"
"\n"
"}\n"
"QTableWidget#new_sales_order_pay_table::item{\n"
"padding-right:10px;\n"
"\n"
"}\n"
"QTableWidget#new_sales_order_pay_table::item:selected { \n"
"\n"
"background-color: #4C4C4C;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.new_sales_order_pay_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.new_sales_order_pay_table.setAlternatingRowColors(False)
        self.new_sales_order_pay_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.new_sales_order_pay_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.new_sales_order_pay_table.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.new_sales_order_pay_table.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.new_sales_order_pay_table.setShowGrid(True)
        self.new_sales_order_pay_table.setGridStyle(QtCore.Qt.SolidLine)
        self.new_sales_order_pay_table.setCornerButtonEnabled(True)
        self.new_sales_order_pay_table.setObjectName("new_sales_order_pay_table")
        self.new_sales_order_pay_table.setColumnCount(4)
        self.new_sales_order_pay_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.new_sales_order_pay_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.new_sales_order_pay_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.new_sales_order_pay_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.new_sales_order_pay_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(47, 134, 166))
        brush.setStyle(QtCore.Qt.SolidPattern)
        item.setForeground(brush)
        self.new_sales_order_pay_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.new_sales_order_pay_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.new_sales_order_pay_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.new_sales_order_pay_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.new_sales_order_pay_table.setItem(0, 3, item)
        self.new_sales_order_pay_table.horizontalHeader().setVisible(True)
        self.new_sales_order_pay_table.horizontalHeader().setDefaultSectionSize(200)
        self.new_sales_order_pay_table.horizontalHeader().setMinimumSectionSize(100)
        self.new_sales_order_pay_table.horizontalHeader().setSortIndicatorShown(True)
        self.new_sales_order_pay_table.horizontalHeader().setStretchLastSection(True)
        self.new_sales_order_pay_table.verticalHeader().setVisible(True)
        self.new_sales_order_pay_table.verticalHeader().setCascadingSectionResizes(False)
        self.new_sales_order_pay_table.verticalHeader().setHighlightSections(False)
        self.new_sales_order_pay_table.verticalHeader().setSortIndicatorShown(True)
        self.new_sales_order_pay_table.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_20.addWidget(self.new_sales_order_pay_table)
        self.frame_16 = QtWidgets.QFrame(self.frame_14)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setContentsMargins(0, 0, 10, 0)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.label_13 = QtWidgets.QLabel(self.frame_16)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border: 3px solid rgb(52, 190, 130);\n"
"")
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_16.addWidget(self.label_13, 0, QtCore.Qt.AlignRight)
        self.verticalLayout_20.addWidget(self.frame_16)
        self.frame_15 = QtWidgets.QFrame(self.frame_14)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_15.setContentsMargins(150, 50, 150, -1)
        self.horizontalLayout_15.setSpacing(50)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.update_sales_order_btn = QtWidgets.QPushButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.update_sales_order_btn.setFont(font)
        self.update_sales_order_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.update_sales_order_btn.setStyleSheet("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap("img/refresh-cw.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.update_sales_order_btn.setIcon(icon14)
        self.update_sales_order_btn.setIconSize(QtCore.QSize(30, 30))
        self.update_sales_order_btn.setObjectName("update_sales_order_btn")
        self.horizontalLayout_15.addWidget(self.update_sales_order_btn)
        self.delete_sales_order_btn = QtWidgets.QPushButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.delete_sales_order_btn.setFont(font)
        self.delete_sales_order_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.delete_sales_order_btn.setStyleSheet("")
        icon15 = QtGui.QIcon()
        icon15.addPixmap(QtGui.QPixmap("img/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.delete_sales_order_btn.setIcon(icon15)
        self.delete_sales_order_btn.setIconSize(QtCore.QSize(30, 30))
        self.delete_sales_order_btn.setObjectName("delete_sales_order_btn")
        self.horizontalLayout_15.addWidget(self.delete_sales_order_btn)
        self.pay_sales_order_btn = QtWidgets.QPushButton(self.frame_15)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pay_sales_order_btn.setFont(font)
        self.pay_sales_order_btn.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pay_sales_order_btn.setStyleSheet("")
        icon16 = QtGui.QIcon()
        icon16.addPixmap(QtGui.QPixmap("img/shopping-cart (1).svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pay_sales_order_btn.setIcon(icon16)
        self.pay_sales_order_btn.setIconSize(QtCore.QSize(30, 30))
        self.pay_sales_order_btn.setObjectName("pay_sales_order_btn")
        self.horizontalLayout_15.addWidget(self.pay_sales_order_btn)
        self.verticalLayout_20.addWidget(self.frame_15)
        self.verticalLayout_19.addWidget(self.frame_14)
        self.verticalLayout_18.addWidget(self.frame_13)
        self.verticalLayout_18.setStretch(0, 2)
        self.verticalLayout_18.setStretch(1, 3)
        self.verticalLayout_16.addWidget(self.new_sales_order_body)
        self.sales_order_no_data = QtWidgets.QFrame(self.sales_order_body_body)
        self.sales_order_no_data.setMaximumSize(QtCore.QSize(0, 0))
        self.sales_order_no_data.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.sales_order_no_data.setFrameShadow(QtWidgets.QFrame.Raised)
        self.sales_order_no_data.setObjectName("sales_order_no_data")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.sales_order_no_data)
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_12 = QtWidgets.QLabel(self.sales_order_no_data)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_15.addWidget(self.label_12)
        self.verticalLayout_16.addWidget(self.sales_order_no_data)
        self.verticalLayout_14.addWidget(self.sales_order_body_body)
        self.verticalLayout_14.setStretch(0, 1)
        self.verticalLayout_14.setStretch(1, 7)
        self.verticalLayout_5.addWidget(self.sales_order_body)
        self.horizontalLayout_3.addWidget(self.content_body)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.verticalLayout_2.addWidget(self.body_body)
        self.footer_body = QtWidgets.QFrame(self.main_body)
        self.footer_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer_body.setObjectName("footer_body")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.footer_body)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.date_time = QtWidgets.QLabel(self.footer_body)
        font = QtGui.QFont()
        font.setFamily("Open Sans")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.date_time.setFont(font)
        self.date_time.setWordWrap(True)
        self.date_time.setObjectName("date_time")
        self.horizontalLayout_13.addWidget(self.date_time)
        self.verticalLayout_2.addWidget(self.footer_body)
        self.verticalLayout_2.setStretch(0, 5)
        self.verticalLayout_2.setStretch(1, 50)
        self.verticalLayout_2.setStretch(2, 3)
        self.verticalLayout.addWidget(self.main_body)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.header_logo.setText(_translate("MainWindow", "  Store name"))
        self.person_name.setText(_translate("MainWindow", "Gerald Michael Acero"))
        self.person_role.setText(_translate("MainWindow", "Admin"))
        __sortingEnabled = self.menu.isSortingEnabled()
        self.menu.setSortingEnabled(False)
        item = self.menu.item(0)
        item.setText(_translate("MainWindow", "Home"))
        item = self.menu.item(1)
        item.setText(_translate("MainWindow", "Sales Order"))
        item = self.menu.item(2)
        item.setText(_translate("MainWindow", "Products"))
        item = self.menu.item(3)
        item.setText(_translate("MainWindow", "Categories"))
        item = self.menu.item(4)
        item.setText(_translate("MainWindow", "Suppliers"))
        item = self.menu.item(5)
        item.setText(_translate("MainWindow", "Invoice"))
        self.menu.setSortingEnabled(__sortingEnabled)
        __sortingEnabled = self.menu2.isSortingEnabled()
        self.menu2.setSortingEnabled(False)
        item = self.menu2.item(0)
        item.setText(_translate("MainWindow", "Users"))
        item = self.menu2.item(1)
        item.setText(_translate("MainWindow", "Settings"))
        item = self.menu2.item(2)
        item.setText(_translate("MainWindow", "Logout"))
        self.menu2.setSortingEnabled(__sortingEnabled)
        self.user_message.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-family:\'Open Sans\'; font-size:16pt; color:#4c4c4c;\">Hi, User </span><span style=\" font-size:16pt; font-weight:600; font-style:italic; color:#2f86a6;\">Goodmorning</span></p></body></html>"))
        self.user_message2.setText(_translate("MainWindow", "Here is what is happening with your store today"))
        self.label.setText(_translate("MainWindow", "Total Sales"))
        self.label_2.setText(_translate("MainWindow", "999"))
        self.label_3.setText(_translate("MainWindow", "Products"))
        self.label_4.setText(_translate("MainWindow", "999"))
        self.label_5.setText(_translate("MainWindow", "Categories"))
        self.label_6.setText(_translate("MainWindow", "999"))
        self.label_7.setText(_translate("MainWindow", "Suppliers"))
        self.label_8.setText(_translate("MainWindow", "999"))
        self.label_9.setText(_translate("MainWindow", "Customers"))
        self.label_10.setText(_translate("MainWindow", "999"))
        self.label_11.setText(_translate("MainWindow", "All Sales Orders"))
        self.new_sales_order_btn.setText(_translate("MainWindow", "New"))
        self.sales_order_table.setSortingEnabled(True)
        item = self.sales_order_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.sales_order_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Date Added"))
        item = self.sales_order_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Sales Order#"))
        item = self.sales_order_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Customer Name"))
        item = self.sales_order_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        __sortingEnabled = self.sales_order_table.isSortingEnabled()
        self.sales_order_table.setSortingEnabled(False)
        item = self.sales_order_table.item(0, 0)
        item.setText(_translate("MainWindow", "4 May 2002"))
        item = self.sales_order_table.item(0, 1)
        item.setText(_translate("MainWindow", "SO-00001"))
        item = self.sales_order_table.item(0, 2)
        item.setText(_translate("MainWindow", "Customer 1"))
        item = self.sales_order_table.item(0, 3)
        item.setText(_translate("MainWindow", "9000"))
        self.sales_order_table.setSortingEnabled(__sortingEnabled)
        self.label_14.setText(_translate("MainWindow", "Customers name*"))
        self.label_15.setText(_translate("MainWindow", "Product*"))
        self.label_16.setText(_translate("MainWindow", "Quantity*"))
        self.add_to_list_sales_order_btn.setText(_translate("MainWindow", "Add order"))
        self.new_sales_order_pay_table.setSortingEnabled(True)
        item = self.new_sales_order_pay_table.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.new_sales_order_pay_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Product"))
        item = self.new_sales_order_pay_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Quantity"))
        item = self.new_sales_order_pay_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Price"))
        item = self.new_sales_order_pay_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Amount"))
        __sortingEnabled = self.new_sales_order_pay_table.isSortingEnabled()
        self.new_sales_order_pay_table.setSortingEnabled(False)
        item = self.new_sales_order_pay_table.item(0, 0)
        item.setText(_translate("MainWindow", "Helmet"))
        item = self.new_sales_order_pay_table.item(0, 1)
        item.setText(_translate("MainWindow", "2"))
        item = self.new_sales_order_pay_table.item(0, 2)
        item.setText(_translate("MainWindow", "500.00"))
        item = self.new_sales_order_pay_table.item(0, 3)
        item.setText(_translate("MainWindow", "1000.00"))
        self.new_sales_order_pay_table.setSortingEnabled(__sortingEnabled)
        self.label_13.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#2f86a6;\">Total: </span><span style=\" font-weight:400;\">1000.00</span></p></body></html>"))
        self.update_sales_order_btn.setText(_translate("MainWindow", "Update"))
        self.delete_sales_order_btn.setText(_translate("MainWindow", "Delete"))
        self.pay_sales_order_btn.setText(_translate("MainWindow", "Pay"))
        self.label_12.setText(_translate("MainWindow", "No orders yet"))
        self.date_time.setText(_translate("MainWindow", "12:00"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):


        def __init__(self, parent=None):

                super(MainWindow, self).__init__(parent=parent)
                self.setupUi(self)

                self.ss()
                self.box_shadow()
                self.get_new_sales_total()

                self.menu.itemClicked.connect(self.item_clicked)
                self.menu2.itemClicked.connect(self.item_clicked2)
                self.add_to_list_sales_order_btn.clicked.connect(self.add_to_sales_list)
                self.new_sales_order_btn.clicked.connect(self.new_sales_order_btn_funct)
                self.close_sales_order_btn.clicked.connect(self.close_sales_order_btn_funct)

                self.new_sales_order_pay_table.cellClicked.connect(self.new_sales_order_pay_table_clicked) 

                self.loaddata()
                self.update_new_sales_total()
                
                cname_list = ['Pedro', 'Juan', 'Johny', 'Kevin', 'Ronaldo']
                

                self.new_sales_product.addItems(self.prdct())
                self.new_sales_customers_name.addItems(cname_list)

        def prdct(self):

                prdct_list = ['Coke', 'Sprite', 'Royal', 'Mug Beer', 'Royal Crown']

                return prdct_list

        def new_sales_order_pay_table_clicked(self, row, column):

                item = self.new_sales_order_pay_table.itemAt(row, column)

                get = self.get_items()
                count = len(get)

                prdct_list = self.prdct()
                
                product = []
                quantity = []
                price = []
                amount = []

                for i in range(count):

                        a = get[i]
                        product.append(a[0])
                        quantity.append(a[1])
                        price.append(a[2])
                        amount.append(a[3])

                table_data = [product[row],quantity[row],price[row],amount[row]]

                self.new_sales_product.setCurrentIndex(prdct_list.index(str(table_data[0])))

                print(f"Product: {str(table_data[0])}")
                print(f"Qty: {str(table_data[1])}")
                print(f"Price: {str(table_data[2])}")
                print(f"Amount: {str(table_data[3])}")

                self.show_new_sales_btn()

        def show_new_sales_btn(self):
                
                self.update_sales_order_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.delete_sales_order_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.pay_sales_order_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))

        def hide_new_sales_btn(self):

                self.update_sales_order_btn.setMaximumSize(QtCore.QSize(0, 0))
                self.delete_sales_order_btn.setMaximumSize(QtCore.QSize(0, 0))
                self.pay_sales_order_btn.setMaximumSize(QtCore.QSize(0, 0))

        def new_sales_order_btn_funct(self):

                self.new_sales_order_btn.setMaximumSize(QtCore.QSize(0, 0))
                self.close_sales_order_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))

                self.label_11.setText('New Sales Order')

                self.sales_order_no_data.setMaximumSize(QtCore.QSize(0, 0))
                self.new_sales_order_body.setMaximumSize(QtCore.QSize(16777215, 16777215))

        def close_sales_order_btn_funct(self):

                self.new_sales_order_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.close_sales_order_btn.setMaximumSize(QtCore.QSize(0, 0))

                self.label_11.setText('All Sales Order')

                self.sales_order_no_data.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.new_sales_order_body.setMaximumSize(QtCore.QSize(0, 0))



        def update_new_sales_total(self):

                get_amount = self.get_new_sales_total()
                self.label_13.setText(f"""<html><head/><body><p><span style=" color:#2f86a6;">Total: </span><span style=" font-weight:400;">{get_amount}</span></p></body></html>""")
       
        def get_new_sales_total(self):
                
                with conn:

                        c.execute(" SELECT amount FROM new_sales ")

                        rs = c.fetchall()   

                        try:
                                amount = []
                                for i in range(len(rs)):

                                        a = rs[i]
                                        amount.append(a[0])

                                total = 0
                                for val in amount:
                                        total = total + val

                                        formatted_total = "₱ {:,.2f}".format(total)

                                return formatted_total

                        except Exception as e:
                                print(e)


        def add_to_sales_list(self):

                get_cname = self.new_sales_customers_name.currentText()
                get_product = self.new_sales_product.currentText()
                get_qty = self.new_sales_quantity.text()
                get_price = 10
                

                self.add_items(get_cname, get_product, get_qty, get_price)
                

        def add_items(self,cname,product,qty, price):

                amount = int(qty)*price
                

                with conn:
                 c.execute("INSERT INTO new_sales VALUES (:cname, :product, :qty, :price, :amount)", {'cname': cname,'product': product,'qty': qty,'price': price,'amount': amount})  
                self.loaddata()
                self.update_new_sales_total()


        def get_items(self):

                with conn:
                        c.execute(" SELECT product, quantity, price, amount FROM new_sales ")
                        return c.fetchall() 

        def loaddata(self):

                get = self.get_items()
                # print(get)
                count = len(get)

                cname = []
                product = []
                quantity = []
                price = []
                amount = []


                for i in range(len(get)):

                        a = get[i]
                        product.append(a[1])
                        quantity.append(a[2])
                        price.append(a[1])
                        amount.append(a[1])

                        tablerow=0
                
                        self.new_sales_order_pay_table.setRowCount(count)

                        # item = QtWidgets.QTableWidgetItem()
                        # item.setTextAlignment(QtCore.Qt.AlignCenter)
                        
                        for row in get:

                                item = QtWidgets.QTableWidgetItem
                                

                                self.new_sales_order_pay_table.setItem(tablerow, 0, item(str(row[0])))
                                
                                self.new_sales_order_pay_table.setItem(tablerow, 1, QtWidgets.QTableWidgetItem(str(row[1])))
                                self.new_sales_order_pay_table.setItem(tablerow, 2, QtWidgets.QTableWidgetItem(str(row[2])))
                                self.new_sales_order_pay_table.setItem(tablerow, 3, QtWidgets.QTableWidgetItem(str(row[3])))

                                # item.setTextAlignment(QtCore.Qt.AlignCenter)
                                


        
                                # self.new_sales_order_pay_table.setItem(tablerow, 0, item)

                                

                                
                                tablerow+=1
                        

        def showtime(self):
                
                datetime = QDateTime.currentDateTime()
                text = datetime.toString("ddd | MMMM d, yyyy | hh:mm:ss AP")
                self.date_time.setText("   "+ text)

        def item_clicked(self,item):
                self.menu2.clearSelection()
                value = item.text()
                
                if value == 'Home':

                        self.sales_order_body.setMaximumSize(QtCore.QSize(0, 0))
                        self.home_body.setMaximumSize(QtCore.QSize(16777215, 16777215))

                elif value == 'Sales Order':
                        
                        self.sales_order_body.setMaximumSize(QtCore.QSize(16777215, 16777215))
                        self.home_body.setMaximumSize(QtCore.QSize(0, 0))

        def item_clicked2(self,item):
                self.menu.clearSelection()
                value = item.text()
                
                if value == 'Users':
                        
                        print('Users')

                elif value == 'Settings':
                        
                        print('Settings')
                                
        
        def box_shadow(self):

                blur = 22
                x = 1
                y = 2
                
                self.totals_sales_body.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=blur,xOffset=x,yOffset=y))
                self.sales_order_body.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=blur,xOffset=x,yOffset=y))
                self.totals_products_body.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=blur,xOffset=x,yOffset=y))
                self.totals_products_body_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=blur,xOffset=x,yOffset=y))
                self.totals_products_body_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=blur,xOffset=x,yOffset=y))
                self.totals_products_body_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=blur,xOffset=x,yOffset=y))

        def ss(self):

                self.menu.setSpacing(5)
                self.menu2.setSpacing(5)
                self.menu.setCurrentRow(0)
                self.new_sales_order_btn.setMaximumSize(QtCore.QSize(16777215, 16777215))
                self.close_sales_order_btn.setMaximumSize(QtCore.QSize(0, 0))

                self.hide_new_sales_btn()

                timer = QTimer(self)
                timer.timeout.connect(self.showtime)
                timer.start()

                self.new_sales_customers_name.setStyleSheet("font-size: 20px;")
                self.new_sales_product.setStyleSheet("font-size: 20px;")

                self.label_13.setText(f"""<html><head/><body><p><span style=" color:#2f86a6;">Total: </span><span style=" font-weight:400;">{"0.00"}</span></p></body></html>""")

                # self.new_sales_customers_name.setStyleSheet("QComboBox {subcontrol-origin: padding;subcontrol-position: top right;selection-background-color: #111;selection-color: yellow;color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);border-style: solid;border: 1px solid #1e1e1e;border-radius: 5;padding: 1px 0px 1px 20px;}QComboBox:hover, QPushButton:hover {border: 1px solid yellow;color: white;}QComboBox:editable {background: red;color: pink;}QComboBox:on {padding-top: 0px;padding-left: 0px;color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);selection-background-color: #ffaa00;}QComboBox:!on {color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);}QComboBox QAbstractItemView {border: 2px solid darkgray;color: black;selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);}QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;color: white;border-left-width: 0px;border-left-color: darkgray;border-left-style: solid;border-top-right-radius: 3px;border-bottom-right-radius: 3px;padding-left: 10px;}QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow {image: url("+cart+");width: 20px;height: 20px;}")
                # self.new_sales_product.setStyleSheet("QComboBox {subcontrol-origin: padding;subcontrol-position: top right;selection-background-color: #111;selection-color: yellow;color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);border-style: solid;border: 1px solid #1e1e1e;border-radius: 5;padding: 1px 0px 1px 20px;}QComboBox:hover, QPushButton:hover {border: 1px solid yellow;color: white;}QComboBox:editable {background: red;color: pink;}QComboBox:on {padding-top: 0px;padding-left: 0px;color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);selection-background-color: #ffaa00;}QComboBox:!on {color: white;background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #666, stop: 0.1 #555, stop: 0.5 #555, stop: 0.9 #444, stop: 1 #333);}QComboBox QAbstractItemView {border: 2px solid darkgray;color: black;selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #111, stop: 1 #333);}QComboBox::drop-down {subcontrol-origin: padding;subcontrol-position: top right;width: 15px;color: white;border-left-width: 0px;border-left-color: darkgray;border-left-style: solid;border-top-right-radius: 3px;border-bottom-right-radius: 3px;padding-left: 10px;}QComboBox::down-arrow, QSpinBox::down-arrow, QTimeEdit::down-arrow, QDateEdit::down-arrow {image: url("+cart+");width: 20px;height: 20px;}")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


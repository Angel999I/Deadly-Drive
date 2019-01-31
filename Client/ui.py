# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(985, 602)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 99999))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(19)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../../Desktop/output-onlinepngtools.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("\n"
"    background-color: rgb(255, 255, 255);\n"
"    \n"
"")
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stacked_widget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked_widget.setGeometry(QtCore.QRect(0, 0, 981, 581))
        self.stacked_widget.setStyleSheet("")
        self.stacked_widget.setObjectName("stacked_widget")
        self.page_connecting = QtWidgets.QWidget()
        self.page_connecting.setObjectName("page_connecting")
        self.frame_ip_4 = QtWidgets.QFrame(self.page_connecting)
        self.frame_ip_4.setGeometry(QtCore.QRect(360, 160, 281, 231))
        self.frame_ip_4.setStyleSheet("QFrame{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 9px; \n"
"}")
        self.frame_ip_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ip_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ip_4.setObjectName("frame_ip_4")
        self.connecting_label_idle = QtWidgets.QLabel(self.frame_ip_4)
        self.connecting_label_idle.setGeometry(QtCore.QRect(80, 110, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.connecting_label_idle.setFont(font)
        self.connecting_label_idle.setStyleSheet("QLabel{\n"
"    color: solid black;\n"
"    border: 0px\n"
"}\n"
"")
        self.connecting_label_idle.setObjectName("connecting_label_idle")
        self.connecting_label_title_1 = QtWidgets.QLabel(self.frame_ip_4)
        self.connecting_label_title_1.setGeometry(QtCore.QRect(10, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.connecting_label_title_1.setFont(font)
        self.connecting_label_title_1.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.connecting_label_title_1.setObjectName("connecting_label_title_1")
        self.connecting_label_title_2 = QtWidgets.QLabel(self.frame_ip_4)
        self.connecting_label_title_2.setGeometry(QtCore.QRect(170, 10, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.connecting_label_title_2.setFont(font)
        self.connecting_label_title_2.setStyleSheet("QLabel{\n"
"    color: rgb(15, 112, 232);\n"
"    border: 0px\n"
"}")
        self.connecting_label_title_2.setObjectName("connecting_label_title_2")
        self.stacked_widget.addWidget(self.page_connecting)
        self.page_ip = QtWidgets.QWidget()
        self.page_ip.setObjectName("page_ip")
        self.frame_ip = QtWidgets.QFrame(self.page_ip)
        self.frame_ip.setGeometry(QtCore.QRect(300, 80, 411, 401))
        self.frame_ip.setStyleSheet("QFrame{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 9px; \n"
"}")
        self.frame_ip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_ip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ip.setObjectName("frame_ip")
        self.ip_line_edit_ipaddress = QtWidgets.QLineEdit(self.frame_ip)
        self.ip_line_edit_ipaddress.setGeometry(QtCore.QRect(20, 140, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.ip_line_edit_ipaddress.setFont(font)
        self.ip_line_edit_ipaddress.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"\n"
"")
        self.ip_line_edit_ipaddress.setInputMethodHints(QtCore.Qt.ImhNone)
        self.ip_line_edit_ipaddress.setInputMask("")
        self.ip_line_edit_ipaddress.setText("")
        self.ip_line_edit_ipaddress.setObjectName("ip_line_edit_ipaddress")
        self.ip_button_next = QtWidgets.QPushButton(self.frame_ip)
        self.ip_button_next.setGeometry(QtCore.QRect(310, 340, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ip_button_next.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ip_button_next.setFont(font)
        self.ip_button_next.setMouseTracking(False)
        self.ip_button_next.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 115, 232);\n"
"color: white;\n"
"border: 2px rgb(26, 115, 232);\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}")
        self.ip_button_next.setAutoDefault(False)
        self.ip_button_next.setDefault(False)
        self.ip_button_next.setFlat(False)
        self.ip_button_next.setObjectName("ip_button_next")
        self.ip_label_ipsetup = QtWidgets.QLabel(self.frame_ip)
        self.ip_label_ipsetup.setGeometry(QtCore.QRect(160, 80, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ip_label_ipsetup.setFont(font)
        self.ip_label_ipsetup.setStyleSheet("QLabel{\n"
"    color: solid black;\n"
"    border: 0px\n"
"}\n"
"")
        self.ip_label_ipsetup.setObjectName("ip_label_ipsetup")
        self.ip_label_title1 = QtWidgets.QLabel(self.frame_ip)
        self.ip_label_title1.setGeometry(QtCore.QRect(90, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.ip_label_title1.setFont(font)
        self.ip_label_title1.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.ip_label_title1.setObjectName("ip_label_title1")
        self.ip_label_title2 = QtWidgets.QLabel(self.frame_ip)
        self.ip_label_title2.setGeometry(QtCore.QRect(240, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.ip_label_title2.setFont(font)
        self.ip_label_title2.setStyleSheet("QLabel{\n"
"    color: rgb(15, 112, 232);\n"
"    border: 0px\n"
"}")
        self.ip_label_title2.setObjectName("ip_label_title2")
        self.ip_button_exit = QtWidgets.QPushButton(self.frame_ip)
        self.ip_button_exit.setGeometry(QtCore.QRect(20, 340, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.ip_button_exit.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.ip_button_exit.setFont(font)
        self.ip_button_exit.setMouseTracking(False)
        self.ip_button_exit.setStyleSheet("QPushButton {\n"
"background-color: rgb(255, 0, 0);\n"
"color: white;\n"
"border: 2px rgb(26, 115, 232);\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}")
        self.ip_button_exit.setAutoDefault(False)
        self.ip_button_exit.setDefault(False)
        self.ip_button_exit.setFlat(False)
        self.ip_button_exit.setObjectName("ip_button_exit")
        self.stacked_widget.addWidget(self.page_ip)
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.frame_login = QtWidgets.QFrame(self.page_login)
        self.frame_login.setGeometry(QtCore.QRect(300, 30, 421, 511))
        self.frame_login.setStyleSheet("QFrame{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 9px; \n"
"}")
        self.frame_login.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_login.setObjectName("frame_login")
        self.login_line_edit_email = QtWidgets.QLineEdit(self.frame_login)
        self.login_line_edit_email.setGeometry(QtCore.QRect(20, 140, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.login_line_edit_email.setFont(font)
        self.login_line_edit_email.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"\n"
"")
        self.login_line_edit_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.login_line_edit_email.setInputMask("")
        self.login_line_edit_email.setText("")
        self.login_line_edit_email.setObjectName("login_line_edit_email")
        self.login_line_edit_password = QtWidgets.QLineEdit(self.frame_login)
        self.login_line_edit_password.setGeometry(QtCore.QRect(20, 210, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.login_line_edit_password.setFont(font)
        self.login_line_edit_password.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"")
        self.login_line_edit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        self.login_line_edit_password.setObjectName("login_line_edit_password")
        self.login_button_next = QtWidgets.QPushButton(self.frame_login)
        self.login_button_next.setGeometry(QtCore.QRect(320, 450, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.login_button_next.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.login_button_next.setFont(font)
        self.login_button_next.setMouseTracking(False)
        self.login_button_next.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 115, 232);\n"
"color: white;\n"
"border: 2px rgb(26, 115, 232);\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}")
        self.login_button_next.setAutoDefault(False)
        self.login_button_next.setDefault(False)
        self.login_button_next.setFlat(False)
        self.login_button_next.setObjectName("login_button_next")
        self.login_label_login = QtWidgets.QLabel(self.frame_login)
        self.login_label_login.setGeometry(QtCore.QRect(170, 80, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.login_label_login.setFont(font)
        self.login_label_login.setStyleSheet("QLabel{\n"
"    color: solid black;\n"
"    border: 0px\n"
"}\n"
"")
        self.login_label_login.setObjectName("login_label_login")
        self.login_label_title_1 = QtWidgets.QLabel(self.frame_login)
        self.login_label_title_1.setGeometry(QtCore.QRect(90, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.login_label_title_1.setFont(font)
        self.login_label_title_1.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.login_label_title_1.setObjectName("login_label_title_1")
        self.login_label_title_2 = QtWidgets.QLabel(self.frame_login)
        self.login_label_title_2.setGeometry(QtCore.QRect(240, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.login_label_title_2.setFont(font)
        self.login_label_title_2.setStyleSheet("QLabel{\n"
"    color: rgb(15, 112, 232);\n"
"    border: 0px\n"
"}")
        self.login_label_title_2.setObjectName("login_label_title_2")
        self.login_button_account = QtWidgets.QPushButton(self.frame_login)
        self.login_button_account.setGeometry(QtCore.QRect(20, 450, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.login_button_account.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.login_button_account.setFont(font)
        self.login_button_account.setMouseTracking(False)
        self.login_button_account.setStyleSheet("QPushButton {\n"
"color:rgb(32, 115, 232);\n"
"border: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}")
        self.login_button_account.setAutoDefault(False)
        self.login_button_account.setDefault(False)
        self.login_button_account.setFlat(False)
        self.login_button_account.setObjectName("login_button_account")
        self.stacked_widget.addWidget(self.page_login)
        self.page_regiser = QtWidgets.QWidget()
        self.page_regiser.setObjectName("page_regiser")
        self.register_frame = QtWidgets.QFrame(self.page_regiser)
        self.register_frame.setGeometry(QtCore.QRect(300, 30, 421, 511))
        self.register_frame.setStyleSheet("QFrame{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 9px; \n"
"}")
        self.register_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.register_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_frame.setObjectName("register_frame")
        self.register_line_edit_email = QtWidgets.QLineEdit(self.register_frame)
        self.register_line_edit_email.setGeometry(QtCore.QRect(20, 210, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.register_line_edit_email.setFont(font)
        self.register_line_edit_email.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"\n"
"")
        self.register_line_edit_email.setInputMethodHints(QtCore.Qt.ImhNone)
        self.register_line_edit_email.setInputMask("")
        self.register_line_edit_email.setText("")
        self.register_line_edit_email.setObjectName("register_line_edit_email")
        self.register_line_edit_password = QtWidgets.QLineEdit(self.register_frame)
        self.register_line_edit_password.setGeometry(QtCore.QRect(20, 280, 381, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.register_line_edit_password.setFont(font)
        self.register_line_edit_password.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px;\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"")
        self.register_line_edit_password.setInputMethodHints(QtCore.Qt.ImhHiddenText|QtCore.Qt.ImhSensitiveData)
        self.register_line_edit_password.setObjectName("register_line_edit_password")
        self.register_button_next = QtWidgets.QPushButton(self.register_frame)
        self.register_button_next.setGeometry(QtCore.QRect(320, 450, 81, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.register_button_next.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.register_button_next.setFont(font)
        self.register_button_next.setMouseTracking(False)
        self.register_button_next.setStyleSheet("QPushButton {\n"
"background-color: rgb(32, 115, 232);\n"
"color: white;\n"
"border: 2px rgb(26, 115, 232);\n"
"border-radius: 6px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}")
        self.register_button_next.setAutoDefault(False)
        self.register_button_next.setDefault(False)
        self.register_button_next.setFlat(False)
        self.register_button_next.setObjectName("register_button_next")
        self.register_label_new = QtWidgets.QLabel(self.register_frame)
        self.register_label_new.setGeometry(QtCore.QRect(70, 80, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.register_label_new.setFont(font)
        self.register_label_new.setStyleSheet("QLabel{\n"
"    color: solid black;\n"
"    border: 0px\n"
"}\n"
"")
        self.register_label_new.setObjectName("register_label_new")
        self.registe_label_title_1 = QtWidgets.QLabel(self.register_frame)
        self.registe_label_title_1.setGeometry(QtCore.QRect(90, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.registe_label_title_1.setFont(font)
        self.registe_label_title_1.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.registe_label_title_1.setObjectName("registe_label_title_1")
        self.register_label_title_2 = QtWidgets.QLabel(self.register_frame)
        self.register_label_title_2.setGeometry(QtCore.QRect(240, 10, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.register_label_title_2.setFont(font)
        self.register_label_title_2.setStyleSheet("QLabel{\n"
"    color: rgb(15, 112, 232);\n"
"    border: 0px\n"
"}")
        self.register_label_title_2.setObjectName("register_label_title_2")
        self.register_button_login = QtWidgets.QPushButton(self.register_frame)
        self.register_button_login.setGeometry(QtCore.QRect(20, 450, 61, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(32, 115, 232))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.register_button_login.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.register_button_login.setFont(font)
        self.register_button_login.setMouseTracking(False)
        self.register_button_login.setStyleSheet("QPushButton {\n"
"color:rgb(32, 115, 232);\n"
"border: 0px;\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"}")
        self.register_button_login.setAutoDefault(False)
        self.register_button_login.setDefault(False)
        self.register_button_login.setFlat(False)
        self.register_button_login.setObjectName("register_button_login")
        self.register_line_edit_first_name = QtWidgets.QLineEdit(self.register_frame)
        self.register_line_edit_first_name.setGeometry(QtCore.QRect(20, 140, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.register_line_edit_first_name.setFont(font)
        self.register_line_edit_first_name.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"\n"
"")
        self.register_line_edit_first_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.register_line_edit_first_name.setInputMask("")
        self.register_line_edit_first_name.setText("")
        self.register_line_edit_first_name.setObjectName("register_line_edit_first_name")
        self.register_line_edit_last_name = QtWidgets.QLineEdit(self.register_frame)
        self.register_line_edit_last_name.setGeometry(QtCore.QRect(220, 140, 181, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.register_line_edit_last_name.setFont(font)
        self.register_line_edit_last_name.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"\n"
"")
        self.register_line_edit_last_name.setInputMethodHints(QtCore.Qt.ImhNone)
        self.register_line_edit_last_name.setInputMask("")
        self.register_line_edit_last_name.setText("")
        self.register_line_edit_last_name.setObjectName("register_line_edit_last_name")
        self.stacked_widget.addWidget(self.page_regiser)
        self.page_files = QtWidgets.QWidget()
        self.page_files.setObjectName("page_files")
        self.files_frame_border = QtWidgets.QFrame(self.page_files)
        self.files_frame_border.setGeometry(QtCore.QRect(10, 10, 971, 561))
        self.files_frame_border.setStyleSheet("QFrame{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 9px; \n"
"}")
        self.files_frame_border.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.files_frame_border.setFrameShadow(QtWidgets.QFrame.Raised)
        self.files_frame_border.setObjectName("files_frame_border")
        self.files_label_title_1 = QtWidgets.QLabel(self.files_frame_border)
        self.files_label_title_1.setGeometry(QtCore.QRect(350, 10, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.files_label_title_1.setFont(font)
        self.files_label_title_1.setStyleSheet("QLabel{\n"
"    border: 0px;\n"
"    color: rgb(255, 0, 0);\n"
"}")
        self.files_label_title_1.setObjectName("files_label_title_1")
        self.files_label_title_2 = QtWidgets.QLabel(self.files_frame_border)
        self.files_label_title_2.setGeometry(QtCore.QRect(510, 10, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Forte")
        font.setPointSize(28)
        self.files_label_title_2.setFont(font)
        self.files_label_title_2.setStyleSheet("QLabel{\n"
"    color: rgb(15, 112, 232);\n"
"    border: 0px\n"
"}")
        self.files_label_title_2.setObjectName("files_label_title_2")
        self.files_line_edit_commands = QtWidgets.QLineEdit(self.files_frame_border)
        self.files_line_edit_commands.setGeometry(QtCore.QRect(10, 520, 951, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Light")
        font.setPointSize(12)
        self.files_line_edit_commands.setFont(font)
        self.files_line_edit_commands.setStyleSheet("QLineEdit{\n"
"    border: 1.25px solid rgb(194, 194, 194);\n"
"    border-radius: 3.5px\n"
"}\n"
"QLineEdit:hover{\n"
"    border: 1.25px solid rgb(15, 112, 232)\n"
"}\n"
"\n"
"")
        self.files_line_edit_commands.setInputMethodHints(QtCore.Qt.ImhNone)
        self.files_line_edit_commands.setInputMask("")
        self.files_line_edit_commands.setText("")
        self.files_line_edit_commands.setPlaceholderText("")
        self.files_line_edit_commands.setObjectName("files_line_edit_commands")
        self.files_text_edit_console = QtWidgets.QTextEdit(self.files_frame_border)
        self.files_text_edit_console.setEnabled(False)
        self.files_text_edit_console.setGeometry(QtCore.QRect(10, 120, 951, 391))
        self.files_text_edit_console.setStyleSheet("QTextEdit\n"
"{\n"
"    background-color: black;\n"
"    color: white;\n"
"}")
        self.files_text_edit_console.setObjectName("files_text_edit_console")
        self.files_progress_bar = QtWidgets.QProgressBar(self.files_frame_border)
        self.files_progress_bar.setGeometry(QtCore.QRect(20, 70, 931, 31))
        self.files_progress_bar.setProperty("value", 0)
        self.files_progress_bar.setTextVisible(False)
        self.files_progress_bar.setObjectName("files_progress_bar")
        self.help_1 = QtWidgets.QLabel(self.files_frame_border)
        self.help_1.setGeometry(QtCore.QRect(780, 140, 41, 16))
        self.help_1.setStyleSheet("QLabel\n"
"{\n"
"    color: white;\n"
"    background-color: black;\n"
"}")
        self.help_1.setObjectName("help_1")
        self.help_2 = QtWidgets.QTextEdit(self.files_frame_border)
        self.help_2.setEnabled(False)
        self.help_2.setGeometry(QtCore.QRect(650, 170, 301, 211))
        self.help_2.setStyleSheet("QTextEdit\n"
"{\n"
"    border-radius: 0px;\n"
"    background-color: black;\n"
"    color: white;\n"
"}")
        self.help_2.setObjectName("help_2")
        self.stacked_widget.addWidget(self.page_files)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stacked_widget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Deadly Drive"))
        self.connecting_label_idle.setText(_translate("MainWindow", "Connecting..."))
        self.connecting_label_title_1.setText(_translate("MainWindow", "Deadly"))
        self.connecting_label_title_2.setText(_translate("MainWindow", "Drive"))
        self.ip_line_edit_ipaddress.setPlaceholderText(_translate("MainWindow", "  IP Address"))
        self.ip_button_next.setText(_translate("MainWindow", "Next"))
        self.ip_label_ipsetup.setText(_translate("MainWindow", "IP Setup"))
        self.ip_label_title1.setText(_translate("MainWindow", "Deadly"))
        self.ip_label_title2.setText(_translate("MainWindow", "Drive"))
        self.ip_button_exit.setText(_translate("MainWindow", "Exit"))
        self.login_line_edit_email.setPlaceholderText(_translate("MainWindow", "  Email"))
        self.login_line_edit_password.setPlaceholderText(_translate("MainWindow", "  Password"))
        self.login_button_next.setText(_translate("MainWindow", "Next"))
        self.login_label_login.setText(_translate("MainWindow", "Sign In"))
        self.login_label_title_1.setText(_translate("MainWindow", "Deadly"))
        self.login_label_title_2.setText(_translate("MainWindow", "Drive"))
        self.login_button_account.setText(_translate("MainWindow", "Create new account"))
        self.register_line_edit_email.setPlaceholderText(_translate("MainWindow", "  Email"))
        self.register_line_edit_password.setPlaceholderText(_translate("MainWindow", "  Password"))
        self.register_button_next.setText(_translate("MainWindow", "Next"))
        self.register_label_new.setText(_translate("MainWindow", "Hey! You are new here right?"))
        self.registe_label_title_1.setText(_translate("MainWindow", "Deadly"))
        self.register_label_title_2.setText(_translate("MainWindow", "Drive"))
        self.register_button_login.setText(_translate("MainWindow", "Login"))
        self.register_line_edit_first_name.setPlaceholderText(_translate("MainWindow", "  First name"))
        self.register_line_edit_last_name.setPlaceholderText(_translate("MainWindow", "  Last name"))
        self.files_label_title_1.setText(_translate("MainWindow", "Deadly"))
        self.files_label_title_2.setText(_translate("MainWindow", "Drive"))
        self.help_1.setText(_translate("MainWindow", "HELP:"))
        self.help_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">exit:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Close the program</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">dir:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Get the list of files from the server</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">upload [FILENAME]:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Upload a file to the server</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">The file need\'s to be in the files folder</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">download [FILENAME]:</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Download file from your userid directory</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


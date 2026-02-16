# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LoginWidget.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import resources_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(800, 600)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(800, 600))
        Login.setStyleSheet(u"QWidget#Login {\n"
"    \n"
"	\n"
"	background-image: url(:/images/assets/login_bg_small.png);\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"	background-size: cover;\n"
"}\n"
"")
        self.frameLogin = QFrame(Login)
        self.frameLogin.setObjectName(u"frameLogin")
        self.frameLogin.setGeometry(QRect(50, 130, 400, 250))
        sizePolicy.setHeightForWidth(self.frameLogin.sizePolicy().hasHeightForWidth())
        self.frameLogin.setSizePolicy(sizePolicy)
        self.frameLogin.setMinimumSize(QSize(400, 250))
        self.frameLogin.setMaximumSize(QSize(400, 250))
        self.frameLogin.setStyleSheet(u"QFrame#frameLogin {\n"
"    background: rgba(0, 0, 0, 120);\n"
"    border: 1px solid rgba(255, 255, 255, 40);\n"
"    border-radius: 14px;\n"
"}\n"
"")
        self.frameLogin.setFrameShape(QFrame.Shape.StyledPanel)
        self.frameLogin.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frameLogin)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblUsername = QLabel(self.frameLogin)
        self.lblUsername.setObjectName(u"lblUsername")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblUsername.sizePolicy().hasHeightForWidth())
        self.lblUsername.setSizePolicy(sizePolicy1)
        self.lblUsername.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"")

        self.verticalLayout.addWidget(self.lblUsername)

        self.leUsername = QLineEdit(self.frameLogin)
        self.leUsername.setObjectName(u"leUsername")
        self.leUsername.setMinimumSize(QSize(0, 40))
        self.leUsername.setStyleSheet(u"QLineEdit{\n"
"  padding: 8px 10px;\n"
"  border-radius: 8px;\n"
"  background: rgba(255,255,255,220);\n"
"  border: 1px solid rgba(255,255,255,60);\n"
"  font-size: 13px;\n"
"}\n"
"QLineEdit:focus{\n"
"  border: 1px solid rgba(45,212,255,180);\n"
"  background: rgba(255,255,255,240);\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.leUsername)

        self.lblPassword = QLabel(self.frameLogin)
        self.lblPassword.setObjectName(u"lblPassword")
        sizePolicy1.setHeightForWidth(self.lblPassword.sizePolicy().hasHeightForWidth())
        self.lblPassword.setSizePolicy(sizePolicy1)
        self.lblPassword.setStyleSheet(u"color: white;\n"
"font-size: 12px;\n"
"")

        self.verticalLayout.addWidget(self.lblPassword)

        self.lePassword = QLineEdit(self.frameLogin)
        self.lePassword.setObjectName(u"lePassword")
        self.lePassword.setStyleSheet(u"QLineEdit{\n"
"  padding: 8px 10px;\n"
"  border-radius: 8px;\n"
"  background: rgba(255,255,255,220);\n"
"  border: 1px solid rgba(255,255,255,60);\n"
"  font-size: 13px;\n"
"}\n"
"QLineEdit:focus{\n"
"  border: 1px solid rgba(45,212,255,180);\n"
"  background: rgba(255,255,255,240);\n"
"}\n"
"")
        self.lePassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout.addWidget(self.lePassword)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnLogin = QPushButton(self.frameLogin)
        self.btnLogin.setObjectName(u"btnLogin")
        sizePolicy.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy)
        self.btnLogin.setMinimumSize(QSize(120, 40))
        self.btnLogin.setStyleSheet(u"QPushButton#btnLogin {\n"
"    background: rgba(45, 212, 255, 220);\n"
"    color: white;\n"
"    border-radius: 12px;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"QPushButton#btnLogin:hover {\n"
"    background: rgba(45, 212, 255, 255);\n"
"}\n"
"QPushButton#btnLogin:pressed {\n"
"    background: rgba(34, 193, 220, 255);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnLogin)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.lblUsername.setText(QCoreApplication.translate("Login", u"Username", None))
        self.leUsername.setText("")
        self.leUsername.setPlaceholderText(QCoreApplication.translate("Login", u"username", None))
        self.lblPassword.setText(QCoreApplication.translate("Login", u"Password", None))
        self.lePassword.setPlaceholderText(QCoreApplication.translate("Login", u"password", None))
        self.btnLogin.setText(QCoreApplication.translate("Login", u"Login", None))
    # retranslateUi


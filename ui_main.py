# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QToolBox, QVBoxLayout, QWidget)
import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1097, 712)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	border: none\n"
"}\n"
"\n"
"QLabel {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.F01main = QFrame(self.centralwidget)
        self.F01main.setObjectName(u"F01main")
        self.F01main.setFrameShape(QFrame.StyledPanel)
        self.F01main.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.F01main)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.F01menu = QFrame(self.F01main)
        self.F01menu.setObjectName(u"F01menu")
        self.F01menu.setMaximumSize(QSize(9, 16777215))
        self.F01menu.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(223, 223, 223);	\n"
"}\n"
"\n"
"QToolBox {\n"
"	text-align:left;\n"
"	\n"
"	background-color: rgb(228, 254, 255);\n"
"}\n"
"\n"
"QToolBox::tab {\n"
"	border-radius: 5px	\n"
"	background-color: rgb(194, 232, 255);\n"
"	text-align:left;\n"
"}")
        self.F01menu.setFrameShape(QFrame.StyledPanel)
        self.F01menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.F01menu)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(6, 6, 6, 6)
        self.toolBox = QToolBox(self.F01menu)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setStyleSheet(u"QPushButton:hover {\n"
"	background-color: rgb(0, 255, 255);\n"
"	border-top-left-radius: 15px\n"
"}\n"
"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 122, 629))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btnLancamentos = QPushButton(self.page)
        self.btnLancamentos.setObjectName(u"btnLancamentos")
        self.btnLancamentos.setMinimumSize(QSize(0, 30))
        self.btnLancamentos.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(11)
        self.btnLancamentos.setFont(font)
        self.btnLancamentos.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btnLancamentos)

        self.btmFluxoCaixa = QPushButton(self.page)
        self.btmFluxoCaixa.setObjectName(u"btmFluxoCaixa")
        self.btmFluxoCaixa.setMinimumSize(QSize(0, 30))
        self.btmFluxoCaixa.setMaximumSize(QSize(16777215, 30))
        self.btmFluxoCaixa.setFont(font)
        self.btmFluxoCaixa.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.btmFluxoCaixa)

        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(0, 30))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.page, u"Atividades")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 188, 646))
        self.verticalLayout_3 = QVBoxLayout(self.page_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_5 = QPushButton(self.page_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(0, 30))
        self.pushButton_5.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.page_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setMinimumSize(QSize(0, 30))
        self.pushButton_6.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_3.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.page_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(0, 30))
        self.pushButton_7.setMaximumSize(QSize(16777215, 50))

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.page_2, u"Cadastros")

        self.verticalLayout.addWidget(self.toolBox)


        self.horizontalLayout_2.addWidget(self.F01menu)

        self.F02tela = QFrame(self.F01main)
        self.F02tela.setObjectName(u"F02tela")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.F02tela.sizePolicy().hasHeightForWidth())
        self.F02tela.setSizePolicy(sizePolicy)
        self.F02tela.setStyleSheet(u"background-color: rgb(203, 203, 203);")
        self.F02tela.setFrameShape(QFrame.StyledPanel)
        self.F02tela.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.F02tela)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_toggle = QPushButton(self.F02tela)
        self.btn_toggle.setObjectName(u"btn_toggle")
        self.btn_toggle.setMaximumSize(QSize(100, 25))
        icon = QIcon()
        icon.addFile(u":/imagens/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

        self.frame = QFrame(self.F02tela)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgb(223, 223, 223);")

        self.verticalLayout_5.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.F02tela)


        self.horizontalLayout.addWidget(self.F01main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Tela Principal", None))
        self.btnLancamentos.setText(QCoreApplication.translate("MainWindow", u"Lan\u00e7amentos", None))
        self.btmFluxoCaixa.setText(QCoreApplication.translate("MainWindow", u"Fluxo Caixa", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Fatos Cont\u00e1beis", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Atividades", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Grupo Categorias", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Plano Contas", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Contas", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Cadastros", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/imagens/icone-pagamento.png\"/></p></body></html>", None))
    # retranslateUi


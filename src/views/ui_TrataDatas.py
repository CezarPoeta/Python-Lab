from qt_core import *


class Ui_TesteData(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)

        self.lblData = QLabel(self.centralwidget)
        self.lblData.setObjectName(u"lblData")
        self.gridLayout.addWidget(self.lblData, 0, 0, 1, 1)

        self.txtData = QDateEdit(self.centralwidget)
        self.txtData.setStyleSheet(u"background-color: rgb(255, 255, 0);")        
        self.txtData.setObjectName(u"txtData")
        self.txtData.setCalendarPopup(True)
        self.txtData.setDate(QDate(2023, 12, 1))

        self.gridLayout.addWidget(self.txtData, 0, 1, 1, 1)

        self.btnPrint = QPushButton(self.centralwidget)
        self.btnPrint.setObjectName(u"btnPrin")
        self.gridLayout.addWidget(self.btnPrint,0,0,1,1)

        self.btnRecupera = QPushButton(self.centralwidget)
        self.btnRecupera.setObjectName(u"btnRecupera")
        self.gridLayout.addWidget(self.btnRecupera,0,0,1,1)

        
        self.table = QTableWidget(3, 4)
        self.table.setStyleSheet('''
            QAbstractItemView::indicator {width: 15px; height: 15px;} 
            QTableWidget::Item {width: 500px; height: 40px; }'''
            )

       
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem4 = QTableWidgetItem()

        self.table.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        self.table.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        self.table.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        self.table.setHorizontalHeaderItem(3, __qtablewidgetitem4)




        self.gridLayout.addWidget(self.table)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

       # brush1 = QBrush(QColor(0, 0, 255, 255))
       # brush1.setStyle(Qt.NoBrush)
        font1 = QFont()
        font1.setFamilies([u"Arial Black"])
        font1.setBold(True)
        

        self.lblData.setText(QCoreApplication.translate("MainWindow", u"Date Edit-> Data:", None))
        self.btnPrint.setText(QCoreApplication.translate("Ok", u"btnOK", None))
        self.btnRecupera.setText(QCoreApplication.translate("Recupera", u"btnRecupera", None))

        ___qtablewidgetitem1 = self.table.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("JanelaPrincipal", u"Codigo", None));
        ___qtablewidgetitem1.setFont(font1)
        ___qtablewidgetitem1.setForeground(QBrush(QColor(255, 0, 0, 255)))
        ___qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)

        ___qtablewidgetitem2 = self.table.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("JanelaPrincipal", u"Descricao", None));
        ___qtablewidgetitem2.setFont(font1)
        ___qtablewidgetitem2.setForeground(QBrush(QColor(255, 0, 0, 255)))
        ___qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)

        ___qtablewidgetitem3 = self.table.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("JanelaPrincipal", u"Nome", None));
        ___qtablewidgetitem3.setFont(font1)
        ___qtablewidgetitem3.setForeground(QBrush(QColor(255, 0, 0, 255)))
        ___qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)

        ___qtablewidgetitem4 = self.table.horizontalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("JanelaPrincipal", u"Ultimo Nome", None));
        ___qtablewidgetitem4.setFont(font1)
        ___qtablewidgetitem4.setForeground(QBrush(QColor(255, 0, 0, 255)))
        ___qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter)


    # retranslateUi


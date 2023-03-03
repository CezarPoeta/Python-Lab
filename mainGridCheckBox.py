from qt_core import *
from ui_main import Ui_MainWindow
from src.views.ui_TrataDatas import Ui_TesteData
import sys

#CONTROLA MARCAR E DESMARCAR CHECKBOX PARA CADA LINHA DO GRID
class MainWindow(QMainWindow, Ui_TesteData):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Testes")

        #Captura evento a partir do click nos botoes
        self.btnPrint.clicked.connect(self.PrintNovaData_Click)
        self.btnRecupera.clicked.connect(self.recupera_marcados_Click)
        
        lista = [('Angela', 'Cezar', 'Sandra','Dagoberto'),('Raoni', 'Camila', 'Ju','Ledi'),('Lu', 'Cris', 'Priscila', 'Nei')]

        for row in range(len(lista)):
            for col in range(len(lista[row])):
                if col % (len(lista[row])) == 0:
                    item = QTableWidgetItem(lista[row][col])
                    item.setFlags(Qt.ItemFlag.ItemIsUserCheckable | Qt.ItemFlag.ItemIsEnabled)
                    item.setCheckState(Qt.CheckState.Unchecked)
                    self.table.setItem(row, col, item)
                else:
                    self.table.setItem(row, col, QTableWidgetItem(lista[row][col]))

    def recupera_marcados_Click(self):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0).checkState() == Qt.CheckState.Checked:
                print([self.table.item(row, col).text() for col in range(self.table.columnCount())])

    def PrintNovaData_Click(self):
        self.txtData.setDate(QDate(2023,1,16))
        print(self.txtData.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
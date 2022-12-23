'''
    Empresa      : Slice Treinamentos Ltda
    Objetivo     : Controle Mensagens Emitidas pelo Sistema 
    Desenvolvedor: Cezar Roberto Poeta 
    Data         : 24/08/2021
    Revisão Nr.  :
    Responsável  :   
'''

# Import Qt Core
from qt_core import *

class Msg_SysFinan():

    def __init__(self, mymsg, *args, **argvs):
        self.txtmsg = mymsg
        self.msg = QMessageBox()
       

    def msg_Critical(mymsg: str) -> bool:
        msg = QMessageBox()
        msg.setWindowTitle('Sistema Financeiro Pessoal!')
        msg.setText(mymsg)
        msg.setInformativeText('')
        msg.setIcon(QMessageBox.Critical)
        msg.exec_()
        return False

    def msg_Warning(mymsg: str) -> bool:
        msg = QMessageBox()
        msg.setText(mymsg)
        msg.setIcon(QMessageBox.Warning)
        msg.exec_()
        return True

    def msg_Question(mymsg: str) -> bool:
        msg = QMessageBox()
        msg.setText(mymsg)
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        resposta = msg.exec_()
        if resposta == QMessageBox.Yes:
            return True
        else:
            return False

    def msg_Information(self, mymsg: str) -> bool:
        msg = QMessageBox()
        msg.setText(mymsg)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)
        resposta = msg.exec_()
        return resposta
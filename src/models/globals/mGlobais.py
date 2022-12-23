'''
    Empresa      : Slice Treinamentos Ltda
    Objetivo     : Controla a Geração das Listas para Grids do Sistema 
    Desenvolvedor: Cezar Roberto Poeta 
    Data         : 23/09/2022
    Revisão Nr.  :
    Responsável  :   
'''

import datetime
from src.models.database.configs.connection import DBConnection as mDB
from src.models.globals.mCtrlMessages import Msg_SysFinan as mMsg
from pprint import pprint


#FUNÇÕES GERAIS DO SISTEMA
#---------- Bloquear Campos
def Bloquear(self, lObj):
    for objfield in lObj:

        if objfield.objectName() == 'btnConfirmar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:10px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnSair':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:10px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnAtualizar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnPagar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnTransferir':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnCadastrar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnEditar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnExcluir':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnClassificar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnFiltrar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnAbertura':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnReabertura':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'btnEncerramento':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'cboTpContas':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboContas':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboPeriodos':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboTipoConta':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboPlanoContas':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboEstConta':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboAnos':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboMeses':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboSitPeriodo':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboGrCategorias':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboCategorias':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboTpMovimento':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboBeneficiario':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboSitLanc':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        elif objfield.objectName() == 'cboContaOrigem':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QComboBox {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")

        else:
            objfield.setStyleSheet("QLineEdit {font-family:'Sanserif'; font:normal; font-size:15px; background-color: rgb(182, 182, 182); color: Blue}")
            objfield.setEnabled(False)


def Liberar(self, lObj):
    for objfield in lObj:
        if objfield.objectName() == 'btnConfirmar':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:10px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")
        
        elif objfield.objectName() == 'btnSair':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:10px; background-color: rgb(177, 180, 197); color: rgb(0, 0, 0)}")
    
        elif objfield.objectName() == 'btnAtualizar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnPagar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnTransferir':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnCadastrar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnEditar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnExcluir':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnClassificar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnFiltrar':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnAbertura':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnReabertura':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'btnEncerramento':
            objfield.setEnabled(False)
            objfield.setStyleSheet("QPushButton {font:bold; font-size:15px; background-color: rgb(182, 182, 182); color: grey}")

        elif objfield.objectName() == 'cboTpContas':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'cboContas':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'cboPeriodos':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")

        elif objfield.objectName() == 'cboEstConta':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboTipoConta':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboPlanoContas':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboAnos':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboMeses':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboSitPeriodo':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboGrCategorias':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboCategorias':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboTpMovimento':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboBeneficiario':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboContaOrigem':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        elif objfield.objectName() == 'cboSitLanc':
            objfield.setEnabled(True)
            objfield.setStyleSheet("QComboBox {font:bold; font-size:15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            
        else:
            objfield.setStyleSheet("QLineEdit {font:bold; font-size: 15px; background-color: #fff6c2; color: rgb(0, 0, 0)}")
            objfield.setEnabled(True)

def FormatarValor(valor: str) -> float:
    valor = f'R$ {float(valor):_.2f}'
    valor = valor.replace('.',',').replace('_','.')
    return valor

def DesFormatarValor(valor: str) -> float:
    valor = valor.replace('.','_').replace(',','.').replace('_','').replace('R$','')
    return valor

def BuscaPeriodoAtual(psData: str = None) -> str:
    if psData == None:
        #Não passado parametro pega data atual
        hoje = datetime.date.today()
    else:
        #Passado parâmetro pega data parametro
        hoje = datetime.date(int(psData[6:]), int(psData[3:5]), int(psData[:2]))

    #Pega Ano e Mes da data informada
    ano = hoje.year
    mes = hoje.month

    #Pesquisa ID do Ano pela variavel
    pSQL = f"SELECT id FROM tbAnos where nome = '{ano}';"
    Conn = mDB.ConnectDBSQLite()
    lo = mDB.ExecutaSQL(Conn, pSQL)
    for i in lo:
        anoID = i[0]
    Conn.close()

    #Pesquisa ID do Mes pela variavel
    pSQL = f"SELECT id FROM tbMeses where id = '{mes}';"
    Conn = mDB.ConnectDBSQLite()
    lo = mDB.ExecutaSQL(Conn, pSQL)
    for i in lo:
        mesID = i[0]
    Conn.close()

    #Pesquisa ID do Periodo pelos IDs das variaveis
    periodoID = 0
    pSQL = f"SELECT nome FROM tbPeriodos where tbPeriodos.AnoID = '{int(anoID)}' AND tbPeriodos.MesID = '{int(mesID)}';"
    try:
        Conn = mDB.ConnectDBSQLite()
        lo = mDB.ExecutaSQL(Conn, pSQL)
        for i in lo:
            periodoID = i[0]
        Conn.close()
        gPeriodoReferencia = periodoID
    except Exception as Erro:
        myMsg = f'Tabela Periodos sem Dados Informados! {Erro}'
        mMsg.msg_Critical(myMsg)

    return gPeriodoReferencia


def converteData(pdDate):
    dt = pdDate.split('/')
    return datetime.datetime(
        int(dt[2]),
        int(dt[1]),
        int(dt[0]),
    )

def ordenar_DtVenc(value):
    return(converteData(value[3]))

def ordenar_DtFato(value):
    return(converteData(value[2]))

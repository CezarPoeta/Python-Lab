import pandas as pd
import PersonalBudget.Modulos.mDataBase as mDB
import datetime

'''
index - 01 -TBPERIODOS
index - 02 -TBPLANOCONTAS
index - 03 -TBCONTAS
index - 04 -TBCONTAPERIODOS
index - 05 -TBBENEFICIARIOS
index - 06 -TBCATEGORIAS
index - 07 -TBFATOSCONTABEIS

'''

def Importar_TBBENEFICIARIOS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBBENEFICIARIOS') 
    max = df['ID'].count()
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):
        id = df['ID'][i]
        nome = df['Nome'][i]
        pSQL = f"INSERT INTO tbBeneficiarios (nome, CreatedAt, UpDatedAt) VALUES('{nome}','{dt}','{dt}')"
        mDB.ExecutaSQL(con, pSQL)
        con.commit()
    con.close()

def Importar_TBPLANOCONTAS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBPLANOCONTAS') 
    max = df['ID'].count()
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):
        id = df['ID'][i]
        my_CdConta = df['CdConta'][i]
        my_Nome = df['Nome'][i]
        my_TpConta = df['TBTPCONTA.Nome'][i]
        my_EstConta = df['TBESTCONTA.Nome'][i]
        pSql = f"INSERT INTO tbPlanoContas (CdConta, nome, TpContaID, EstContaID, CreatedAt, UpDatedAt) VALUES ('{my_CdConta}', '{my_Nome}', (SELECT id from tbTpConta WHERE nome = '{my_TpConta}'), (SELECT id from tbEstConta WHERE nome = '{my_EstConta}'), '{dt}', '{dt}')"
        mDB.ExecutaSQL(con, pSql)
        con.commit()
    con.close()


def Importar_TBCONTAS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBCONTAS') 
    max = df['ID'].count()
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):
        id = df['ID'][i]
        my_Nome = df['Nome'][i]
        my_TipoConta = df['TBTIPOCONTA.Nome'][i]
        my_PlanoContas = df['TBPLANOCONTAS.Nome'][i]

        pSql = f"INSERT INTO tbContas (nome, TipoContaID, PlanoContasID, CreatedAt, UpDatedAt) VALUES ('{my_Nome}', (SELECT id from tbTipoConta WHERE nome = '{my_TipoConta}'), (SELECT id from tbPlanoContas WHERE nome = '{my_PlanoContas}'), '{dt}', '{dt}')" 
        mDB.ExecutaSQL(con, pSql)
        con.commit()
    con.close()


def Importar_TBPERIODOS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBPERIODOS') 
    max = df['ID'].count()
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):
        id = df['ID'][i]
        my_N = df['Nome'][i]
        my_NomeAno = df['TBANOS.Nome'][i]
        my_NomeMes = df['TBMESES.Nome'][i]
        my_NomeSitPer = df['TBSITPERIODO.Nome'][i]

        my_Nome = f'{my_NomeMes}/{my_NomeAno}'
        pSql = f"INSERT INTO tbPeriodos (nome, AnoID, MesID, SitPeriodoID, CreatedAt, UpDatedAt) VALUES ('{my_Nome}', (SELECT id FROM tbAnos WHERE nome = '{my_NomeAno}'), (SELECT id FROM tbMeses WHERE nome = '{my_NomeMes}'), (SELECT id FROM tbSitPeriodo WHERE nome = '{my_NomeSitPer}'), '{dt}', '{dt}')" 
        mDB.ExecutaSQL(con, pSql)
        con.commit()
    con.close()
    

def Importar_TBCONTAPERIODOS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBCONTAPERIODOS')

    max = df['ID'].count()
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):
        id = df['ID'][i]
        my_NP = df['TBPERIODO.Nome'][i]
        my_NomeConta = df['TBCONTAS.Nome'][i]
        my_VlSldInicial = df['VlSldInicial'][i]
        my_VlSldFinal = df['VlSldFinal'][i]
        meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        my_NomePeriodo = meses[my_NP.month - 1] + '/' + str(my_NP.year)
        print(my_NomePeriodo)
        pSql = f"INSERT INTO tbContaPeriodos (ContaID, PeriodoID, vlSldInicial, vlSldFinal, CreatedAt, UpDatedAt) VALUES ((SELECT id FROM tbContas WHERE nome = '{my_NomeConta}'), (SELECT id FROM tbPeriodos WHERE nome = '{my_NomePeriodo}'), {my_VlSldInicial}, {my_VlSldFinal}, '{dt}', '{dt}')" 
        mDB.ExecutaSQL(con, pSql)
        con.commit()
    con.close()


def Importar_TBCATEGORIAS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBCATEGORIAS') 
    max = df['ID'].count()
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):
        my_id = df['ID'][i] 
        my_nome = df['Nome'][i] 
        my_nomeBeneficiarios = df['TBBENEFICIARIOS.Nome'][i] 
        my_vlMedia = df['VlMedia'][i] 
        my_vlModa = df['VlModa'][i] 
        my_vlMediana = df['VlMediana'][i] 
        my_diaVenc = df['DiaVenc'][i] 
        my_nomeContas = df['TBCONTAS.Nome'][i] 
        my_nomeSitLanc = df['TBSITLANC.Nome'][i] 
        my_nomeGrCat = df['TBGRCATEGORIAS.Nome'][i] 
        my_MovCon = df['TBTPMOVIMENTO.MovCon'][i]

        pSql = f"INSERT INTO tbCategorias (nome, BeneficiarioID, vlMedia, vlModa, vlMediana, diaVenc, ContaID, SitLancID, GrCategoriasID, TpMovimentoID, CreatedAt, UpDatedAt) VALUES ('{my_nome}', (SELECT id FROM tbBeneficiarios WHERE nome = '{my_nomeBeneficiarios}'), '{my_vlMedia}', '{my_vlModa}', '{my_vlMediana}', '{my_diaVenc}', (SELECT id FROM tbContas WHERE nome = '{my_nomeContas}'), (SELECT id FROM tbSitLanc WHERE nome = '{my_nomeSitLanc}'), (SELECT id FROM tbGrCategorias WHERE nome = '{my_nomeGrCat}'), (SELECT id FROM tbTpMovimento WHERE movcon = '{my_MovCon}'), '{dt}', '{dt}')"
        mDB.ExecutaSQL(con, pSql)
        con.commit()
    con.close()



def Importar_TBFATOSCONTABEIS():
    df = pd.read_excel(r'\\tsclient\C\Users\cezar\OneDrive\Documentos\Cadernos\3-Pessoal\00-SisAdm\T5-Fechamento-ExportaçãoDados.xlsx', sheet_name='TBFATOSCONTABEIS') 
    max = df['ID'].count()
    
    dt = datetime.datetime.now() 
    con = mDB.ConnectDBSQLite()

    for i in range(0, max):

        my_id = df['ID'][i] 
        my_NP = df['TBPERIODO.Nome'][i]
        my_NomeConta = df['TBCONTAS.Nome'][i]
        my_NomeBeneficiario = df['TBBENEFICIARIOS.Nome'][i] 
        my_NomeCategoria = df['TBCATEGORIAS.Nome'][i] 
        my_DtF = df['DtFato'][i]
        my_DtV = df['DtVenc'][i]
        my_vlFato = df['VlFato'][i]
        my_Historico = df['Historico'][i]
        my_NomeSitLanc = df['TBSITLANC.Nome'][i]

        #Corrige Data Fato
        mydia = str(my_DtF.day)
        if int(mydia) < 10:
            mydia = '0' + mydia

        mymes = str(my_DtF.month)
        if int(mymes) < 10:
            mymes = '0' + mymes

        myano = str(my_DtF.year)
        my_DtFato = myano + '-' + mymes + '-' + mydia

        #Corrige Data Vencimento
        mydia = str(my_DtV.day)
        if int(mydia) < 10:
            mydia = '0' + mydia

        mymes = str(my_DtV.month)
        if int(mymes) < 10:
            mymes = '0' + mymes

        myano = str(my_DtV.year)
        my_DtVenc = myano + '-' + mymes + '-' + mydia

       # my_NomePeriodo = my_NP.month_name() + '/' + str(my_NP.year)
        meses = ['Janeiro', 'Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
        my_NomePeriodo = meses[my_NP.month - 1] + '/' + str(my_NP.year)
        print(my_NomePeriodo)

        pSql = f"""
            INSERT INTO tbFatosContabeis 
                (PeriodoID, 
                 ContaID, 
                 BeneficiarioID, 
                 CategoriaID, 
                 DtFato, 
                 DtVenc, 
                 vlFato, 
                 Historico, 
                 SitLancID, 
                 CreatedAt, 
                 UpDatedAt)
            VALUES (
                (SELECT id FROM tbPeriodos WHERE nome = '{my_NomePeriodo}'), 
                (SELECT id FROM tbContas WHERE nome = '{my_NomeConta}'), 
                (SELECT id FROM tbBeneficiarios WHERE nome = '{my_NomeBeneficiario}'), 
                (SELECT id FROM tbCategorias WHERE nome = '{my_NomeCategoria}'), 
                '{my_DtFato}', 
                '{my_DtVenc}', 
                '{my_vlFato}', 
                '{my_Historico}', 
                (SELECT id FROM tbSitLanc WHERE nome = '{my_NomeSitLanc}'), 
                '{dt}', 
                '{dt}')
        """
        mDB.ExecutaSQL(con, pSql)
        con.commit()
        
    con.close()
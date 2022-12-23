
import Modulos.mImportaExcel as mI        
print('Início do Processo Períodos')
mI.Importar_TBPERIODOS()
print('Final do Processo Períodos')

print('Início do Processo Plano de Contas')
mI.Importar_TBPLANOCONTAS()
print('Final do Processo Plano de Contas')

print('Início do Processo Contas')
mI.Importar_TBCONTAS()
print('Final do Processo Contas')

print('Início do Processo Conta x Períodos')
mI.Importar_TBCONTAPERIODOS()
print('Final do Processo Conta x Períodos')

print('Início do Processo Beneficiários')
mI.Importar_TBBENEFICIARIOS()
print('Final do Processo Beneficiários')

print('Início do Processo Categorias')
mI.Importar_TBCATEGORIAS()
print('Final do Processo Categorias')

print('Início do Processo Fatos Contábeis')
mI.Importar_TBFATOSCONTABEIS()
print('Final do Processo Fatos Contábeis')


from src.control.clasSm import Soma
from src.control.clasSt import Subtracao

class Resultado(Soma, Subtracao):
        soma = Soma(7,9)
#        n1 = Soma.som(6.0,Subtracao.sub(87,54))
        print(soma.som())
#        print(n1)



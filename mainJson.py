import json

""" carros_json = {
    "marca":"honda", 
    "modelo":"HRV", 
    "cor":"preto",
    "Ano":"2017"}

#GRAVACAO ARQUIVO carros_json 
with open('carros_json', 'w') as arquivo_json:
    json.dump(carros_json, arquivo_json)

#LEITURA ARQUIVO carros_json
with open('carros_json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

#DIFERENTES FORMAS DE APRESENTACAO DOS DADOS
for dado in dados:
    print(f'Dados: {dado}')

for dado in dados.values():
    print(f'Valores: {dado}')

for dado in dados.items():
    print(f'Itens: {dado}')

for chave, dado in dados.items():
    print(f'Chave e Dado: {chave}-{dado}')

for chave, dado in dados.items():
    if chave == 'Ano':
        print(f'Ano-Dado: {chave}-{dado}') """

####ABERTURA ARQUIVO CONFIG
with open('config.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)

###APRESENTACAO DOS PARAMETROS
""" for chave, dado in dados.items():
    if chave == 'configurations':
        print(f'Configuracao chave, dado: {chave}-{dado}')

for dado in dados.items():
    if chave == 'configurations':
        print(f'Configuracao dado: {dado[1][0]}')
 """
for chave, dado in dados.items():
    if chave == 'configurations':
        for d in dado:
            myName = d["name"]
            myType = d["type"]
            print(f'Nome: {myName}')
            print(f'Tipo: {myType}')
            print(f'Requisicao: {d["request"]}')
            print(f'Programa: {d["program"]}')
            print(f'Console: {d["console"]}')
            print(f'Meu Codigo: {d["justMyCode"]}')

#Dicionário vazio 
D = {}

D = dict()

#Dicionário com itens
D = {'nome': 'João', 'idade': '25'}

D = dict(nome='João', idade='25')

#criando dicionários por pares de chave/valor
D = dict([('nome', 'idade'), ('joão','25')])

print(D)

#indexação de dicionários
#elementos de um dicionário deve ser acessados através de sua chave

D = {'nome': 'João', 'idade': '25'}

#acessando o valor disponível em nome
print(D['nome'])
print(D['idade'])

#tamanho do dicionário
print(len(D))

#assiciação em dicionários
print('nome' in D)

#alteração de dicionário

#adicionar elementos
D['sexo'] = 'masculino'
print(D)

#editar elemento
D['idade'] = 30
print(D)

#apagar um elemento
del D['idade']
print(D)

#alteração de dicionários usando métodos
D = {'nome': 'João', 'idade': '25'}

D.pop('idade')
print(D)

#métodos de dicionários
D = {'nome': 'João', 'idade': '25'}

#Ciar uma lista com as chaves
print(list(D.keys()))

#cirar lista com os valores
print(list(D.values()))

#criar lista com os pares valor/chave
print(list(D.items()))

#retorne None,caso a chave não exista
D = {'nome': 'João', 'idade': '25'}
#print(D['sexo'])
print(D.get('sexo'))

#interação em dicionários
D = {'nome': 'João', 'idade': '25'}

for i in D.keys():
    print(i)
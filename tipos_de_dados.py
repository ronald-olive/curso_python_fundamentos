
'''
    Os tipos de dados mais básicos em Python são: 
    Sequências: Strings(str), listas(list), tuplas(tuple)
    Mapeamentos: Dicionários(dict)
    Conjuntos: Set(), conjuntos imutáveis(frozenset)
    Booleano: Verdadeiro ou Falso(bool)
    None: Representa a ausência de valor(NoneType)
    Numéricos: 3, 1, -1 10000 1.0 
 '''

# # Sequência de strings
nome = 'Curso de Python'
instrutor = 'Guilherme'
print(nome + ' com ' + instrutor )

# # Sequência: listas(Representa uma sequência de valores)
pessoas = ['Amanda', 'Ronaldo', 'Kátia', 'Rose']
print(pessoas)

# Mapeamentos: Dicionários
elemento = {
   'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
 }

print(f'Elemento:  {elemento['nome']}' )
print(f'Densidade:  {elemento['densidade']}' )
print(f'O dicionario possui {len(elemento)} elementos')

#Conjuntos: Set(), conjuntos imutáveis(frozenset)
planeta_anao = {'Plutão', 'Ceres', 'Eris', 'Haumea', 'Makemake'}
print(len(planeta_anao))
print('Ceres' in planeta_anao)
print('Lua' in planeta_anao)
print('Lua' not in planeta_anao)

#Booleano: Verdadeiro ou Falso(bool)
x = 10
y = 15
print(x == y)




  

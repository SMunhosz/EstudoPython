
from statistics import variance


nomes =  ['Guilherme', 'Mário', 'Nina', 'Junior']
"""
for valor in nomes:
    if valor.startswith('J'):
        print('Começa com J', valor)
    else:
        print('Não começa com J', valor)
"""

comecaJ = False
for valor in nomes:
    if valor.lower().startswith('j'):
        comecaJ = True

if comecaJ :
    print('Existe uma Palavra que Começa com J')
else:
    print('Não existe palabra que começa com J')
"""
for in em Python
Iterando strings com for
Função range(start=0, stop, step=1)
"""

"""
texto = 'Python'
c = 0
while c < len(texto): # ISSO USANDO WHILE, SERIA USANDO FOR IN :::
    print(texto[c])
    c += 1
"""

texto = 'Guilherme'
for letra in texto:
    print(letra)

print()

for numero in range(5, 10, 2):
    print(numero)
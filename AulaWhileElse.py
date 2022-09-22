# O VALOR QUE CONTEM NA VARIAVEL CONTADOR NO WHILE, SERVE PARA QUE O LAÇO TENHA UM FIM

contador = 1
acumulador = 1

while contador <= 10:
    print(contador, acumulador)

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('Fim! ')
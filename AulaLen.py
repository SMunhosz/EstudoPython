usuario = input('Informe seu usuário: ')
qtd = len(usuario)


if qtd >= 9:
    print('O nome de usuário:', usuario, 'Contém:', qtd, 'De Letras')
    print('Nome Válido')
else:
    print('O usuário:', usuario, 'Tem Apenas:', qtd, 'Letras')
    print('Nome Inválido')

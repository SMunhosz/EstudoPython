
numero_inteiro = input('Digite um número inteiro')

if numero_inteiro.isdigit():
    numero_inteiro = int(numero_inteiro)

    if numero_inteiro % 2 == 0:
        print(numero_inteiro, 'é PAR')
    else:
        print(numero_inteiro, 'é Impar')

else:
    print('ISSO NÃO É UM NÚMERO INTEIRO')

# -------------------------------------------

horario = input('Digite um horário (0 a 23): ')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve estar de acordo com os números estipulados na descrição do sistema.')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa Tarde!')
        else:
            print('Boa Noite!')
else:
    print('Digite um horário válido, por favor. (0 a 23)')
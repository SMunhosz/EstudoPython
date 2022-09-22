num1 = input('Digite um número')
num2 = input('Digite um número')

# isnumeric, isdigit, isdecimal
# números e positivos
# print(num1.isnumeric())
# print(num2.isnumeric())

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print('Não consegui converter o(s) número(s)')



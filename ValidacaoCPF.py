# Estrutura de Validação
cpf = '53962947876'
num1 = 0
num2 = 0
numCheck = 0
numCheck2 = 0
i = 1

# Verificar numero de caracteres
if len(cpf) < 11:
    difcpf = 11 - len(cpf)
    cpf = '0' * difcpf + cpf

# Capturar o número do digito verificador
numCheck = int(cpf[9:10]) # Captura o penultimo digito verficador
numCheck2 = int(cpf[10:11]) # Caputra o ultimo digito verificador

# Calculo do Primeito Digito Verificador
for i in range(1,10):
    num1 = num1 + int(cpf[i - 1:i]) * i

# Resto da Divisão por 11
num1 = num1 % 11
print(num1)

# Se o número for maior que 10, considerar 0
if (num1 == 10):
    num1 = 0

# Verificar o Primeiro Digito
if num1 != numCheck:
    print('Dígito i inválido')

# Digito Verificador 2
for i in range(2, 11):
    num2 = num2 + int(cpf[i - 1:i]) * (i - 1)

num2 + num2 % 11

if (num2 == 10):
    num2 = 0

if num2 != numCheck2:
    print('Digito 2 Inválido')

if (num1 == numCheck and num2 == numCheck2):
    print('CPF VÁLIDO !')

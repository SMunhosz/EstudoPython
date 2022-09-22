import requests

cep = input('Informe o CEP: ')
r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

data = r.json()

print('CEP: {}'.format(data['cep']))
print('Logradouro: {}'.format(data['logradouro']))
print('Bairro: {}'.format(data['bairro']))
print('Localidade: {}'.format(data['localidade']))




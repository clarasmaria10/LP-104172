import os
from datetime import date
os.system('cls')

# INICIO
print('= DADOS =')
nome = input('Digite seu nome completo: ')
sexo = input('Digite seu sexo [M/F]: ').strip().upper()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, digite seu sexo [M/F]: ').strip().upper()[0]
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
os.system('cls')

# PROCESSAMENTO

print('= EXIBINDO DADOS =')
print('Nome: ', nome)
print('Sexo: ', sexo)
print('Ano de nascimento: ', nascimento)
print('Idade: ', idade)

if idade < 18 or sexo == 'F':
    print('Você não pode se alistar.')
elif idade == 18 and sexo =='M':
    print('Você tem que se alistar.')
elif idade > 18 and sexo == 'M':
    print('Você já deveria ter se alistado.')
else:
    print('Você não pode se alistar.')
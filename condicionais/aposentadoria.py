import os
from datetime import date
os.system('cls || clear')

print('= SOLICITANDO DADOS =')
matricula = int(input('Digite sua matrícula: '))
nascimento = int(input('Digite seu ano de nascimento: '))
temposerv = int(input('Digite seu tempo de serviço: '))
idade = date.today().year - nascimento

os.system('cls || clear')

print('= EXIBINDO DADOS =')
print(f'Matrícula: {matricula}')
print(f'Ano de nascimento: {nascimento}')
print(f'Tempo de serviço: {temposerv} anos')

if idade >= 65 or temposerv >= 30:
    resultado = 'Requerer aposentadoria.'
else:
    resultado = 'Não requerer aposentadoria.'

print(f'Resultado: {resultado}')
print(f'Data: {date.today()}')
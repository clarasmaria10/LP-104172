import os
os.system('cls || clear')

dia = int(input('Digite um número para o dia (1 a 7): '))
while dia > 7:
    dia =int(input('Número inválido. Digite um número para o dia(1 a 7): '))

match dia:
    case 1 | 7:
        print('Final de semana')
    case 2 | 3 | 4 | 5 | 6:
        print('Dia útil')
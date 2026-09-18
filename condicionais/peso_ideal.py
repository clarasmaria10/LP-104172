import os
os.system('cls || clear')

altura = float(input('Qual sua altura? (Em metros): '))
sexo = input('Qual seu sexo? [M/F] ').upper()
os.system('cls || clear')

match sexo:
    case 'M':
        peso_ideal_M = (72.7 * altura) - 58
        print(f'Seu peso ideal é {peso_ideal_M:.2f}')
    case 'F':
        peso_ideal_F = (62.1 * altura) - 44.7
        print(f'Seu peso ideal é {peso_ideal_F:.2f}')
    case _:
        print('Inválido.')
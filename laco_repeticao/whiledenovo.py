import os
os.system('cls || clear')

while True:
    nota = float(input('Digite uma nota entre 0 e 10: '))
    if nota < 0 or nota > 10:
        print('\nNota inválida! Digite novamente. ')
    else:
        print()
        print(f'Sua nota é {nota}.')
        break

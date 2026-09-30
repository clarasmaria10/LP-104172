import os
os.system('cls || clear')

while True:
    numero = int(input('Digite um numero entre 1 e 10: '))
    if numero < 1 or numero > 10:
        print('\nNúmero inválido! Tente novamente.')
    else:
        print()
        print('O número está entre 1 e 10.')
        break # Serve para parar o laço de repetição quando a condição for satisfeita.

print('== FIM DO PROGRAMA ==')

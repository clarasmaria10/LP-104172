import os
os.system('cls || clear')

soma = 0

for i in range(5):
    numero = int(input('Digite um número: '))
    soma = numero + soma

print(f'Soma: {soma}')
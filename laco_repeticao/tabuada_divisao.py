import os
os.system('cls || clear')

print('= TABUADA =')
numero = int(input('Digite um número: '))

for i in range(1, 11):
    print(f'{numero} / {i} = {numero / i}')
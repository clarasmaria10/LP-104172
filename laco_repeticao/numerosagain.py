import os
os.system('cls || clear')

# CONSTANTE
pares = 0
impares = 0
QUANTIDADE_REPETICOES = 6

for i in range(QUANTIDADE_REPETICOES):
    numero = int(input('Digite um número: '))
    if numero % 2 == 0:
        pares += pares + 1
    else:
        impares += impares + 1

print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números impares: {impares}')

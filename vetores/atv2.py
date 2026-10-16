import os
os.system('cls || clear')

vetor_numeros = []
QUANTIDADE_NUMEROS = 5

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'Digite o {i + 1}º número: '))
    vetor_numeros.append(numero)

for i in range(QUANTIDADE_NUMEROS):
    if vetor_numeros[i] < 0:
        vetor_numeros[i] = 0
    else:
        vetor_numeros[i] = vetor_numeros[i]

print(f'Valores do vetor: {vetor_numeros}')

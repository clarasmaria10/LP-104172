import os
os.system('cls || clear')

vetor_numeros = []
QUANTIDADE_NUMEROS = 5
negativos = 0
soma_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'Digite o {i + 1}º número: '))
    vetor_numeros.append(numero)

for numero in vetor_numeros:
    if numero < 0:
        negativos += 1
    else:
        soma_positivos += numero

print(f'Quantidade de números negativos: {negativos}')
print(f'Soma dos números positivos: {soma_positivos}')
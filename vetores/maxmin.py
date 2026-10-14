import os
os.system('cls || clear')

vetor_numero = []
QUANTIDADE_NUMEROS = 5

print('== NUMEROS ==')
for i in range(QUANTIDADE_NUMEROS):
    numero = float(input(f'Digite o {i + 1}° número: '))
    vetor_numero.append(numero)
os.system('cls || clear')

maior = max(vetor_numero)
menor = min(vetor_numero)

print('== RESULTADOS ==')
print(f'Maior número: {maior}')
print(f'Menor número: {menor}')
print(f'Números digitados: {vetor_numero}')
import os
os.system('cls || clear')

QUANTIDADE_NOTAS = 3
vetor_notas = []

for i in range(QUANTIDADE_NOTAS):
    nota = float(input('Digite sua nota: '))
    vetor_notas.append(nota) # inserir a nota dentro do vetor "notas"

media = sum(vetor_notas) / QUANTIDADE_NOTAS

for i in range(QUANTIDADE_NOTAS):
    print(f'Nota: {vetor_notas[i]}')

print(f'Média: {media}')
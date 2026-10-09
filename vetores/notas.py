import os
os.system('cls || clear')

vetor_notas = []

for i in range(3):
    nota = float(input('Digite sua nota: '))
    vetor_notas.append(nota) # inserir a nota dentro do vetor "notas"

media = sum(vetor_notas) / 3

for i in range(3):
    print(f'Nota: {vetor_notas[i]}')

print(f'Média: {media}')
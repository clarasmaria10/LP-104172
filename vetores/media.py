import os
os.system('cls || clear')

QUANTIDADE_NOTAS = 4
vetor_notas = []

print('== CONFERINDO NOTAS ==')
for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f'Digite sua {i + 1}° nota: '))
    vetor_notas.append(nota)
os.system('cls || clear')

media = sum(vetor_notas) / QUANTIDADE_NOTAS

print('== RESULTADOS ==')
for i in range(QUANTIDADE_NOTAS):
    print(f'{i + 1}° nota: {vetor_notas[i]}')
    print(f'Média: {media}')
if media < 5:
    print('Aluno reprovado.')
elif 5 <= media < 7:
    print('Aluno em recuperação.')
else:
    print('Aluno aprovado.')
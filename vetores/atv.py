import os
os.system('cls || clear')

vetor_livros = []
QUANTIDADE_LIVROS = 5

print('== INSIRA 5 LIVROS ==')
for i in range(QUANTIDADE_LIVROS):
    livros = input(f'Escreva o {i + 1}° livro: ')
    vetor_livros.append(livros)
    os.system('cls || clear')

print('== MOSTRANDO OS 5 LIVROS DIGITADOS')
for i in range(QUANTIDADE_LIVROS):
    print(f'{i + 1}° livro: {vetor_livros[i]}')
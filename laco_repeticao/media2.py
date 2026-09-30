import os

os.system('cls')

soma = 0

while True:
    for i in range(2):
        nota = float(input('Digite a nota do aluno: '))
        if nota >= 0 and nota <= 10:
            soma += nota,
        else:
            print('Nota inválida! Digite um valor entre 0 e 10.')
            break
    media = soma / 2
    print(f'Sua media é {media}')
    print('\n== FIM DO PROGRAMA ==')
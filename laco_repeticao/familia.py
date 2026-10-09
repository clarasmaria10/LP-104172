import os
os.system('cls || clear')

familia = salariomax = salariomin = salariototal = filhostotal = 0

while True:
    menu = (input('Digite o número correspondente ao menu:\n1 | Adicionar família\n2 | Sair e Exibir resultados \n'))
    match menu:
        case '1':
            salario = float(input('Digite o salário da família: R$ '))
            filhos = int(input('Digite quantos filhos(as) a família tem: '))
            familia = familia + 1
            salariototal += salario
            filhostotal += filhos
            if familia == 1:
                salariomax = salario
                salariomin = salario
            else:
                salariomax = max(salariomax, salario)
                salariomin = min(salariomin, salario)
                os.system('cls')
        case '2':
            media_salario = salariototal / familia
            media_filhos = filhostotal / familia
            print(f'Total de famílias: {familia}')
            print(f'Média salarial da população: {media_salario}')
            print(f'Média de filhos da população: {media_filhos}')
            print(f'Maior salário: {salariomax}')
            print(f'Menor salário: {salariomin}')
            break
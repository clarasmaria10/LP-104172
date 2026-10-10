import os
os.system('cls' if os.name == 'nt' else 'clear')

alunos = []

while True:
    print('\n== MENU ==\n 1 | Cadastrar nota do aluno\n 2 | Sair e exibir resultados')
    op = int(input('\nDigite a opção desejada: '))

    match op:
        case 1:
            nome = input("Digite o nome do aluno: ")
            nota = float(input("Digite a nota do aluno: "))
            alunos.append({'nome': nome, 'nota': nota})

            print(f'Nota cadastrada para {nome}: {nota}')
            input('Pressione Enter para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')

        case 2:
            break
        
        case _:
            print('Opção inválida! Tente novamente.')
            input('Pressione Enter para continuar...')
            os.system('cls' if os.name == 'nt' else 'clear')

alunos_aprovados = [aluno['nome'] for aluno in alunos if aluno['nota'] >= 6]

if len(alunos) > 0:
    media_turma = sum(aluno['nota'] for aluno in alunos) / len(alunos)
    notas_texto = ", ".join([str(aluno['nota']) for aluno in alunos])
    aprovados_texto = ", ".join(alunos_aprovados) if alunos_aprovados else "Nenhum"

    print('\n== RESULTADOS ==')
    print(f'\nMédia da turma: {media_turma}')
    print(f'Notas cadastradas: {notas_texto}')
    print(f'Alunos aprovados: {aprovados_texto}')

else:
    print('Nenhuma nota foi cadastrada.')
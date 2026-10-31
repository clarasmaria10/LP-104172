import os
os.system('cls || clear')

jogadores = []


def solicitar_valido(rotulo):
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print('Erro: O campo não pode ficar em branco. Tente novamente.')

def solicitar_valido_atualizar(rotulo, valor_atual):
    while True:
        valor = input(rotulo).strip()
        if not valor:
            return valor_atual
        return valor


def solicitar_camisa_valida(rotulo, camisa_atual=None):
    while True:
        entrada = input(rotulo).strip()

        if '.' in entrada or ',' in entrada:
            print(
                'Erro: Digite apenas números inteiros (sem casas decimais).'
            )
            continue

        try:
            valor = int(entrada)
            if valor <= 0:
                print('Erro: Digite um número maior que zero.')
                continue

            if valor != camisa_atual and any(
                j['camisa'] == valor for j in jogadores
            ):
                print(
                    f'Erro: A camisa número {valor} já está em uso por outro jogador. Escolha outro número.'
                )
                continue

            return valor

        except ValueError:
            print(
                'Erro: Entrada inválida. Digite apenas números inteiros válidos.'
            )


def cadastrar_jogador():
    print('\n-- Cadastrar jogador --')
    nome = solicitar_valido('Nome: ')
    sobrenome = solicitar_valido('Sobrenome: ')
    posicao = solicitar_valido('Posição: ')
    camisa = solicitar_camisa_valida('Número da camisa: ')

    jogadores.append({
        'nome': nome,
        'sobrenome': sobrenome,
        'posicao': posicao,
        'camisa': camisa,
    })
    print('Jogador cadastrado.')


def listar_jogadores():
    print('\n--- Lista de Jogadores ---')
    if not jogadores:
        print('Nenhum jogador cadastrado.')
        return

    for index, jogador in enumerate(jogadores, start=1):
        print(
            f"{index}. {jogador['nome']} {jogador['sobrenome']} - {jogador['posicao']} (Camisa {jogador['camisa']})"
        )


def atualizar_jogador():
    print('\n--- Atualizar Jogador ---')
    if not jogadores:
        print('Nenhum jogador cadastrado.')
        return

    listar_jogadores()
    try:
        numero = int(
            input('\nDigite o número do jogador que deseja atualizar: ')
        )
        if 1 <= numero <= len(jogadores):
            jogador = jogadores[numero - 1]
            print(
                f"\nAtualizando jogador: {jogador['nome']} {jogador['sobrenome']}"
            )

            nome = solicitar_valido('Novo nome (deixe em branco para manter): ')
            sobrenome = solicitar_valido(
                'Novo sobrenome (deixe em branco para manter): '
            )
            posicao = solicitar_valido(
                'Nova posição (deixe em branco para manter): '
            )
            camisa = solicitar_camisa_valida(
                'Novo número da camisa (deixe em branco para manter): ',
                camisa_atual=jogador['camisa'],
            )

            if nome:
                jogador['nome'] = nome
            if sobrenome:
                jogador['sobrenome'] = sobrenome
            if posicao:
                jogador['posicao'] = posicao
            if camisa:
                jogador['camisa'] = camisa

            print('Jogador atualizado com sucesso!')
        else:
            print('Erro: Número do jogador inexistente.')
    except ValueError:
        print('Erro: Por favor, insira um número válido.')

def excluir_jogador():
    print('\n--- Excluir Jogador ---')
    if not jogadores:
        print('Nenhum jogador cadastrado.')
        return

    listar_jogadores()
    try:
        numero = int(
            input('\nDigite o número do jogador que deseja excluir: ')
        )
        if 1 <= numero <= len(jogadores):
            jogador_removido = jogadores.pop(numero - 1)
            nome_completo = (
                f"{jogador_removido['nome']} {jogador_removido['sobrenome']}"
            )
            print(f"Jogador '{nome_completo}' removido com sucesso!")
        else:
            print('Erro: Número do jogador inexistente.')
    except ValueError:
        print('Erro: Por favor, insira um número válido.')


def menu():
    while True:
        print('\n== TIME ==')
        print('1. Cadastrar jogador')
        print('2. Listar jogadores')
        print('3. Atualizar jogador(es)')
        print('4. Excluir jogador(es)')
        print('0. Sair')

        try:
            opcao = input('\nOpção: ').strip()
        except KeyboardInterrupt:
            print('\n\nEncerrando o programa...')
            break

        match opcao:
            case '1':
                cadastrar_jogador()
            case '2':
                listar_jogadores()
            case '3':
                atualizar_jogador()
            case '4':
                excluir_jogador()
            case '0':
                print('Encerrando o programa... Até logo!')
                break
            case _:
                print('Opção inválida! Tente novamente.')


if __name__ == '__main__':
    menu()
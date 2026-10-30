import os
os.system('cls || clear')

jogadores = []

def solicitar_nome_valido(rotulo):
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print('Erro: O campo não pode ficar em branco. Tente novamente. ')

def solicitar_posicao_valida(rotulo):
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print('Erro: O campo não pode fiacar em branco. Tente novamente. ')

def solicitar_camisa_valida(rotulo):
    while True:
        entrada = input(rotulo).strip()

        if "." in entrada or "," in entrada:
            print("Erro: Digite apenas números inteiros (sem casas decimais).")
            continue

        try:
            valor = int(entrada)
            if valor > 0:
                return valor
            print("Erro: Digite um número maior que zero.")
        except ValueError:
            print("Erro: Entrada inválida. Digite apenas números inteiros válidos.")

def cadastrar_jogador():
    print('\n-- Cadastrar jogador --')
    nome = solicitar_nome_valido('Nome: ')
    sobrenome = solicitar_nome_valido('Sobrenome: ')
    posicao = solicitar_posicao_valida('Posição: ')
    camisa = solicitar_camisa_valida('Número da camisa: ')

    jogadores.append({"nome": nome, "sobrenome": sobrenome,'posição': posicao, "camisa": camisa})
    print('Jogador cadastrado.')

def listar_jogador():
    print("\n--- Lista de Jogadores ---")
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return

    for index, jogadores in enumerate(jogadores, start=1):
        print(f"{index}. {jogadores['nome']} {jogadores['sobrenome']} {jogadores['posicao']} {jogadores['camisa']}")

def atualizar_jogador():
    print("\n--- Atualizar Jogador ---")
    if not jogadores:
        print("Nenhum jogador cadastrado.")
        return

    listar_jogador()
    try:
        numero = int(input("\nDigite o número do jogador que deseja atualizar: "))
        if 1 <= numero <= len(jogadores):
            novo_nome = solicitar_nome_valido("Novo Nome: ")
            novo_sobrenome = solicitar_nome_valido("Novo Sobrenome: ")
            nova_posicao = solicitar_posicao_valida('Nova posição: ')
            nova_camisa = solicitar_camisa_valida('Novo número da camisa: ')

            jogadores[numero - 1]["nome"] = novo_nome
            jogadores[numero - 1]["sobrenome"] = novo_sobrenome
            print("Cadastro do paciente atualizado com sucesso!")
        else:
            print("Erro: Número de paciente inexistente.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")

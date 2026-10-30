import os
os.system('cls || clear')


pacientes = []

def solicitar_nome_valido(rotulo):
    """Garante que o nome ou sobrenome não seja vazio/em branco."""
    while True:
        valor = input(rotulo).strip()
        if valor:
            return valor
        print("Erro: O campo não pode ficar em branco. Tente novamente.")


def cadastrar_paciente():
    """Cadastra um novo paciente pedindo nome e sobrenome."""
    print("\n--- Cadastrar Paciente ---")
    nome = solicitar_nome_valido("Nome: ")
    sobrenome = solicitar_nome_valido("Sobrenome: ")

    pacientes.append({"nome": nome, "sobrenome": sobrenome})
    print("Paciente cadastrado!")


def listar_pacientes():
    """Exibe todos os pacientes com um número de identificação."""
    print("\n--- Lista de Pacientes ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    for index, paciente in enumerate(pacientes, start=1):
        print(f"{index}. {paciente['nome']} {paciente['sobrenome']}")


def atualizar_paciente():
    """Atualiza o nome e sobrenome de um paciente existente."""
    print("\n--- Atualizar Paciente ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    listar_pacientes()
    try:
        numero = int(input("\nDigite o número do paciente que deseja atualizar: "))
        if 1 <= numero <= len(pacientes):
            novo_nome = solicitar_nome_valido("Novo Nome: ")
            novo_sobrenome = solicitar_nome_valido("Novo Sobrenome: ")

            pacientes[numero - 1]["nome"] = novo_nome
            pacientes[numero - 1]["sobrenome"] = novo_sobrenome
            print("Cadastro do paciente atualizado com sucesso!")
        else:
            print("Erro: Número de paciente inexistente.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")


def excluir_paciente():
    """Remove um paciente da lista pelo seu número."""
    print("\n--- Excluir Paciente ---")
    if not pacientes:
        print("Nenhum paciente cadastrado.")
        return

    listar_pacientes()
    try:
        numero = int(
            input("\nDigite o número do paciente que deseja excluir: ")
        )
        if 1 <= numero <= len(pacientes):
            paciente_removido = pacientes.pop(numero - 1)
            nome_completo = (
                f"{paciente_removido['nome']} {paciente_removido['sobrenome']}"
            )
            print(f"Paciente '{nome_completo}' removido com sucesso!")
        else:
            print("Erro: Número de paciente inexistente.")
    except ValueError:
        print("Erro: Por favor, insira um número válido.")


def menu():
    """Função principal que gerencia o loop do programa utilizando match case."""
    while True:
        print("\nEXEMPLO DE INTERAÇÃO")
        print("1. Cadastrar paciente")
        print("2. Listar pacientes")
        print("3. Atualizar paciente")
        print("4. Excluir paciente")
        print("0. Sair")

        opcao = input("\nOpção: ").strip()

        match opcao:
            case "1":
                cadastrar_paciente()
            case "2":
                listar_pacientes()
            case "3":
                atualizar_paciente()
            case "4":
                excluir_paciente()
            case "0":
                print("Encerrando o programa... Até logo!")
                break
            case _:
                print("Opção inválida! Tente novamente.")


# Executa o programa
if __name__ == "__main__":
    menu()

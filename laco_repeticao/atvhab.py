import os
os.system('cls')

soma_salarios = total = mulheres_salario = 0
maior_idade = menor_idade = None

while True:
    print('''   | 1 - Adicionar |
    | 2 - Exibir |
    | 3 - Sair |''')
    opcao = int(input("Opção: "))

    match opcao:
        case 1:
            os.system('cls')
            idade = int(input("Idade: "))
            sexo = input("Sexo (M/F): ").strip().upper()
            salario = float(input("Salário (R$): "))

            soma_salarios += salario
            total += 1
        
            maior_idade = idade if maior_idade is None else max(maior_idade, idade)
            menor_idade = idade if menor_idade is None else min(menor_idade, idade)
        
            if sexo == 'F' and salario >= 5000:
                mulheres_salario += 1
            
            os.system('cls || clear')

        case 2:
            if total == 0:
                print("Nenhum dado cadastrado.")
            else:
                print(f"a) Média salarial: R$ {soma_salarios / total:.2f}")
                print(f"b) Maior idade: {maior_idade} | Menor idade: {menor_idade}")
                print(f"c) Mulheres com salário >= R$ 5.000: {mulheres_salario}")

        case 3:
            break

        case _:
            print('Opção inválida.')
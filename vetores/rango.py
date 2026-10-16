import os
os.system('cls || clear')

vetor_pratos = []
vetor_preco = []


print('''== RESTAUTANTE ==
1 - PICANHA (R$25,00)
2- LASANHA (R$20,00)
3 - STROGONOFF (R$18,00)
4 - BIFE ACEBOLADO (R$15,00)
5 - PÃO COM OVO (R$5,00)''')
while True:
    pedido = int(input('Digite o número do prato desejado: '))

    match pedido:
        case 1:
            prato = 'PICANHA'
            preco = 25
        
        case 2:
            prato = 'LASANHA'
            preco = 20

        case 3:
            prato = 'STROGONOFF'
            preco = 18

        case 4:
            prato = 'BIFE ACEBOLADO'
            preco = 15

        case 5:
            prato = 'PÃO COM OVO'
            preco = 5

        case _:
            print('Opção inválida. Tente novamente.')

    if pedido >= 1 and pedido <= 5:
        vetor_pratos.append(prato)
        vetor_preco.append(preco)

        resposta = input('Deseja pedir mais algum prato? (S/N): ').strip().upper()
        if resposta == 'N':
            break
        os.system('cls || clear')

if sum(vetor_preco) == 0:
    print('Nenhum prato foi pedido.')
else:
    print('=== PEDIDO ===')
    for i in range(len(vetor_pratos)):
        print(f'{vetor_pratos[i]} - R${vetor_preco[i]:.2f}')
    valor_total = sum(vetor_preco)
    print(f'Valor total: R${valor_total:.2f}')

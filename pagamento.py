import os
os.system('cls || clear')

valor = float(input('Digite o valor do produto: '))
pagamento = int(input('''Selecione a forma de pagamento:
1 - Pagamento à vista
2 - Pagamento à prazo '''))

match pagamento:
    case 1:
        desconto = valor * 0,1
        valor_final = valor - desconto
        os.system('cls || clear')

        print(f'Valor do produto: R${valor:.2f}')
        print('Forma de pagamento: à vista.')
        print(f'Valor do desconto: R${desconto:.2f}')
        print(f'Total a pagar: R${valor_final:.2f}')

    case 2:
        parcelas = int(input('Digite a quantidade de parcelas: '))
        if parcelas > 6:
            print('Quantidade de parcelas inválidas')
            exit() #FIM DO PROGRAMA
        valor_parcela = valor / parcelas

        print(f'Valor do produto: R${valor:.2f}')
        print('Forma de pagament: à prazo')
        print(f'Quantidade de parcelas: {parcelas}')
        print(f'Valor por parcela: R${valor_parcela:.2f}')
        print(f'Total à prazo: R${valor:.2f}')
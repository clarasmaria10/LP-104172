import os
os.system('cls')

print('= SOLICITANDO DADOS')
valor = float(input("Digite o valor: "))
desconto = float(input("Digite o desconto: "))

# CALCULO
valor_desc = (desconto / 100) * valor
valor_com_desconto = valor - valor_desc

print('= EXIBINDO DADOS')
print("Valor com desconto final: ", valor_com_desconto)
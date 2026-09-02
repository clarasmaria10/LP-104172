import os
os.system("cls")
#ENTRADA
quantidade = int(input("informe quantas maçãs deseja:"))

if quantidade < 12:
    preco = 1.30
else:
    preco = 1.0
valor_total = quantidade * preco

print("valor total: ", valor_total)
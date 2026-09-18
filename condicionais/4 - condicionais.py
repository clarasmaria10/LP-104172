import os
os.system("cls")

numeroa = float(input("Digite o primeiro número: "))
numerob = float(input("DIgite o segundo número: "))
numeroc = float(input("Digite o terceiro número: "))

maior = max(numeroa, numerob, numeroc)
menor = min(numeroa, numerob, numeroc)

# EXIBINDO RESULTADOS
print(f"Números selecionados: {numeroa}, {numerob} e {numeroc}.")
print("Maior número: ", maior)
print("Menor número: ", menor)
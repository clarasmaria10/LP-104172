import os
os.system('cls')

# INICIO
media = float(input("Digite sua média: "))
faltas = int(input('Digite sua quantidade de faltas: '))

# SISTEMA
if media >= 7.0 and faltas <= 40:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"

# FINAL
print("= RESULTADO =")
print(f"Média:{media} ")
print(f"Faltas: {faltas}")
print(resultado)
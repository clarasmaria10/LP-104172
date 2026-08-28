import os
os.system('cls')

# INICIAL
idade = int(input("Qual sua idade? "))

# LOGICA
if 16 > idade:
    print("Você não pode votar.")
elif idade == 16 or idade == 17 or idade >= 65:
    print("Você pode votar, mas não é obrigatório.")
else:
    print("Você tem que votar.")

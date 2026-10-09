import os
os.system('cls || clear')

soma_notas = 0
contador = 0
resposta = 's'

while resposta.upper() != "N":
    nota = float(input("Digite uma nota: "))
    soma_notas += nota
    contador += 1
    resposta = input("Deseja inserir mais uma nota? (S/N): ")

if contador > 0:
    media = soma_notas / contador
    print(f"\nA média aritmética das {contador} notas é: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
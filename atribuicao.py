import os
os.system("cls")

#ENTRADA

nome = (input("digite seu nome: "))
nota1 = int(input("digite sua primeira nota:"))
nota2 = int(input("digite sua segunda nota:"))

#PROCESSAMENTO

media = (nota1 + nota2) / 2

if media >= 9:
    conceito = ("A")
elif media >= 7.5:
    conceito = ("B")
elif media >= 6:
    conceito = ("C")
elif media >= 4:
    conceito = ("D")
else:
    conceito = ("E")
    if media >= 6:
        resultado = ("Você está aprovado")
    else:
        resultado = ("Você está reprovado")

# SAÍDA

print("Nome: ", nome)
print("Sua média: ", media)
print("Seu conceito foi: ", conceito)
print("Seu resultado foi: ", resultado)

import os
os.system('cls || clear')

valor_A = float(input('Digite o primeiro valor: '))
valor_B = float(input('Digite o segundo valor: '))
valor_C = float(input("Digite o terceiro valor: "))

soma = valor_A + valor_B

if valor_C > soma:
    print("A soma dos dois primeiros valores é menor que o terceiro valor.")
else:
    print("A soma dos dois primeiros valores é maior que o terceiro valor.")
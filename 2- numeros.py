import os
os.system('cls')

print("= SOLICITANDO DADOS =")
primeiro = int(input("Digite o primeiro número: "))
segundo = int(input("Digite o segundo número: "))

# Cálculos
media = (primeiro + segundo) / 2
soma = primeiro + segundo
produto = primeiro * segundo
maior = max(primeiro, segundo)
menor = min(primeiro, segundo)

# Resultados
print('Primeiro número: ', primeiro)
print('Segundo número: ', segundo)
print('Média:', media)
print('Soma: ', soma)
print('Produto: ', produto)
print('Maior: ', maior)
print('Menor: ', menor)
import os
os.system('cls')

# ENTRADA
peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

# PROCESSO
imc = peso / (altura * altura)

if imc < 18.5:
    resultado = "Abaixo do peso."
elif imc <= 24.9:
    resultado = "Peso ideal."
elif imc <= 29.9:
    resultado = "Levemente acima do peso"
elif imc <= 34.9:
    resultado = "Obesidade Grau I"
elif imc <= 39.9:
    resultado = "Obesidade Grau II (severa)"
else:
    resultado = "Obesidade Grau III (mórbida)"

# SAÍDA 
print("\n= RESULTADO =")
PRINT(f"Resultado {resultado}")
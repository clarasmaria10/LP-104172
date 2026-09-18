import os
os.system('cls')

numeroa = int(input("Escreva o primeiro número: "))
numerob = int(input("Escreva o segundo número: "))

# SISTEMA
media = (numeroa + numerob) / 2
soma = numeroa + numerob
produto = numeroa * numerob

# RESULTADO

print("= RESULTADOS =")
print(f"A média é {media:.2f}.")
print(f"A soma é {soma:.2f}.")
print(f"O produto é {produto:.2f}.")

if numeroa < numerob:
    print(f"O maior número é o {numeroa}.")
    print(f"O menor número é {numerob}.")
elif numeroa == numerob:
    print(f"Os dois números são iguais.")
else:
    print(f"O maior número é {numerob}")
    print(f"O menor número é {numeroa}.")
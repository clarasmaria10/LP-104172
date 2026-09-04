import os
os.system("cls")

nota = float(input("Digite sua nota: "))

if 10 >= nota >= 0:
    print("Nota: ", nota)
else:
    print("A nota deve ser entre zero e dez.")
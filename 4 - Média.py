import os

# limpa o terminal
os.system('cls')

print('= SOLICITANDO DADOS')
nome = input("Digite seu nome: ")
serie = input("Digite sua série (N° + ano): ")
primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))
media =  (primeira_nota + segunda_nota) / 2

print('\n= EXIBINDO DADOS')
print('Nome: ', nome)
print('Série: ', serie)
print("Primeira nota: ", primeira_nota)
print("Segunda nota: ", segunda_nota)
print("Média: ", media)

if media < 6: 
    print("Aluno(a) reprovado")
else:
    print("Aluno(a) aprovado")
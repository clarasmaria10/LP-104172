import os
os.system("cls")

login = (input("Digite o login: "))
senha = (input("Digite sua senha: "))

login_salvo = 'clarinhars'
senha_salva = '0221'

login_correto = login == login_salvo
senha_correta = senha == senha_salva

if login_correto and senha_correta:
    print("Bem vindo!")
else:
    print("Login e senha inválido.")

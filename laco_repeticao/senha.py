import os
os.system('cls || clear')

QUANTIDADE_TENTATIVAS = 3
tentativas = 0

login_salvo = 'Claramitinha'
senha_salva = '022120'


while True:
    login = input('Digite o login: ')
    senha = input('Digite a senha: ')

    if login == login_salvo and senha == senha_salva:
        print('Acesso permitido!')
        break
    else:
        tentativas += 1
        tentativas_restantes = QUANTIDADE_TENTATIVAS - tentativas
        
        if tentativas >= QUANTIDADE_TENTATIVAS:
            print('Número máximo de tentativas atingido. Acesso negado.')
            break
            
        print(f'Login ou senha incorretos! Você tem {tentativas_restantes} tentativa(s) restante(s).\n')

usuario_correto = "ADM"
senha_correta = "123456789"

while True:
  
    usuario = input("Informe o nome de usuário: ")

    senha = input("Informe a senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Bem-vindo ADM")
        break 
    else:
        print("Usuário ou senha incorretos. Tente novamente.")
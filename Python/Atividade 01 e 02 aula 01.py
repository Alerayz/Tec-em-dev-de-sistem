def cadastrar_usuario():
    # Lê os dados do usuário
    nome = input("Digite seu nome: ")
    email = input("Digite seu email: ")
    senha = input("Digite sua senha: ")
    
    # Exibe os dados salvos
    print("\nDados salvos:")
    print(f"Nome: {nome}")
    print(f"Email: {email}")
    
    # Lê o ano de nascimento
    ano_nascimento = int(input("Digite seu ano de nascimento: "))
    
    # Calcula a idade
    ano_atual = 2024  # Você pode usar datetime para obter o ano atual
    idade = ano_atual - ano_nascimento
    
    # Exibe a idade
    print(f"Sua idade é: {idade} anos")

# Chama a função para executar o cadastro
cadastrar_usuario()
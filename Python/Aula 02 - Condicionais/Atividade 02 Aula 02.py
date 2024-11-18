# Função principal
def calcular_multa():
    # Lê o peso de peixes
    P = float(input("Digite o peso de peixes (em quilos): "))
    
    # Inicializa as variáveis de excesso e multa
    E = 0
    M = 0
    
    # Verifica se há excesso
    if P > 50:
        E = P - 50  # Calcula o excesso
        M = E * 4   # Calcula a multa
    else:
        E = 0
        M = 0
    
    # Mostra os resultados
    print(f"Excesso: {E} quilos")
    print(f"Multa: R$ {M:.2f}")

# Chama a função principal
calcular_multa()
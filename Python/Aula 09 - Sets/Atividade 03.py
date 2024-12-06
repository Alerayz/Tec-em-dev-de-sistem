import random

def escolher_palavra():
    palavras = ['Mercedes Amg', 'Mercedes G63', 'Golf Gti', 'Nissan GT R34', 'NIssan 370z', 'Dodge Hellcat']
    return random.choice(palavras)

def jogar():
    palavra = escolher_palavra()
    letras_adivinhadas = set()
    tentativas = 6
    palavra_oculta = set(palavra)

    print("Bem-vindo ao Jogo da Forca!")
    
    while tentativas > 0 and palavra_oculta != letras_adivinhadas:
        print("\nPalavra: ", end="")
        for letra in palavra:
            if letra in letras_adivinhadas:
                print(letra, end=" ")
            else:
                print("_", end=" ")
        
        print(f"\nTentativas restantes: {tentativas}")
        print("Letras já adivinhadas: ", " ".join(letras_adivinhadas))
        
        letra = input("Adivinhe uma letra: ").lower()
        
        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra. Tente outra.")
        elif letra in palavra:
            letras_adivinhadas.add(letra)
            print("Boa! A letra está na palavra.")
        else:
            letras_adivinhadas.add(letra)
            tentativas -= 1
            print("Ops! A letra não está na palavra.")
    
    if palavra_oculta == letras_adivinhadas:
        print(f"Parabéns! Você adivinhou a palavra: {palavra}")
    else:
        print(f"Você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    jogar()
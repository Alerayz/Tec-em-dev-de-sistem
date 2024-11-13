def identificar_faixa_etaria(idade):
    if 0 <= idade < 17:
        return "Criança"
    elif 18 <= idade < 25:
        return "Jovem"
    elif 25 <= idade < 50:
        return "Adulto"
    elif idade >= 50:
        return "Idoso"
    else:
        return "Idade inválida"

def main():
    try:
        idade = int(input("Informe a sua idade: "))
        faixa_etaria = identificar_faixa_etaria(idade)
        print(f"Você é: {faixa_etaria}")
    except ValueError:
        print("Por favor, insira um número válido para a idade.")

if __name__ == "__main__":
    main()
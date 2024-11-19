def par_ou_impar(numero):
    if numero % 2 == 0:
        return f'O número {numero} é par.'
    else:
        return f'O número {numero} é ímpar.'

resultado = par_ou_impar(7)
print(resultado)

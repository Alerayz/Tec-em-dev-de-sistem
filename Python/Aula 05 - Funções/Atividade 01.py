def multiplicar(*args):
    total = 1
    
    for num in args:
        total *= num
    
    print(f'O total da multiplicação é: {total}')
    return total

resultado = multiplicar(2, 3, 4)
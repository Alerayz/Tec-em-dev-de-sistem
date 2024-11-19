def somarMuitos(*numeros):
    valortotal = 0    

    for numero in numeros:
        valortotal += numero
    print(numeros, valortotal)

somarMuitos(1,2)
somarMuitos(252,901,416,659)
somarMuitos(545564,1651651)

print(sum([1,3,5,7,9]))
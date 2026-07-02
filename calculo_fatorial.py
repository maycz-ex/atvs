import math

#aqui pede o numero inteiro 
numero = int(input("Digite um número inteiro positivo (preferencialmente entre 1 e 10): "))

#aqui é onde o calculo é feito pelo script math.fatorial
fatorial = math.factorial(numero)

#aqui é onde o resultado é mostrado
print(f"O fatorial de {numero} é {fatorial}.")
### CALCULADORA DE FATORIAL ### SIMPLIFICADO USANDO A LIB MATH

from math import factorial

n = int(input("\nDigite um número para calcular o fatorial: "))
contador = n # Estipula-se um 'contador' igual ao N, já que no calculo de fatoriais começa-se a partir de N! e vai descendo de 1 em 1.
print(f"\n{n}! = ", end = "")
while contador > 1: # Enquanto o contador estiver acima de 0...
    print(f"{contador} x ", end = "") # Uso do end="" impedindo a quebra de linha => Ele fica dentro do parênteses do 'print'.
    contador -= 1 # o -= vai diminuindo 1 do 'contador' até chegar a 1 e parar. (porque depois que chega a 0, não printa mais de acordo com o parâmetro 'while')
print(f"1 = {factorial(n)}\n")
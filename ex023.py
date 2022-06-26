### SEPARADOR DE NÚMEROS ###

# Faça um programa que separa um número de 0 a 9999 entre 'milhares', 'centenas', 'dezenas' e 'unidades'

# Strings
num = int(input("\nDigite aqui o número que você quer separar em 'milhares', 'centenas', 'dezenas' e 'unidades': "))
# Transforma o (num) em str para fragmentar os seus 'caracteres' nas ações abaixo
nstr = str(num)

# Ações - Prints e fragmentações da str
print("\nAnalisando o número {}".format(num))
print(f"\nUnidade(s): {nstr[3]}")
print(f"Dezena(s): {nstr[2]}")
print(f"Centena(s): {nstr[1]}")
print(f"Milhar(es): {nstr[0]}\n")


### O PROBLEMA AQUI É QUE NÃO FUNCIONA PARA NÚMEROS DE MENOS DE 4 ALGARISMOS
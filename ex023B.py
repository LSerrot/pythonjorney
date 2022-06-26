### SEPARADOR DE NÚMEROS ###

# Faça um programa que separa um número de 0 a 9999 entre 'milhares', 'centenas', 'dezenas' e 'unidades'

# Strings
num = int(input("\nDigite aqui o número que você quer separar em 'milhares', 'centenas', 'dezenas' e 'unidades': "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

# Ações
print(f"MILHAR(ES): {m}\nCENTENA(S): {c}\nDEZENA(S): {d}\nUNIDADE(S): {u}\n")

# CONFESSO NÃO TER ENTENDIDO BEM COMO FUNCIONA ISSO DE MÓDULOS ( % 10)
# NOVO ENTENDIMENTO: X % 10 SIGNIFICA QUE EU PEGO O X, DIVIDO POR 10 E FICO COM O QUE SOBROU.
# EXEMPLO: 230
# 230 % 10 seria 230/10 isolando o resto e ficando com ele.
# Ou seja: 23 (20 + 3. Pega o 3 -> 3 dezenas).

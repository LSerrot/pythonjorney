### AUMENTOS MÚLTIPLOS ###

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10$.
# Para os inferiores ou iguais, o aumento é de 15%.

# Importações
from colorama import Fore

# Strings
salario = float(input("\nDigite aqui o salário do funcionário => R$"))
salario15 = salario + (salario * 0.15)
salario10 = salario + (salario * 0.1)

# Ação - Print + If
if salario > 1250:
    print(
        f"\nEsta faixa salarial sofre 10% de ajuste e, portanto, o novo salário vai para {Fore.GREEN}R${salario10:.2f}{Fore.RESET}.")
else:
    print(
        f"\nEsta faixa salarial sofre 15% de ajuste e, portanto, o novo salário vai para {Fore.GREEN}R${salario15:.2f}{Fore.RESET}.")

input("\nDigite 'Enter' para encerrar a sessão. ")

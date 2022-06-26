### APROVANDO OU NÃO UM EMPRÉSTIMO ###

# Escreva um programa para aprovar um emprésitmo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

# Importações
from colorama import Fore

# Strings

imovel = int(input("\nDigite aqui o valor do imóvel => R$"))
salario = int(input("Digite aqui quanto você ganha => R$"))
anos = int(input("Digite aqui em quantos anos você quer pagar: "))
parcelas = anos * 12

# Ação

if imovel / parcelas > salario * 0.3:
    print(f"\n{Fore.RED}O seu empréstimo foi RECUSADO.\nAs parcelas de R${imovel / parcelas:.2f} excedem 30% do seu salário de R${salario:.2f},\nIsso não cumpre com as diretrizes do banco.{Fore.RESET}")
else:
    print(f"\n{Fore.GREEN}O seu empréstimo foi APROVADO.\nAs parcelas de R${imovel / parcelas:.2f} estão de acordo com o seu salário de R${salario:.2f}.\nVamos prosseguir?{Fore.RESET}")

input("\nDigite 'Enter' para encerrar esta aplicação e seguir para a próxima etapa. ")

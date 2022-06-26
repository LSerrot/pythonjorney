### CONVERSOR DE BASES NUMÉRICAS ###

# Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal


# Strings - input 'número inteiro'
num = int(input("\nDigite um número inteiro: "))

# Strings linkáveis
bin_ = bin(num)
oct_ = oct(num)
hex_ = hex(num)

# Menu
print('''\nEscolha uma das bases parar conversão:\n
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
''')  # destaque para a boa utilização do ''' para muitos textos em linhas diferentes

# Opção escolhida
opcao = int(input("Sua opção: "))


# Ação => if + print + contagem de posição [a partir de > até a] 
if opcao == 1:
    print(f"\n{num} convertido para BINÁRIO é igual a {bin_[2:]}") # Quando não se preenche nada após os ':', presume-se que é até o fim da str
elif opcao == 2:
    print(f"\n{num} convertido para OCTAL é igual a {oct_[2:]}")
elif opcao == 3:
    print(f"\n{num} convertido para HEXADECIMAL é igual a {hex_[2:]}")
else:
    print("\nOpção inválida. Encerrando a sessão...\n")

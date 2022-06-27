### SIMULADOR SISU ###

# Importações
from time import sleep

def input_de_validacao(msg):
    x = input(msg)
    while x.isnotnumeric():
        x = input_de_validacao("Valor inválido" + msg)
    x = float(x)
    return x
    


# Strings inputáveis
print()
print("-=-" * 13)
print("Seja bem-vindo(a) ao Sisu Calculator!")
print("-=-" * 13)
print('''
[ 1 ] SIMPLES
[ 2 ] PONDERADA
''')
tipo = input("Escolha qual o tipo de média você quer calcular: [1/2] ").strip().lower()
while tipo == "" or tipo not in '12':
    tipo = input("Opção inválida. Escolha qual o tipo de média você quer calcular: [1/2] "))

# CÁLCULO DA MÉDIA SIMPLES
if tipo == "1":
    print("\nVamos dar início ao cálculo da sua média simples!")

    n_lct = float(input("\nDigite aqui a sua nota em Linguagens: "))
    n_cht = float(input("Digite aqui a sua nota em Ciências Humanas: "))
    n_cnt = float(input("Digite aqui a sua nota em Ciências da Natureza: "))
    n_mat = float(input("Digite aqui a sua nota em Matemática: "))
    n_red = float(input("Digite aqui a sua nota em Redação: "))

    ms = (n_lct + n_cht + n_cnt + n_mat + n_red) / 5

    print("\nAguarde...")

    sleep(2)

    print(f"\nA sua média simples é de {ms} pontos.\n")

# CÁLCULO DA MÉDIA PONDERADA
elif tipo == "2":

    print("\nVamos dar início ao cálculo da sua média ponderada!")

    p_lct = float(input(
        "\nDigite aqui o peso que o curso e a universidade que você quer passar destinam para Linguagens: "))
    p_cht = float(input(
        "Digite aqui o peso que o curso e a universidade que você quer passar destinam para Ciências Humanas: "))
    p_cnt = float(input(
        "Digite aqui o peso que o curso e a universidade que você quer passar destinam para Ciências da Natureza: "))
    p_mat = float(input(
        "Digite aqui o peso que o curso e a universidade que você quer passar destinam para Matemática: "))
    p_red = float(input(
        "Digite aqui o peso que o curso e a universidade que você quer passar destinam para Redação: "))

    print("\nOk, agora vamos para as suas notas...")

    sleep(3)

    n_lct = float(input("\nDigite aqui a sua nota em Linguagens: "))
    n_cht = float(input("Digite aqui a sua nota em Ciências Humanas: "))
    n_cnt = float(input("Digite aqui a sua nota em Ciências da Natureza: "))
    n_mat = float(input("Digite aqui a sua nota em Matemática: "))
    n_red = float(input("Digite aqui a sua nota em Redação: "))

    mp = ((n_lct * p_lct) + (n_cht * p_cht) + (n_cnt * p_cnt) + (n_mat *
          p_mat) + (n_red * p_red)) / (p_lct + p_cht + p_cnt + p_mat + p_red)

    print("\nAguarde...")

    sleep(3)

    print(
        f"\nA sua média ponderada de acordo com os pesos preenchidos é de {mp:.2f} pontos.\n")

# INPUT DE ENCERRAMENTO DE SESSÃO
input("Digite 'Enter' para finalizar a sessão.")

### SIMULADOR SISU ###

# Importações
from time import sleep

# Strings inputáveis
print()
print("-=-" * 13)
print("Seja bem-vindo(a) ao Sisu Calculator!")
print("-=-" * 13)
print('''
[ S ] SIMPLES
[ P ] PONDERADA
''')
tipo = input("Escolha qual o tipo de média você quer calcular: [S/P] ").strip().lower()
while tipo not in 'sp':
    tipo = str(
        input("Opção inválida. Escolha qual o tipo de média você quer calcular: [S/P] "))

# CÁLCULO DA MÉDIA SIMPLES
if tipo == "s":
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
elif tipo == "p":

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
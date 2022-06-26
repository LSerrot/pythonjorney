### CRIANDO UM MENU DE OPÇÕES ###

# Crie um programa que leia DOIS VALORES e mostre um MENU. Seu programa deverá realizar a operação solicitada em cada caso.

# Boas-vindas
print()
print("-=-" * 10)
print("Seja bem-vindo ao Calc'O'Matic!")
print("-=-" * 10)
print()
# Inputs de valores (em loop até serem preenchidos)
v1 = input("Digite o primeiro valor: ")
while v1 == "":
    v1 = input("Valor inválido. Digite o primeiro valor: ")
v2 = input("Digite o segundo valor: ")
while v2 == "":
    v2 = input("Valor inválido. Digite o segundo valor: ")
v1_float = float(v1)
v2_float = float(v2)
print()
menu = 0
print("-=-" * 11)

# Menu
while menu != 5:
    print('''
    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS
    [ 5 ] SAIR
    ''')
    menu = int(input("Qual opção você escolhe? "))
    print()
    print("-=-" * 11)
    if menu == 1:  # SOMAR
        print()
        print("O resultado desta adição é:")
        print(f"\n{v1_float} + {v2_float} = {v1_float + v2_float}.")
        print()
        print("-=-" * 11)

    elif menu == 2:  # MULTIPLICAR
        print()
        print("O resultado desta multiplicação é:")
        print(f"\n{v1_float} x {v2_float} = {v1_float * v2_float}.")
        print()
        print("-=-" * 11)

    elif menu == 3:  # MAIOR

        if v1_float > v2_float:
            print()
            print(f"\n{v1_float} é maior que {v2_float}.")
            print()
            print("-=-" * 11)

        elif v1_float < v2_float:
            print()
            print(f"\n{v2_float} é maior que {v1_float}.")
            print()
            print("-=-" * 11)

        elif v1_float == v2_float:
            print()
            print("\nAmbos têm o mesmo valor.")
            print()
            print("-=-" * 11)

    elif menu == 4:  # NOVOS NÚMEROS (Em loop até serem preenchidos)
        print()
        v1 = input("Digite o primeiro valor: ")
        while v1 == "":
            v1 = input("Valor inválido. Digite o primeiro valor: ")
        v2 = input("Digite o segundo valor: ")
        while v2 == "":
            v2 = input("Valor inválido. Digite o segundo valor: ")
        v1_float = float(v1)
        v2_float = float(v2)
        print()
        print("-=-" * 11)

    elif menu == 5:  # ENCERRAR SESSÃO
        quit()

    else:  # OPÇÃO INVÁLIDA.
        print()
        print("Opção inválida. Tente novamente com um dígito de 1 a 5: ")
        print()
        print("-=-" * 11)

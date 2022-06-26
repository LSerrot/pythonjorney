### FORMA OU NÃO FORMA UM TRIÂNGULO? ###

## BESSE EU FIQUEI COM ALGUMAS DÚVIDAS SOBRE SE USAVA >= OU >. SERIA IMPORTANTE CONFERIR SE O QUE EU FIZ TÁ VALENDO.

# Strings
r1 = float(input("\nDigite aqui o valor do primeiro lado em centímetros: "))
r2 = float(input("Digite aqui o valor do segundo lado em centímetros: "))
r3 = float(input("Digite aqui o valor do terceiro lado em centímetros: "))


# Aqui há uma regra matemática simples: 
# NÂO é possível se formar triângulos quando um dos lados é maior que a soma dos outros dois.
# Portanto, |r1 > (r2+r3) == False| (assim, como |r2 > (r1 + r3) == False|; e |r3 > (r1 + r2) == False| também são.)

# Ação
if r1 >= r2 + r3:
    print("\nOs lados NÃO PODEM formar um triângulo!")
elif r2 >= r1 + r3:
    print("\nOs lados NÃO PODEM formar um triângulo!")
elif r3 >= r1 + r2:
    print("\nOs lados NÃO PODEM formar um triângulo!")
else:
    print("\nOs lados PODEM formar um triângulo!")


input("\nDigite 'Enter' para encerrar a sessão. ")
### DIZ QUAL O ANTECESSOR E O SUCESSOR ###

# Strings
numero = int(input("Digite aqui o número que bem entender: "))

# Função já dentro do format na hora do print (o que economiza memória)
print(
    f"Analisando o valor {numero}, constato que o seu antecessor é {numero - 1} e o seu sucessor é {numero + 1}. Incrível, né?")

# Vale dizer que se eu por algum motivo precisasse desse antecessor e desse sucessor lá na frente, talvez fosse legal criá-los na forma de variáveis, como abaixo:
# numero = int(input("Digite aqui o número que você bem entender: "))
# antecessor = numero - 1
# sucessor = numero + 1
# print(f"Analisando o valor {numero}, posso constatar que o seu antecessor é {antecessor} e o seu sucessor é {sucessor}. Incrivél, né?")
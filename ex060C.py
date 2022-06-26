### CALCULADORA DE FATORIAL ### SIMPLIFICADO USANDO A LIB MATH

# Strings
n = int(input("\nDigite um número para calcular o fatorial: "))
contador = n # Estipula-se um 'contador' igual ao N, já que no calculo de fatoriais começa-se a partir de N! e vai descendo de 1 em 1.
fatorial = 1 # FATOR NULO DE FATORIAIS, DIVISÕES E MULTIPLICAÇÕES [SOMA E SUBTRAÇÃO É 0] 

# Ações - print + while + if/else + factorial + ---> -= <---
print(f"\n{n}! = ", end = "")

while contador > 0: # Enquanto o contador estiver acima de 0...

    print(f"{contador} ", end = "") # Uso do end="" impedindo a quebra de linha => Ele fica dentro do parênteses do 'print'.

    print("x " if contador > 1 else "= ", end = "") # Aqui usei o if e else na mesma linha para as definições do sinal após o número. Vai diminuindo até no 1 mudar de 'x ' para '= '
    fatorial *= contador # Sempre que o contador mudar de acordo com a parametrização if/else acima, é multiplicado pelo seu valor nulo ('fatorial')
    contador -= 1 # o -= vai diminuindo 1 do 'contador' até chegar a 1 e parar. (porque depois que chega a 0, não printa mais de acordo com o parâmetro 'while')

print(fatorial)

### O ESQUEMA DO CONTADOR FICOU RELATIVAMENTE CLARO PARA MIM, O DO STR FATORIAL TERMINANDO SE MULTIPLICANDO ENTRE SI A PONTO DE RESOLVER TUDO SÓ COM O print(fatorial) NÃO FICOU CLARO.
# nesta etapa e realizada a criacao de funcoes
# funcoes podem ou nao nao receber dados, para realizar uma acao
# proporciona modularidade e possibilidade de reuso

# toda funcao em python inicia com a palavra reservada "def"
# em seguida, o nome da funcao, acompanhada por parenteses e seus parametros
# depois vem o corpo da funcao indentado e suas instrucoes
# e por ultimo, o retono

# funcao basica
def minha_funcao(msg):
    print(msg)

minha_funcao("Ola Mundo")

# funcao sem parametro
def imprimir_nome():
    print("Ola Mundo")
    
# funcao com um parametro
def imprimir_nome(nome):
    print(nome)

# chamando funcao, com parametro "Tom Hanks"
imprimir_nome("Tom Hanks")


# argumento posicional, deve ser passado na mesma ordem em que foi definido
# Definição da função
def somatorio(a, b, c):
    print(a + b + c)

# Chamada da função com os argumentos passados por posição
somatorio(1, 5, 9)


# argumento nomeados, ordem nao importa, pois ja foi definido o valor
# Definição da função
def somatorio(a, b, c):
    print(a + b + c)

# Chamada da função com os argumentos passados de forma nomeada
somatorio(b=1, c=5, a=9)


# argumento padrao
# Definição de uma função
def imprimir_nome(nome, sobrenome='Silva'):
    print(f'{nome} {sobrenome}')

# Chamando a função e passando apenas o primeiro argumento
imprimir_nome('Jorge') # Jorge Silva

# Chamando a função e passando dois argumentos, sobrescrevendo o valor padrao
imprimir_nome('Jorge', 'Luiz') # Jorge Luiz


# retornando um valor em uma funcao
# return encerra a funcao
def par_ou_impar(num):
    if num % 2 == 0:
        return True
    else:
        return False

# atribui funcao na variavel numero_par
numero_par = par_ou_impar(5)

# exibe valor: False
print(numero_par)


# funcao recursiva
# quando uma funcao chama a si mesma
# deve ter condicao base de parada
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(10))
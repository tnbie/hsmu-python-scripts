#-------------------------------------------------------#
## primeiro_programa.py
## primeiro contato com python no curso da hsm university
#-------------------------------------------------------#

# usando o print
print("Hello World!")

# criando uma variavel numerica e vendo o seu tipo
numero = 10
print(type(numero))
print(numero)

# criando uma variavel numerica e vendo o seu tipo
resultado = "10"
print(type(resultado))
print(resultado)

# criando uma variavel de texto e vendo o seu tipo
cidade = "Fortaleza"
print(cidade)

# atribuindo valores a varias variaveis
a, b, c = 10, 20, 40
print(a, b, c)

# operacao matematica com variaveis
d = 200
e = 250
print(d + e)

# python e case sensitive
nome = "Luiz"
Nome = "Joao"
print(nome)
print(Nome)

# alterando o valor de uma variavel
nome = 15
print(nome)

# tipos inteiro positivo
valor = 50
print(type(valor))
print(valor)

# tipos inteiro negativo
valor_negativo = -5
print(type(valor_negativo))
print(valor_negativo)

# tipo complexo
var_uu = 3+5j
print(var_uu)
print(type(var_uu))

# tipo texto aspas duplas
str1 = "bicicleta"
print(str1)
print(type(str1))

# tipo texto aspas simples
str2 = 'bicicleta2'
print(str2)
print(type(str2))

# texto multi linhas
frase = '''
Python é uma linguagem muito poderosa
 
Ela possui strings que podem ser divididas
em várias linhas a fim de deixar o texto
mais legível.
'''
print(frase)

# operacoes com texto (concatenacao)
nome_teste = "Joao"
sobrenome_teste = "Pedro"
print(nome_teste + sobrenome_teste)

# indice usando texto
str3 = "Python"

# posicao 1
print(str3[0])

# posicao 6
print(str3[5])

# busca inversa - ultima posicao 
print(str3[-1])

# busca inversa - contagem posicao
print(str3[-3])

# slicing (fatiamento de textos)
# indice inicial:indice final
str4 = str3[0:3]
print(str4)

# omitindo indice inicial
str5 = str3[:4]
print(str5)

# indice final no fim da palavra
str6 = str3[1:]
print(str6)

# nao e permitida a modificacao dos indices
# erro intencional
str7 = "carro"
print(str7)

# transforma em uppercase - maiusculas
atriz = "Angelina Jolie"
print(atriz)
print(atriz.upper())

# transforma em lowercase - minusculas
print(atriz.lower())

## tamanho do texto
print(len(atriz))

# dados booleanos
print(5 < 9)
print(type(True))
print(5 < 3)
print(type(True))

# operadores matematicos
# adicao
print(10 + 8)

# subtracao
print(10 - 8)

# multiplicacao
print(5 * 6)

# divisao
print(7 / 2)

# divide dois valores com arredondamento (sem modulo)
print(7 // 2)

# resto da divisao (modulo)
print(7 % 2)

# exponenciacao
print(7 ** 2)

# operadores atribuicao
# atribuicao simples
x = 25
print(x)

# atribuicao composta - adicao
x += 50
print(x)

# atribuicao composta - subtracao
x -= 50
print(x)

# atribuicao composta - multiplicacao
x *= 200
print(x)

# atribuicao composta - divisao
x /= 500
print(x)

# atribuicao composta - divisao sem modulo
x //= 700
print(x)

# atribuicao composta - resto da divisao (modulo)
x %= 1000
print(x)

# operadores relacionais
# se ambos iguais
x = 5
y = 5
print(x == y)

# se um for diferente
z = 5
w = 10
print(z != w)

# se x maior que y
x = 5
y = 10
print(5 > 10)

# se x menor que y
x = 5
y = 10
print(5 < 10)

# se x maior ou igual que y
x = 5
y = 10
print(5 >= 10)

# se x menor ou igual que y
x = 5
y = 10
print(5 <= 10)

# operadores logicos
# and
x = 1
print(x < 4 and x < 2)

# or
x = 1
print(x < 5 or x < 12)

# not -  negacao
x = 1
print(not(x < 5))

# operadores de identidade
# is
x = 10
y = 10
str1 = "Python"
str2 = "Python"
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(x is y)
print(str1 is str2)
print(lista1 is lista2)

# is not
print(x is not lista1)

# operadores de associacao
# in
lista = [10, 20, 30]
x = 10
print(x in lista)

# not in
y = 5
print(x not in lista)
print(y not in lista)

# print com parametros
var = 1
var1 = 10
var2 = 20
var3 = 30
print(var1, var2, var3)
print(var1, var2, var3, sep="-")

# definindo formatacao por tipo de variavel
# s% string, %d numero int, %f numero float
nome = "Harry Potter"
print("Bem-Vindo %s" % nome)

valor = 50
print("O valor do produto e R$ %d reais" % valor)

# formatando a saida
# chaves indicam aonde os objetos serao passados (indices)
print('Estamos aqui aprendendo {}. Linguagem simples e "{}!" '.format('Python', 'eficaz'))

# usando o indice
print('{0} e {1}'.format('leite', 'ovos'))

# entrada de dados
# input - entrada de dados usuario (terminal)
valor = input('Insira um valor: ')
print(valor)
print(type(valor))

# conversao tipo
# por padrao input e string, necessario converter usando int, se precisar
valor = int(input('Insira um valor: '))
print(valor)
print(type(valor))

# float, decimal
idade = 50
print(type(idade))
print(idade)
idade = float(idade)
print(type(idade))
print(idade)

frase = "Python e uma linguagem divertida"
print(frase[:12])

## usando elif 
estado = input('Nome de um estado: ').lower()

if 'ceara' in estado:
    print('Fortaleza')
elif 'bahia' in estado:
    print('Salvador')
elif 'minas gerais' in estado:
    print('Belo Horizonte')
elif 'amazonas' in estado:
    print('Manaus')
else:
    print('O estado inserido ainda não foi cadastrado!')
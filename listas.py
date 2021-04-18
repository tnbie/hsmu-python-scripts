# lista (mutavel)
linguagem = ['Python', 'Java', 'C++', 'Cobol']
print(linguagem)
      
# alterando valor de uma lista, usando indices (sempre comeca no 0)
linguagem[2] = 'C#'
print(linguagem)


# tuplas
# (imutavel)
t1 = ('a', 'b', 'c', 'd', 'e')

# acessando item na tupla
print(f'The value of index 1 of t1 is: {t1[1]}')

# erro ao tentar modificar uma tupla
# t1[0] = 'A'

# pode definir assim tambem
t2 = tuple()

# imprime t1
print(t1)

# imprime vazio
print(t2)


# dicionarios
# tambem conhecido como key-pair value
# chave usada como ref, semelhante a um campo de um banco de dados
# valores, imutaveis ou nao,. dependendo da utilizacao
t3 = {"name": "Erich", "last_name": "Malfertheiner", "job": "system analyst"}
print(t3)

# pode definir assim tambem
dict = ("a = 1", "b = 2", "c = 3", "d = 4")
print(dict)

# acessando itens
print(t3['name'])

# usando get
print(t3.get('job'))


# criando listas
comidas = ['Feijoada', 'Risoto', 'Lasanha', 'Picanha', 'Sopa de Legumas']
print(comidas)

# listas com diferentes tipos de dados
valores = [1, 3.89, "Null", [3, 4, 5] ]
print(valores)

# acessando os elementos de uma lista
print(comidas[1])

# sem terno indice inicial
print(comidas[-4])

print(comidas[0:3])
print(comidas[1:])
print(comidas[:4])

# copia da lista
print(comidas[:])

# adiciona elemento ao fim de uma lista
comidas.append('Pao de Queijo')
print(comidas)

# removendo um item de uma lista, a partir do indice
del comidas[0]
print(comidas)

# removendo o metodo remove
print(comidas.remove('Risoto'))

# tamanho de uma lista
print(len(comidas))

# concatenacao listas
lista_uni = [5, 6, 7] + [8, 9 , 10]
print(lista_uni)

# repeticao de lista
lista_repeticao = ['Ola Mundo'] * 4
print(lista_repeticao)

# associacao listas (verificacao)
test_list = 5 in [4, 5, 6]
print(test_list)


# acessando elementos de uma tupla
vogais = ('a', 'e', 'i', 'o', 'u')
print(vogais[0])

# contar quantas vezes um elemento se repete
print(vogais.count('a'))

# verificar indice dado um item da tupla
print(vogais.index('a'))


# dicionarios
veiculos = {'Volkswagen' : 'Polo', 'Chevrolet' : 'Cobalt', 'Hyundai' : 'HB20', 'Ford' : 'Fiesta'}
print(veiculos)

# dicionarios com numero inteiros
numbers = {1 : 'One', 2 : 'Two', 3 : 'Three'}
print(numbers)

# elementos de tipos diferentes
apple = {'Apple': ['IPhone', 'Macbook', 'iMac'] , 1 : 'USA'}
print(apple)

# acessando o elemento Ford
print(veiculos['Ford'])

# acessando com get
print(veiculos.get('Hyundai'))

# KeyError - chave inexistente
# print(veiculos['Honda'])

# adicionando um novo elemento
veiculos['Honda'] = 'Civic'

# alterando um valor
veiculos['Volkswagen'] = 'Jetta'

# imprimindo valores
print(veiculos)

# agora ele localiza o valor 'Honda'
print(veiculos['Honda'])

# manipulando elementos de um dicionario
print(f'Removendo o item: {numbers.pop(2)}')

# verificando
print(numbers)

# retornando todas as chaves
print(veiculos.keys())

# retornando todos os valores
print(veiculos.values())

# retorna todos os itens (key e value), em formato de dicionarios
print(veiculos.items())

## exercises
a = [1,2,3,4,5]
print(a[3:0:-1])
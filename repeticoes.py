# lacos de repeticao
# while
contador = 0

# while contador != 100:
 #   nome = input('Digite um nome: ')
  #  contador = contador + 1


# while com else
while contador < 3:
    print("Dentro do loop")
    contador = contador + 1
else:
    print('Dentro do else')
    
# for
capitais = ['Recife','Maceio','Salvador','Aracaju']

# usando o for
for x in capitais:
    # a variavel de controle pode ter qualquer nome, nesse caso ("x")
    print(x)
    
# usando loop while para iterar lista para o mesmo comando do for
index = 0
tamanho_lista = len(capitais)

while index < tamanho_lista:
    print(capitais[index])
    index = index + 1
    
    
# usando o else junto com o for   
for cidade in capitais:
    print(cidade)
else:
    print('Nao ha mais cidades.')
    
# necessario sempre avaliar se o tipo de laco corresponde ao tipo de problema

# resolvendo um problema com while
secreto = 10
tentativa = ''
contador = 0

while tentativa != secreto:
    tentativa = int(input("Digite um numero: "))
    contador += 1
    
    
# resolvendo um problema com for
for number in range(0, 11):
    print(3 * number)
    

# break
# exemplo 1
for letra in 'Recife':
    # executa por letra ate o i, e no i, ele para a execucao
    if letra == 'i':
        break
    print('Letra:', letra)
    
# exemplo 2    
numero = 1
while numero > 0:
    print('Valor:', numero)
    numero += 1
    # executa ate o numero 4, e no 5, ele para a execucao
    if numero == 5:
        break
    
# continue
# exemplo 1
for letra in 'Recife':
    # executa por letra ate o i, e no i, ele salta para proxima execucao
    if letra == 'i':
        continue
    print('Letra:', letra)
    
# exemplo 2
numero = 5
while numero > 0:
    print('Valor: ', numero)
    numero -= 1
    if numero == 5:
        continue

# pass
# utilizado para futuras implementacoes
# interpretado como nulo
for letra in 'Recife':
    pass

# iteracao usando loops
# iterando sobre listas, usando for e while
linguagens = ['Python', 'C++', 'Java', 'Swift', 'Dart']

# ler lista usando o for
for l in linguagens:
    print(l)

# ler lista usando o while
x = 0
while x < len(linguagens):
    print(linguagens[x])
    x += 1
    
# iterando sobre tuplas
frutas = ('banana', 'maca', 'pera', 'laranja')

# retornando o index e o valor na tupla
for var in frutas:
    # detalhe na palavra index aqui
    print(frutas.index(var), var)
    
    
# iterando sobre dicionarios


# usando chaves
supermercado = {'banana': 1.90, 'arroz': 4.5, 'óleo': 6.45}

print(supermercado.keys())

for key in supermercado.keys():
    # busca pelas chaves do dicionario
    print(key)


# usando valores
supermercado = {'banana': 1.90, 'arroz': 4.5, 'óleo': 6.45}

print(supermercado.values())

for value in supermercado.values():
    # busca pelos valores do dicionario
    print(value)
    
    
# usando itens
supermercado = {'banana': 1.90, 'arroz': 4.5, 'óleo': 6.45}

print(supermercado.items())

for item in supermercado.items():
    # busca pelos itens do dicionario
    print(item)

# exemplo 1
total = 0

compras = {
    "camisa": 79.99,
    "sapato": 299.99,
    "cinto": 50.00,
    "hamburguer": 22.80,
    "cinema": 35.50,
    "pipoca": 10.00,
    "estacionamento": 10.00
}

# itera sobre valores dos items
for item in compras.values():
    total = total + item

print("Total gasto R$ %.2f" % total)

# exemplo 2
lista1 = [5, 20, 15, 20, 25, 50, 20]

# remove o item 20 da lista
for num in lista1:
    if num == 20:
        lista1.remove(num)

print(lista1)
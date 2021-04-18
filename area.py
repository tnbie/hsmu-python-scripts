# definindo instrucoes
# constante sempre em maiuscula
PI = 3.14
raio = float(input('Digite o raio do circulo: '))
area = PI * (raio ** 2)
print(area)

# precisao de casas decimais
altura = float(input("Informe sua altura: "))
peso = float(input("Informe o seu peso: "))
imc = peso / (altura * altura)

# definindo precisao usando %.2f (duas casas decimais)
print("Seu IMC e: %.2f" % imc)

# interpolacao de strings
# substitui uma variavel (int, float) por string na saida
## note o f, no print
altura = float(input("Informe sua altura: "))
peso = float(input("Informe o seu peso: "))
imc = peso / (altura * altura)
print(f'Seu IMC e: {imc}')

# calculo de nota semestral, usando expresssao
nota1 = float(input('Insira a primeira nota: '))
nota2 = float(input('Insira a segunda nota: '))
nota3 = float(input('Insira a terceira nota: '))

media = float((nota1 * 2) + (nota2 * 4) + (nota3 * 6)) / 12
print(f'{media}')

# caixa eletronico
valor = int(input('Valor de saque R$: '))

cedulas_100 = int(valor / 100)
valor = valor % 100

cedulas_50 = int(valor/50)
valor = valor % 50

cedulas_20 = int(valor/20)
valor = valor % 20

cedulas_10 = int(valor/10)
valor = valor % 10

cedulas_5 = int(valor/5)
valor = valor % 5

cedulas_2 = int(valor/2)
valor = valor % 2

cedulas_1 = valor

print(
f'{cedulas_100} notas de R$100,00',
f'{cedulas_50} notas de R$50,00',
f'{cedulas_20} notas de R$20,00',
f'{cedulas_10} notas de R$10,00',
f'{cedulas_5} notas de R$5,00',
f'{cedulas_2} notas de R$2,00',
f'{cedulas_1} notas de R$1,00', sep='\n')

# Concatenação de Strings
a = 'São'
b = 'Paulo'
print(a + b)

# Retorna as 3 últimas letras
a = 'Pernambuco'
print(a[-3:])

# Imprimindo apenas os índices pares
str = 'Alemanha'
print(str[::2])

## manipulando strings
frase = 'um passo a frente e você não estará no mesmo lugar!'

# Método capitalize torna a primeira letra maiúscula
print(frase.capitalize())

# Método upper() retorna todos os caracteres em maiúsculo
print(frase.upper())

# Método len() retorna o comprimento da string
print('Tamanho da frase:', len(frase))

# Usando a vírgula como delimitador juntamos as vogais
vogais = "aeiou"
delimiter = vogais + ": "+  ", ".join(vogais)
print(delimiter)
# a, e, i, o, u

# Quebrando a frase onde se tem uma vírgula
frase = 'Ola, mundo, incrível'

# ['Olá', 'mundo', 'incrível']
# separar strings
print(frase.split(', '))


# agrupando strings
marvel = ['Hulk', 'Thor', 'Iron Man', 'Captain America', 'Thanos', 'Black Panther']
print(marvel)

# unir (join)
herois = '-'.join(marvel)
# Hulk-Thor-Iron Man-Captain America-Thanos-Black Panther


herois.split(' ')
# ['Hulk-Thor-Iron', 'Man-Captain', 'America-Thanos-Black', 'Panther']
print(herois)


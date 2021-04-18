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
    

# break & continue

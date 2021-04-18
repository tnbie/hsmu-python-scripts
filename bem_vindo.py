nome = input("Qual seu nome? ")
ano_nascimento = int(input("Qual o ano de seu nascimento? "))
ano_atual = 2020
idade = ano_atual - ano_nascimento

# formatando strings e quebrando a linha
print('Bem vindo(a) {0}, \n Voce tem {1} anos'.format(nome, str(idade)))

# usando if
idade = int(input("Digite sua idade com 2 digitos: "))
if idade > 18:
    print("Voce e maior de idade")

# usando else como condicao
velocidade = int(input("Digite a velocidade capturada: "))
if velocidade <= 80:
    print("Velocidade permitida")
else:
    print("Voce foi multado")
    
## ATENCAO: PONTO IMPORTANTE ##
# usando elif, avaliar outra condicao
x = 5
y = 10
# executada se primeiro e True
if x > y:
    print("X maior que Y")
# executada se anterior nao for True = (False)   
elif x == y:
    print("X igual a Y")
# executado quando nenhuma das condicoes e True
else: 
    print("Y maior que X")
    

# estrutura aninhada
if x > y:
    print("True")
    if x >= 100:
        print("Sim")
    else:
        print("Nao")    
else:
    print("Nao")
    
 # estrutura aninhada parte 2
nota = int(input("Digite sua nota: "))
if nota >= 7:
    print("Aprovado com o conceito:")
    if nota >= 9:
        print("A")
    elif nota >= 8:
        print("B")   
    elif nota >= 7:
        nota("C")
elif nota >= 6:
    print("Exame Final!")
else:
    print("Reprovado!")
    
# estrutura de decisao
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite um outro valor: '))
operacao = int(input('Digite o número da operação que deseja realizar: \
                        \n(1) - soma \
                        \n(2) - subtração \
                        \n(3) - multiplicação \
                        \n(4) - Divisão: \n'))
if (operacao == 1 ):
    print(valor1 + valor2)
if (operacao == 2 ):
    print(valor1 - valor2)
if (operacao == 3 ):
    print(valor1 * valor2)
if (operacao == 4 ):
    print(valor1 / valor2)

# if else exemplo
numero = int(input('Digite um valor: '))
if numero % 2 == 0:
    print('{0} é um número par'.format(numero))
else:
    print('{0} é um número ímpar'.format(numero))


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
    

# operador ternario
numero = int(input("Digite um valor: "))
print("Numero par" if numero % 2 == 0 else "Numero impar")
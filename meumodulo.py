def tudo_maiusculo(msg):
    return msg.upper()

def tudo_ao_contrario(msg):
    return msg[::-1]

# variavel global
# fora do escopo de uma funcao
# Ela pode ser acessada de qualquer lugar do programa, dentro ou fora da função
# sempre tem o mesmo valor
x = "global"

def imprimir_global():
    print(f'x dentro da função: {x}')

imprimir_global()
print(f'x fora da função: {x}')


# variavel local
# Uma variável declarada dentro do corpo de uma função é conhecida como local
# Ela estará disponível apenas para ser utilizada dentro da função de definicao
def imprimir_local():
    y = "local"
    
    # x no escopo global, pode ser usada por todos os metodos
    # print(y, x) <- nesse comentario
    
    print(y)

imprimir_local()

# para fins de exemplo, note o escopo
# y fora do escopo local, nao funcionara
# print(y, x)


# quando ha necessidade de usar locais e globais...
# Nesse caso, é preciso declarar, dentro da função, a variável como global
# foi sinalizado que a variável x deve ser tratada de modo global, não local
x = 1
def imprimir():
    global x
    x += 1
    print('Python' * x)
imprimir()
print(x)
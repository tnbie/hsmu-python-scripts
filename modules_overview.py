# conjunto de funcoes, classes e variaveis
# built-in (diversos)
# conhecidos como extensoes da linguagem, para reutilizacao
# facilita o desenvolvimento de software

# bibilioteca de funcoes matematicas
import math

# importando apenas um metodo especifico
# metodo coseno
from math import cos

# importando todos os metodos disponiveis
# exemplo
# por padrao, nao e boa pratica importar tudo
from csv import *

# raiz quadrade do numero 9
# atribui a uma variavel (x)
x = math.sqrt(9)

# exibe valor
print(x)

# coseno do numero 8
# atribui a uma variavel (y)
y = math.cos(8)

# exibe valor
print(y)


import meumodulo

meumodulo.tudo_ao_contrario('Estou criando meu próprio módulo')
meumodulo.tudo_maiusculo('Estou criando meu próprio módulo')
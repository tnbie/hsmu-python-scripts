# abre um novo arquivo
file = open("compras.txt", "w")

# adiciona itens ao arquivo
file.write('Agua\n')
file.write('Arroz\n')
file.write('Detergente\n')

# fecha arquivo
file.close()

# abre arquivo novamente
file = open("compras.txt", "r")

# ler arquivo
print(file.read())

# ler primeira linha
print(file.readline())

# ler todas as linhas, retorna quebras de linhas tbm
print(file.readlines())

# fecha arquivo
file.close()

# abre arquivo novamente
file = open("compras.txt", "a")

# adiciona itens ao arquivo, sem apagar os ja existentes (a = append)
file.write('Bolacha\n')
file.write('Peixe\n')
file.write('Ovos\n')

# fecha arquivo
file.close()
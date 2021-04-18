# manipulacao de arquivos
# criar, ler, editar, e deletar

# modo simples
# 'r = read mode'
file = open("teste.txt", 'r')
print("Nome do arquivo: ", file.name)

# modo completo (endereco completo do arquivo)
# 'w' =  write mode
file = open("C:/Users/erichm/Desktop/hsmu-python-scripts/teste.txt", 'w')
print("Nome do arquivo: ", file.name)

# 'r' = read
# 'w' = write, delete content
# 'a' = write, preserve content
# 'b' = binary mode
# '+' = update (write/read)

# apos alteracoes no arquivo, sempre necessario fechar ele
file.close()
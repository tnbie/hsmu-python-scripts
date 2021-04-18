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
altura = float(input("Informe sua altura: "))
peso = float(input("Informe o seu peso: "))
imc = peso / (altura * altura)
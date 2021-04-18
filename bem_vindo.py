nome = input("Qual seu nome? ")
ano_nascimento = int(input("Qual o ano de seu nascimento? "))
ano_atual = 2020
idade = ano_atual - ano_nascimento

print('Bem vindo(a) {0}, \n Voce tem {1} anos'.format(nome, str(idade)))
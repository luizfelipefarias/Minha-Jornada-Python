#Questao errada 
 #Motivo do erro falhei no entendimento sobre a questão
print("----------------Desafio 04------------------")
 #Pedindo tipo String(char/caractere)
texto_string=input("Digite texto: ")
 #Saida
print(type(texto_string))
print("--------------------------------------------")

 #Pedindo tipo int(inteiro)
numero_int=int(input("Digite um numero: "))
 #Saida
print(type(numero_int))
print("--------------------------------------------")
 #Pedindo tipo float(Numeros reias)
numero_float=float(input("Digite um numero com ponto: "))
#Saida
print(type(numero_float))
print("--------------------------------------------")
 #Pedindo tipo bool(booleano/Verdadeiro ou Falso)
saida_bool=bool(input("Digite True or False: "))
#Saida
print(type(saida_bool))
print("--------------------------------------------")


#Questao certa
# Usando métodos como .isalpha() para "dissecar" uma variável em Python
print("----------------Desafio 04------------------")

a = input('Digite algo: ')

# Mostra o tipo primitivo (sempre str, já que vem de input())
print('O tipo primitivo desse valor é:', type(a))
print("--------------------------------------------")

# Verificações usando métodos de string
print('Só tem espaços?', a.isspace())             # True se só houver espaços
print("--------------------------------------------")
print('É um número?', a.isnumeric())              # True se for número inteiro
print("--------------------------------------------")
print('É alfabético?', a.isalpha())               # True se tiver só letras
print("--------------------------------------------")
print('É alfanumérico?', a.isalnum())             # Letras ou números, sem símbolos
print("--------------------------------------------")
print('Está em maiúsculas?', a.isupper())         # Todas as letras são maiúsculas?
print("--------------------------------------------")
print('Está em minúsculas?', a.islower())         # Todas as letras são minúsculas?
print("--------------------------------------------")
print('Está capitalizado?', a.istitle())          # Primeira letra maiúscula em cada palavra
print("--------------------------------------------")
print('É decimal?', a.isdecimal())                # True se for número decimal (sem sinais)
print("--------------------------------------------")

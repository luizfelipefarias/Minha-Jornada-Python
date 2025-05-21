print("----------------Desafio 06------------------")
#Importando um biblioteca de matematica
from math import sqrt

#ler o numero na tela
num = int(input('Digite seu numero: '))
print('-'*44)
#calcula o dobro
dobro = num*2
#calcula o triblo
triblo = num*3
#calcula a raiz quadrada sem importa nehuma biblioteca
raiz_quadrada1 = num**(1/2)

#printando na tela
print(f'O dobro do {num} é {dobro}')
print('-'*44)
print(f'O triplo do {num} é {triblo}')
print('-'*44)
print(f'A raiz quadrada do seu numero é {raiz_quadrada1:.2f}')

print('-'*44)
#Pedindo um segundo numero para usar raiz quadrada da biblioteca math
num2=int(input('Digite seu segundo numero: '))


#raiz_quadrada2=> essa parte e a variavel
#math.sqrt(num2)=> math. chama a biblioteca -->caso importou toda a biblioteca
# já sqrt(num2) =>usando a estrtura para calcular raiz
raiz_quadrada2 = sqrt(num2)

#printando na tela
print(f'-----------Raiz quadrada usando a biblioteca math------------')
print(f'{raiz_quadrada2 :.2f}')
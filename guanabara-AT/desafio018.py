#Importando da biblioteca math o sin,cos,tan
from math import sin,cos,tan,radians
#Organização
print("----------------Desafio 18------------------")

#Entrada de dados
angulo=float(input('Digite um angulo: '))
print('-' * 44)

#A biblioteca math espera o angulo digitado na entrada de dados
#em radiano-por isso essa conversão 
radiano=radians(angulo)

#Seno,Cosseno,Tangente do angulo digitado
seno=sin(radiano)
cosseno=cos(radiano)
tangente=tan(radiano)

#Saida de dados
print(f'O angulo {angulo:.2f} digitado em seno é de {seno:.2f}')
print(f'O angulo {angulo:.2f} digitado em cosseno é de {cosseno:.2f}')
print(f'O angulo {angulo:.2f} digitado em tangente é de {tangente:.2f}')

print('-' * 44)

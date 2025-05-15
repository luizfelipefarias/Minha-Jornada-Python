print("----------------Desafio 07------------------")
import statistics

#Ler o texto na tela
nota_1=float(input('Digite sua primeira nota: '))
print('-'*44)
nota_2=float(input('Digite sua segunda nota: '))
print('-'*44)

media=((nota_1+nota_2)/2)

print(f"Sua media é {media}")
print('-'*44)
nota_1=float(input('Digite sua primeira nota: '))
print('-'*44)
nota_2=float(input('Digite sua segunda nota: '))
print('-'*44)
#media=statistics.mean(nota_1,nota_2) => teste usando statistics
#statistics requer lista,tuplas e arrays
#Explicando lista :variavel=>list= recebe [variaveis]
list=[nota_1,nota_2]

#usando metodo statistics
#media => variavel
#statistics. chamando a biblioteca statistics.mean(list)->chamando o metodo de media da biblioteca statistics
media=statistics.mean(list)
print('-'*44)
print(f'Sua media é {media}')
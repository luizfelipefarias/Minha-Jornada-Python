print("----------------Desafio 13------------------")
#Entrada de dados
salario=float(input('Digite seu salrio: '))
print('-'*44)
#aumento de 15%
aumento=15
#calculando o aumento
calculando_salario=salario*aumento/100
#aplciando o aumento
novo_salario=salario + calculando_salario
#Saida de dados
print(f'O seu salrio sem aumento é de {salario:.2f} e o seu novo salario com aumento é de {novo_salario:.2f}')
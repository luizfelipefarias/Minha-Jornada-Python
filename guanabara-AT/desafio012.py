print("----------------Desafio 12------------------")

#Entrada de texto
produto=float(input('Digite o preço do seu produto: R$: '))
print('-'*44)

#desconto de 5%
DESCONTO=5

#calculo para descobrir o desconto
calculando_desconto=((produto*DESCONTO)/100)

#apliacando o desconto
valor= produto - calculando_desconto

#pritando o valor
print(f'O valor do seu produto com desconto é de {valor:.2f}')
print('-'*44)

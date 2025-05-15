print("----------------Desafio 12------------------")
#Entrada de texto
produto=float(input('Digite o preço do seu produto: '))
print('-'*44)

#desconto de 4%
desconto=5
#calculo para descobrir o desconto
calculando_desconto=((produto*desconto)/100)
#apliacando o desconto
valor= produto - calculando_desconto

print('-'*44)
#pritando o valor
print(f'O valor do seu produto é de {valor:.2f}')
print('-'*44)

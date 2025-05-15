print("----------------Desafio 14------------------")

#Entrada de dados
celsius=float(input('Digite a temperatura em graus Celsius:'))
print('-'*44)
#Calculo para converte celsius em fahrenheit
conversor_para_fahrenheit = (celsius*1.80)+32

#Saida de dados
print(f'A sua temperatura em Celsius é de {celsius:.2f}°C ')
print(f'Sua temperatura convertida em fahrenheit {conversor_para_fahrenheit:.2f}°F')
print('-'*44)
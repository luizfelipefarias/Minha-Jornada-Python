print("----------------Desafio 11------------------")
#Entrada de texto
largura=float(input('Qual a largura da parede: '))
print('-'*44)
altura=float(input('Qula a altura da parede: '))

#quantidade da tinta
tinta=2
#calculando area
area=altura*largura

print('-'*44)
#printando area
print(f'A area de sua parede é de {area:.2f}')

#calculando gastos de tinta
litros=area/2

#printando gastos de tinta
print('-'*44)
print(f'Você vai gastar {litros:.2f} litros de tinta por area de {area}')
print('-'*44)
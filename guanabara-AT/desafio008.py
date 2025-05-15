print("----------------Desafio 08------------------")
#Ler o codigo na tela
metros=float(input('Digite seu valor em metros: '))
print('-'*44)

#conversor de Unidades de comprimento
mm=metros*1000
cm=metros*100
dm=metros*10
m=metros
dam=metros/10
hec=metros/100
km=metros/1000

#printando na tela
print(f'Seu valor em milimetros é {mm:.0f}')
print(f'Seu valor em centimentros é {cm:.0f}')
print(f'Seu valor em decimentros é {dm:.0f}')
print(f'Seu valor em metros é {m:.0f}')
print(f'Seu valor em decâmetro é {dm:.0f}')
print(f'Seu valor em  hectômetro é {hec:.0f}')
print(f'Seu valor em kilometros é {km:.0f}')
print('-'*44)
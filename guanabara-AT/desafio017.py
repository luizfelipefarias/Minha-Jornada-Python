# Importando da biblioteca math a função hypot
from math import hypot

# Entrada de dados
print("----------------Desafio 17------------------")
cateto_adjacente = float(input('Digite o cateto adjacente: '))
cateto_oposto = float(input('Digite o cateto oposto: '))
print('-' * 44)
# Usando hypot(cateto_adjacente, cateto_oposto) para calcular a hipotenusa
hipotenusa = hypot(cateto_adjacente, cateto_oposto)

# Saída de dados
print(f'O valor da hipotenusa é: {hipotenusa:.2f} m')
print('-' * 44)

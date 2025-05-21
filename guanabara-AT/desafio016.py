# Importando da biblioteca math o floor
from math import floor


print("----------------Desafio 16------------------")
# Entrada de dados
num = float(input('Digite um número: '))
print('-' * 44)
# Arredonda o número para baixo (parte inteira inferior)
inteiro = floor(num)

# Saída de dados
print(f'O número {num} arredondado para baixo é {inteiro}')
print('-' * 44)

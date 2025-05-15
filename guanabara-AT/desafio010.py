print("----------------Desafio 10------------------")
# Entrada de texto
dinheiro = float(input('Digite quanto você tem na carteira: R$: '))

# Valor da cotação atual/constante
DOLAR = 5.66
EURO = 6.33

# Calculando o valor
conversor_dolar = dinheiro / DOLAR
conversor_euro = dinheiro / EURO

print('-' * 44)
# Saída de texto
print(f'Seu valor em dólar é de: $ {conversor_dolar:.2f}')
print(f'Seu valor em euro é de: € {conversor_euro:.2f}')
print('-' * 44)

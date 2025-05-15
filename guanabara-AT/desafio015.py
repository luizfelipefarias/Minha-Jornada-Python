print("----------------Desafio 15------------------")

# Entrada de dados
km_percorridos = float(input("Quantos quilômetros foram percorridos pelo carro alugado: "))
print('-' * 44)
dias_alugados = int(input("Quantos dias o carro foi alugado: "))

# Constantes
DIA = 60
KM = 0.15

# Cálculos
custo_dias = dias_alugados * DIA
custo_km = km_percorridos * KM
custo_total = custo_dias + custo_km

# Saída de dados
print('-' * 44)
print(f"O custo do aluguel com base nos {dias_alugados} dias foi de R$ {custo_dias:.2f}")
print(f"O custo dos quilômetros rodados foi de R$ {custo_km:.2f}")
print(f"O custo total a pagar é de R$ {custo_total:.2f}")
print('-' * 44)

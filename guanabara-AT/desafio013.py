print("----------------Desafio 13------------------")

# Entrada de dados
salario = float(input("Digite seu salário: R$ "))
print("-" * 44)

# Porcentagem de aumento
AUMENTO = 15

# Calculando o novo salário
novo_salario = ((salario * AUMENTO) / 100)

salario_aumento=salario + novo_salario

# Saída de dados
print(f"O seu salário sem aumento é de R$ {salario:.2f} ")
print(f'O seu novo salário com aumento de {AUMENTO}% é de R$ {salario_aumento:.2f}')
print("-" * 44)

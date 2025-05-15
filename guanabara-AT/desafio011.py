print("----------------Desafio 11------------------")

# Entrada de texto
largura = float(input("Qual a largura da parede (em metros): "))
altura = float(input("Qual a altura da parede (em metros): "))

# Quantidade de tinta necessária (2m² por litro)/constante
TINTA = 2

# Calculando a área
area = altura * largura

print("-" * 44)
# Exibindo a área
print(f"A área da sua parede é de {area:.2f} m²")

# Calculando o gasto de tinta
litros = area / TINTA

# Exibindo o gasto de tinta
print("-" * 44)
print(f"Você vai gastar aproximadamente {litros:.2f} litros de tinta para pintar {area:.2f} m²")
print("-" * 44)

from random import choice
# Organização
print("----------------Desafio 19 ------------------")

# Entrada de dados
aluno1 = input('Digite o nome do primeiro aluno: ')
print('-' * 44)
aluno2 = input('Digite o nome do segundo aluno: ')
print('-' * 44)
aluno3 = input('Digite o nome do terceiro aluno: ')
print('-' * 44)
aluno4 = input('Digite o nome do quarto aluno: ')

# O choice da biblioteca só aceita em lista e tuplas
lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]

# Usando o choice para sortear um dos 4 alunos
sorteando = choice(lista_de_alunos)

print('-' * 44)

# Saída de dados
# Usando o ",".join(lista_de_alunos) dentro do f-string para unir a lista no print
print(f'No total de 4 alunos, sendo eles: {", ".join(lista_de_alunos)}')
print(f'Foi sorteado o aluno {sorteando}')
print('-' * 44)

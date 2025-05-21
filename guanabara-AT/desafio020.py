from random import choice, shuffle

print("----------------Desafio 20 ------------------")

# Entrada de dados
aluno1 = input('Digite o nome do primeiro aluno: ')
print('-' * 44)
aluno2 = input('Digite o nome do segundo aluno: ')
print('-' * 44)
aluno3 = input('Digite o nome do terceiro aluno: ')
print('-' * 44)
aluno4 = input('Digite o nome do quarto aluno: ')

lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]

# Sorteio e embaralhamento
sorteado = choice(lista_de_alunos)
shuffle(lista_de_alunos)

# Saída de dados
print('-' * 44)
print(f'No total de 4 alunos: {", ".join(lista_de_alunos)}')
print(f'Aluno sorteado: {sorteado}')
print(f'Ordem de apresentação: {", ".join(lista_de_alunos)}')
print('-' * 44)

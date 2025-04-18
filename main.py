import random

"""
Desenvolver uma solução baseada em algoritmos genéticos 
para maximizar o valor total de itens inseridos em uma 
mochila com limite de peso de 15 kg, utilizando seleção 
por roleta e representações binárias.
"""
# a mochila tem limite de 15 kg e os 10 itens são os seguintes:
limitWeight = 15  # peso maximo
items = [ #id, peso e valor
    {"id": "A", "weight": 2, "value": 40},
    {"id": "B", "weight": 3, "value": 50},
    {"id": "C", "weight": 4, "value": 65},
    {"id": "D", "weight": 5, "value": 80},
    {"id": "E", "weight": 7, "value": 110},
    {"id": "F", "weight": 1, "value": 15},
    {"id": "G", "weight": 6, "value": 90},
    {"id": "H", "weight": 4.5, "value": 70},
    {"id": "I", "weight": 3.5, "value": 60},
    {"id": "J", "weight": 2.5, "value": 55}
]
"""
===============================================================================================
o objetivo é seguir os seguintes passos:
nova população -> popupulação inicial -> seleção -> crossover -> mutação -> nova população...
o cromossomo vai ser representado como um vetor de 0s e 1s, seguindo a ordem dos itens de cima
[0, 1, 1...] -> item B e C, e assim por diante
FUNÇÃO OBJETIVO: 
Maximizar o valor, sujeito ao peso máximo de 15 kg
===============================================================================================
"""
# P1 - População inicial, tamanho 50 individuos
def check_if_valid(cromossome):
  total = 0
  for i in range(len(cromossome)): # vou percorrendo o cromossomo
    if cromossome[i] == 1: # se for necessario contar o peso
      total += items[i]["weight"] # somo o peso do item
  print(total <= limitWeight) # TESTE PRA VER SE ELE É FACTIVEL 
  return total <= limitWeight # se estourar o peso ele nao eh factivel


def generate_initial_population(population_size, num_items):
  population = [] # popul. como vazia
  for _ in range(population_size): # Faço um for pra preencher, a depender do tamanho que passei lá embaixo
    cromossome = [random.randint(0, 1) for _ in range(num_items)] # for pra gerar cromossomos
    check_if_valid(cromossome) # testo se ele passa no teste de peso (factivel)
    while not check_if_valid(cromossome): # enquanto o cromossomo nao passar na funcao eu vou gerar outro
      cromossome = [random.randint(0, 1) for _ in range(num_items)]
    population.append(cromossome) # se tiver tudo ok eu adiciono ele na populacao
  return population

# Gerar a população inicial
size = 50 #definido no enunciado da questao
num_items = len(items) # tenho que pegar o "n", qtd de itens do problema
population = generate_initial_population(size, num_items)
# PRINT DE TESTES
# for individual in population:
#     print(individual)


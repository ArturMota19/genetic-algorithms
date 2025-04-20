import random

"""
Desenvolver uma solução baseada em algoritmos genéticos 
para maximizar o valor total de itens inseridos em uma 
mochila com limite de peso de 15 kg, utilizando seleção 
por roleta e representações binárias.
"""
# a mochila tem limite de 15 kg e os 10 itens são os seguintes:
limitWeight = 15  # peso maximo
generations = 200 # numero de geracoes

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
# Helpers para ajudar nos passos
def check_if_valid(cromossome):
  total = 0
  for i in range(len(cromossome)): # vou percorrendo o cromossomo
    if cromossome[i] == 1: # se for necessario contar o peso
      total += items[i]["weight"] # somo o peso do item
  return total <= limitWeight # se estourar o peso ele nao eh factivel

def check_best(population):
  best = 0 # maximo de valor
  best_cromossome = [] # melhor cromossomo
  for cromossome in population:
    total = 0 # valor total
    for i in range(len(cromossome)):
      if cromossome[i] == 1:
        total += items[i]["value"]
    if total > best:
      best = total
      best_cromossome = cromossome
  return best_cromossome, best # retorna o melhor cromossomo e o valor total dele
  

# P1 - População inicial, tamanho 50 individuos
def generate_initial_population(population_size, num_items):
  population = [] # popul. como vazia
  for _ in range(population_size): # Faço um for pra preencher, a depender do tamanho que passei lá embaixo
    cromossome = [random.randint(0, 1) for _ in range(num_items)] # for pra gerar cromossomos
    check_if_valid(cromossome) # testo se ele passa no teste de peso (factivel)
    while not check_if_valid(cromossome): # enquanto o cromossomo nao passar na funcao eu vou gerar outro
      cromossome = [random.randint(0, 1) for _ in range(num_items)]
    population.append(cromossome) # se tiver tudo ok eu adiciono ele na populacao
  return population

# faço seleção por roleta
# a ideia é que os individuos mais fortes tenham mais chances de serem selecionados
# P2 - Seleção por roleta
def roulette_selection(population):
  fitness = []  # lista de fitness para cada cromossomo
  for cromossome in population:
    # pra cada cromossomo, vou calcular o valor total dele
    total_value = 0
    for i in range(len(cromossome)):
      gen = cromossome[i] # pego o gen do cromossomo
      if gen == 1:
        total_value += items[i]["value"]
    fitness.append(total_value)

  total_fitness = sum(fitness)  # soma total dos fitness
  probabilities = []
  for f in fitness:
    if total_fitness == 0: # se o fitness total for 0, a probabilidade vai ser 0
      probabilities.append(0)
    else:
      probabilities.append(f / total_fitness) # probabilidade proporcional ao fitness
      # vai ser proporcional pq se o fitness for maior, a probabilidade de ser selecionado vai ser maior tbm
      # se o fitness de um cromossomo for 30 e o total for 100, ele vai ter 0.3 de 1.0 de chance de ser escolhido
  selected = []
  for _ in range(len(population)):
    r = random.uniform(0, 1)  # número aleatório entre 0 e 1
    cumulative = 0
    for i in range(len(probabilities)): # vou percorrer a lista de probabilidades
        cumulative += probabilities[i]
        # vou somando as probabilidades, e quando o numero aleatorio for menor que a soma, eu seleciono
        # a chance de selecionar um individuo vai ser proporcional ao fitness dele
        if r <= cumulative:
          selected.append(population[i])
          break
  return selected

# P3 - Crossover
# preciso definir o ponto de crossover, e fazer a troca dos genes entre os dois individuos
def one_crossover(parent1, parent2):
  # Ponto de crossover entre 1 e 2 (documento)
  crossover_point = random.randint(1, len(parent1) - 1) # ponto de crossover aleatorio entre 1 e o tamanho do cromossomo -1
  child1 = parent1[:crossover_point] + parent2[crossover_point:] # o primeiro filho vai ser a parte do pai 1 e a parte do pai 2
  child2 = parent2[:crossover_point] + parent1[crossover_point:] # o segundo filho vai ser a parte do pai 2 e a parte do pai 1
  return child1, child2 

def two_crossover(parent1, parent2):
  # Dois pontos de crossover
  p1 = random.randint(1, len(parent1) - 2)  # primeiro ponto entre 1 e len-2
  p2 = random.randint(p1 + 1, len(parent1) - 1)  # segundo ponto entre p1+1 e len-1
  child1 = parent1[:p1] + parent2[p1:p2] + parent1[p2:] # o primeiro filho vai ser a parte do pai 1, pai 2 e pai 1
  child2 = parent2[:p1] + parent1[p1:p2] + parent2[p2:] # o segundo filho vai ser a parte do pai 2, pai 1 e pai 2
  return child1, child2

def mutate(cromossome, mutation=0.05):
  # tentando fazer mutação com 5%
  for i in range(len(cromossome)): # percorro o cromossomo todo
    if random.random() < mutation: # se eu realmente tiver que fazer a mutação
      cromossome[i] = 1 - cromossome[i] # troco o gene. 0 vira 1 e 1 vira 0
  return cromossome


# Gerar a população inicial
size = 50 # definido no enunciado da questao
best = [] # vou guardar os melhoires cromossomos por geração, pra fazer o gráfico dps
num_items = len(items) # tenho que pegar o "n", qtd de itens do problema

population = generate_initial_population(size, num_items) # gero a populacao inicial, que vai entrar pras gerações
for generation in range(generations):
  # faço a seleção, pra pegar os caras ali de cima
  selected = roulette_selection(population)
  # agora vai ser o cruzamento (crossover)
  new_generation = [] # nova geração
  
  for _ in range(int((size * 0.8 // 2))): # 80% da população vai ser gerada por crossover
    p1 = random.choice(selected) # seleciono um pai aleatorio
    p2 = random.choice(selected) # seleciono outro pai aleatorio
    # crossover entre os dois pais, vou usar o one crossover mesmo, de um ponto
    c1, c2 = one_crossover(p1, p2)
    # faço a mutação nos filhos
    c1 = mutate(c1)
    c2 = mutate(c2)
    # adiciono os filhos na nova geração
    if check_if_valid(c1): # se o filho for valido, adiciono na nova geracao
      new_generation.append(c1)
    if check_if_valid(c2):
      new_generation.append(c2)
  
  # agora so completar com o que restou da geração anterior
  while len(new_generation) < size: # enquanto a nova geração tiver tamanho menor que 50
    # adiciono os individuos da geração anterior
    new_generation.append(random.choice(population))
  
  # agr vou salvar o melhor da geração pra usar no grafico de convergencia
  best_cromossome, best_value = check_best(new_generation) # pego o melhor cromossomo e o valor dele
  best.append(best_value) # adiciono o valor dele na lista de melhores
  
  population = new_generation # a nova geração vai ser a população agora
  print(best_value)
  
  


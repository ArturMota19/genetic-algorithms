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
# o objetivo é seguir os seguintes passos:
# nova população -> popupulação inicial -> seleção -> crossover -> mutação -> nova população...
# o cromossomo vai ser representado como um vetor de 0s e 1s, seguindo a ordem dos itens de cima
# [0, 1, 1...] -> item B e C, e assim por diante

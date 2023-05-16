




minha_tupla = ("leite", 3.00, "bike", 120.00, "feijao", 8.00, 'farinha', 4.00, 'suco', 1.00)

for i in range(0, len(minha_tupla), 2):
    print(f'{minha_tupla[i]:.<10}{"."*20}R$ {minha_tupla[i+1]:>8.2f}')

def area(a, l):
    d = a * l
    print(f'A dimensao do terreno é {d:.2f}m²')

def enfeite():
    print('-='*30)

enfeite()
print('DEFININDO AREA')
enfeite()
c = float(input('Qual primeira medida do terreno?'))
print(f'A primeira medida é {c}m')
b = float(input('Qual segunda medida do terreno?'))
print(f'A segnda medida é {b}m')
enfeite()
area(c, b)

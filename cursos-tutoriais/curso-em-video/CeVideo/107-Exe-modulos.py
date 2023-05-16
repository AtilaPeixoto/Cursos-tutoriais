from Modulos_exercicios.pacCeV import ModuloMoeda
from Modulos_exercicios.pacCeV import dados


M = ModuloMoeda
# nao pode haver nmeros, aomenos na inicio
# a formatação e designer deve ser a ultima função/ ou externa a ser chamada
# em outro caso primeira ela nao sera executada.

x = dados.verint()




#p = ModuloMoeda.moeda(ModuloMoeda.dobro(x), des=True)
# resolvi a questao chamano a formatação dentro e cada função, quando True, direto no modulo das funções
# este explo abixo mostra como nao funciona a formatação, apenas pela ordem de execução das funçoes
# d = ModuloMoeda.diminuir(ModuloMoeda.moeda(x, des=True))

dados.leiaDados(M.diminuir(x, des=True), M.aumentar(x, des=True), M.dobro(x, des=True))

# print(f'{x:#^40.3f}') # ACEITA NUMEROS LETRAS E SIMBLOS POEM NAO É POSSIVEL MISTURAR, PARA DESIGNER

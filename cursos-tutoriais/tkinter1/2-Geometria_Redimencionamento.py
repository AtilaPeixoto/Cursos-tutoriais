from tkinter import *


janela = Tk()
janela.title('title')

# Tamanho
janela.geometry('500x250+200+200')

# o booleano se refera a largra e altura e dira para onde ela se redimencionará
janela.resizable(True, False)
# icone ao loda do title
# janela.iconbitmap('caminho/icon.icon')

# define limites para dimençoes max e min
# sem o max se expandirá na tela toda
janela.minsize(500, 250)
janela.maxsize(700, 400)

# # executa minimizada
# janela.state('iconic')

# # executa maximizada
# janela.state('zoonmed')

janela.mainloop()
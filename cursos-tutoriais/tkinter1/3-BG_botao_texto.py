from tkinter import *


janela = Tk()
janela.title('title')

janela.geometry('500x250')


# alterando background
janela['bg'] = 'blue'


btn = Button(janela, text='texto do botao',)
# o btn so aparecerá com uma função agregada 
btn.pack()
# como nao foi expecificado onde o btn deve aparecer, aparecerá no topo da janela

janela.mainloop()
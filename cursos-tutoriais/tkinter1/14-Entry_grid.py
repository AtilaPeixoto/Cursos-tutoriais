# ver pygubu - para desenhar layout no tkinter
# é uma interface que substitui as linhas de cod?! salva em .ui abre em xml, quando aberto fora da interface.

from tkinter import *

janela = Tk()
janela.title('title')



Label(janela, text='Usuario').grid(row=1)
Label(janela, text='Senha').grid(row=2)

texto_usuario = Entry(janela).grid(row=1, column=1)
texto_senha = Entry(janela).grid(row=2, column=1)


login = Button(janela, text='Login').grid(row=3, column=2)


janela.mainloop()
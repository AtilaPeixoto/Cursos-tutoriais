from tkinter import *


janela = Tk()
janela.title('title')

janela.geometry('500x250')

Label_1 = Label(janela, text= 'meu texto')


Label_2 = Label(janela, text= 'meu texto')

btn = Button(janela, text='Executar', command=lambda:'')


# sequencia do pack() diz a ordem de apresentação
btn.pack()
Label_2.pack()
Label_1.pack()


janela.mainloop()
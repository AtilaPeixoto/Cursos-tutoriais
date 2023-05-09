from tkinter import *


def funcao():
    var.set(f'teu nome é {texto_1.get()}')

janela = Tk()
janela.title('stringVar')

var = StringVar()



label_1 = Label(janela, text='Escreva seu nome: ')
texto_1 = Entry(janela)
label_2 = Label(janela, textvariable=var)
btn = Button(janela, text='Executar', command=funcao)



label_1.grid(row=0, column=0)
texto_1.grid(row=0, column=1)
label_2.grid(row=2, column=0)
btn.grid(row=1, column=0)






janela.mainloop()
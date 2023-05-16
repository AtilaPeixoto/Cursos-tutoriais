from tkinter import *


janela = Tk()
janela.title('title')


janela.geometry('500x300')

# a tendencia do app é centralizar o texto no label a menos que seja dado alinhamento
label = Label(janela, text='texto\ntexto\ntexto',
              bd=1, relief='solid',
              font='arial 12 italic',
              width=7, height=2
              
              ).pack()


label = Label(janela,)
label.pack()

# para alinhar o label ussamos os pontos cardeais, tomos os 8 ponto, os 4 principais e os 4 secundarios
# ingles e letras maiusculas o atributo é o anchor
label = Label(janela, text='texto',
              bd=1, relief='solid',
              font='arial 12 italic',
              width=7, height=5,
              anchor=NE
              ).pack()



janela.mainloop()
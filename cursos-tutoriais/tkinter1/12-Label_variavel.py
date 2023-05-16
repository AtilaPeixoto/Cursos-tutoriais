from tkinter import *


janela = Tk()
janela.title('title')

janela.geometry('500x300')


texto = StringVar()
texto.set('novo texto')

# quando usado a stringvar é preciso usar o atributo textvar dentro do label
# caso nao o sistema nao reconhece a variavel
label = Label(janela, text=texto, 
              font='arial 10 italic',
              bd=5, relief='solid')

label.pack()

label_2 = Label(janela, textvariable=texto,
                bd=2, relief='solid').pack()


janela.mainloop()
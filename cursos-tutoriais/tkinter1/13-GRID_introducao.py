from tkinter import *

janela = Tk()
janela.title('title')

# se nao houver a dimenssao da janela quem define o tamanho da tea sera a aplicação
#janela.geometry('500x300')


label = Label(janela, text='texto',
              bd=2, relief='solid',)

label_1 = Label(janela, text='texto dois',
              bd=2, relief='solid',)

label.grid(row=2, column=3)
label_1.grid(row=1, column=0)

# ==========================

label_2 = Label(janela, text='text', bd=2, relief='groove')
label_3 = Label(janela, text='text', bd=2, relief='groove')
label_4 = Label(janela, text='text', bd=2, relief='groove')

btn_ = Button(janela, text='botao')
btn_1 = Button(janela, text='botao')
btn_2 = Button(janela, text='botao')

label_2.grid(row=3, column=0)
label_3.grid(row=3, column=1)
label_4.grid(row=3, column=2)

btn_.grid(row=4, column=0)
btn_1.grid(row=4, column=1)
btn_2.grid(row=4, column=2)



janela.mainloop()

'''
GRID é uma matriz, uma grade
o ponto suerior esquerdo é o ponto zero zero de X e Y/linha e coluna
row= 0, column=0 e segue...'''
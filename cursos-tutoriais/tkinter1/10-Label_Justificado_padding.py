from tkinter import *

janela = Tk()
janela.title('title')

janela.geometry('500x300')

# o pad refere-se a distancia entre o texto e a fronteira do label
label = Label(janela, text='texto',
              font='arial 20 italic',
              bd=1, relief='groove',
              pady=50, padx=20,
             
              )
label.pack()

# o justify alinha o texto dentro do label
# neste caso a fronteira do label esta definida pelo proprio conteudo
label = Label(janela, text='texto',
              font='arial 20 italic',
              bd=1, relief='groove',
             
              justify='right'
              )
label.pack()

# perceba nao funcionar quando definimos uma altura e largura para o label, isso
# acontece por, neste caso, o alinhamento ser ditado pelo anchor e os pontos cardeais 
label = Label(janela, text='texto',
              font='arial 20 italic',
              bd=1, relief='groove',
              width=10, height=2,
              justify='right'
              )
label.pack()

label = Label(janela, text='texto',
              font='arial 20 italic',
              bd=1, relief='groove',
              width=10, height=2,
              anchor=E
              )
label.pack()


janela.mainloop()
from tkinter import *

janela = Tk()
janela.title('title')

janela.geometry('500x250')

#o backgroud aqui afeta apenas o fundo do label. fg=fonteground
label_1  = Label(janela, text='texto do label',
                 bg='red', fg='black',
                 font='arial',
                 width='50'
                 )
# perceba qu o widhtaqui é referente ao label nao ao que esta no label 
label_1.pack()

# atenção aos atributos de fonte e seu formato
label_2  = Label(janela, text='texto do label',
                 bg='red', fg='black',
                 font='times 20 bold italic',
                 
                 )
label_2.pack()


#os atributos bg e ft podem ser nos moldes rgb '#000000'
'''no modelo RGB
os doi sprimeiros valores sao para red
dois para green
dois para blue
'''

janela.mainloop()
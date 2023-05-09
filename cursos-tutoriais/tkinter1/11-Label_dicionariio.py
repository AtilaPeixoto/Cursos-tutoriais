from tkinter import *
janela = Tk()
janela.title('title')

janela.geometry('500x300')

# maneira tradicional
label = Label(janela, text='texto', )
label.pack()


# perceba a forma de reatribuiçao de texto possivel, mesmo apos o pack()
label3 = Label(janela, text='texto', )
label3.pack()

label3['text'] = 'palavra'



# ha esta outra forma, usando de dicionario, para fazer tbm
label2 = Label(janela)
label2['text'] = 'texto'
label2['font'] = 'ariel 20 italic'
label2['bg'] = 'red'
label2.pack()


# # esta é uma forma interessante de visualizar as propriedades que podem ser alteradas
# # é claro aparecerao no terminal
# # perceba que esta antes da execução do loop da janela
# for i in label2.keys():
#     print(i,':', label2[i])
    

    
janela.mainloop()

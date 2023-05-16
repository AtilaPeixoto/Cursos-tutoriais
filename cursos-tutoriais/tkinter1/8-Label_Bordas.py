from tkinter import *

janela = Tk()
janela.title('title')

janela.geometry('500x700')

# é possivel usar 3 aspas ou 
label = Label(janela, text='''texto na linha um
              outra linha''',
              font='arial',
              bg='red',
           
              )
label.pack()


# atenção a quantidade de \n sera o numero de linhas 
label = Label(janela, text='texto na linha um \n\n outra linha',
              font='arial',
              bg='red',
              
              )
label.pack()

# para adcionar a borda é preciso do atributo relief
# sao 6 apresentações do relief:
# solid
# flat
# raised
# groove
# sunken
# ridge
label = Label(janela, text='texto ',
              font='arial 20 ',
              bg='red',
              bd=10, relief='solid',
              )
label.pack()
label = Label(janela, text='texto ',
              font='arial 20 ',
              bg='red',
              bd=10, relief='flat',
              )
label.pack()
label = Label(janela, text='texto ',
              font='arial 20 ',
              bg='red',
              bd=10, relief='raised',
              )
label.pack()
label = Label(janela, text='texto ',
              font='arial 20 ',
              bg='red',
              bd=10, relief='groove',
              )
label.pack()
label = Label(janela, text='texto ',
              font='arial 20 ',
              bg='red',
              bd=10, relief='sunken',
              )
label.pack()
label = Label(janela, text='texto ',
              font='arial 20 ',
              bg='red',
              bd=10, relief='ridge',
              )
label.pack()


janela.mainloop()
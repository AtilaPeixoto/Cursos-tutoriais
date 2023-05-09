from tkinter import *

root = Tk()
root.title('texto')
# root.geometry('500x300)

def ver_valor():
    print(valor_1.get())
    

def evento():
    print('evento do radeobutton determinado')


valor_1 = IntVar()


# diferente das checkbox o radeobutton pode-se marcar apenas uma opcao
rb_1 = Radiobutton(root, text='Opcao a 1', variable=valor_1, value=1, command=evento)
rb_2 = Radiobutton(root, text='Opcao a 2', variable=valor_1, value=2,)
rb_3 = Radiobutton(root, text='Opcao a 3', variable=valor_1, value=3)

# modelo diferente para selecao/ o indicatoron é bolleana
rb_4 = Radiobutton(root, text='Opcao a 4', variable=valor_1, value=4, indicatoron=0)
rb_5 = Radiobutton(root, text='Opcao a 5', variable=valor_1, value=5, indicatoron=0)


btn = Button(root, text='executar', command=ver_valor)



# sdeixando uma opcao selecionada
rb_2.select()

rb_1.grid()
rb_2.grid()
rb_3.grid()
btn.grid()
rb_4.grid()
rb_5.grid()






root.mainloop()
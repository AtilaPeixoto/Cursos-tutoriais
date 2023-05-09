from tkinter import *

root = Tk()
root.title('texto')
# root.geometry('500x300)

frameA = Frame(root)
frameB = Frame(root)

def ver_valor():
    print(valor_1.get())
    

def evento():
    print('evento do radeobutton determinado')


valor_1 = IntVar()
valor_2 = IntVar()


# diferente das checkbox o radeobutton pode-se marcar apenas uma opcao
rb_1 = Radiobutton(frameA, text='Opcao A 1', variable=valor_1, value=1, command=evento)
rb_2 = Radiobutton(frameA, text='Opcao A 2', variable=valor_1, value=2,)
rb_3 = Radiobutton(frameA, text='Opcao A 3', variable=valor_1, value=3)

# modelo diferente para selecao/ o indicatoron é bolleana
rb_4 = Radiobutton(frameB, text='Opcao B 1 ', variable=valor_2, value=4, indicatoron=0)
rb_5 = Radiobutton(frameB, text='Opcao B 2', variable=valor_2, value=5, indicatoron=0)
rb_6 = Radiobutton(frameB, text='Opcao B 3', variable=valor_2, value=6, indicatoron=0)


btn = Button(root, text='executar', command=ver_valor)



# sdeixando uma opcao selecionada
rb_2.select()


# FRAME 1
rb_1.grid()
rb_2.grid()
rb_3.grid()
btn.grid(row=1, column=0)
frameA.grid(row=0, column=0)


# FRAME 2
rb_4.grid()
rb_5.grid()
rb_6.grid()
frameB.grid(row=0, column=1)


'''
interessante: se o valor de variable for o mesmo, mesmo estando em frames diferentes
o sistema funciona como um.
A independencia de cada depende de, no caso referido, valore diferentes.
'''



root.mainloop()
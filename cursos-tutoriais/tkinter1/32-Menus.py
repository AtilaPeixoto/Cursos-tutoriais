from tkinter import *

root = Tk()
root.title('titulo')

root.geometry('500x400')


def novo():
    print('novo')


menu_1 = Menu(root)
root.config(menu=menu_1)
# # funcionaria apenas caso nao houvesse subopcaoes. Como temos nao ha razao para usar este metodo
# menu_1.add_command(label='File', )
# menu_1.add_command(label='Edit )


# =====================================================
# File
fileMenu = Menu(menu_1, tearoff=0)
fileMenu.add_command(label='Open')
fileMenu.add_command(label='New', command=novo)
fileMenu.add_command(label='SAVE')
fileMenu.add_separator()
fileMenu.add_command(label='Exit')
menu_1.add_cascade(label='File', menu=fileMenu)



# =====================================================
# Edit
editMenu = Menu(menu_1, tearoff=0)
editMenu.add_command(label='Copy')
editMenu.add_command(label='Paste')
editMenu.add_command(label='Select')
menu_1.add_cascade(label='Edit', menu=editMenu)



'''
interessante e util:
sem a opecao tearOff o menu torna-se movel, podendo ser deslocado da caixa principal.
Em geral nao queremos isso, entao usamos a opcao.
'''



root.mainloop()

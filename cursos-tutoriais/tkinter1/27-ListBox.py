from tkinter import *

root = Tk()
root.title('title')


def executar():
    print(lista.get(ACTIVE))


lista = Listbox(root)
lista.pack()

# posicao - item
lista.insert(0, 'item um ')
lista.insert(END, 'item 2')
lista.insert(END, 'item 3')

lista_1 = ['tarcisio', 'carlos', 'marcio']
for item in lista_1:
    lista.insert(END, item)

# # excluindo itens de listabox
# # item inicial e item final
# lista.delete(2,2)
# lista.delete(0,END)

btn = Button(root, text='executar', command=executar).pack()

root.mainloop()


'''ha muitas funcoes extrar e funcionalidade e aplicaçoes para isto porem o curso é gratuito'''
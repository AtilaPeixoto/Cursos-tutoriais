from tkinter import *


root = Tk()
root.title('titulo')

root.geometry('500x400')


def abrirAgregada():
    # top level é uma janela separada da janela principal
    top = Toplevel()
    top.title('titulo da agregada')
    top.geometry('200x200')
    lbl = Label(top, text='label na janela')
    top.grid()



btn = Button(root, text='Abrir agregada', command=abrirAgregada)
btn.grid()

root.mainloop()
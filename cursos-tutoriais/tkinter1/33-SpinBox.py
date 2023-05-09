from tkinter import *

root = Tk()
root.title('titulo')

root.geometry('200x200')

def exe():
    print(spin_1.get())
    print(spin_2.get())
    print(spin_3.get())
    print(spin_4.get())

spin_1 = Spinbox(root, from_=0, to=10)
spin_2 = Spinbox(root, values=(19, 39 , 47, 10))
# a opcao wrap permite que a spin rode ara cima e ou para baixo logo no inicio
spin_3 = Spinbox(root, values=('air', 'bus' ,'carro', 'moto'), wrap=True)
spin_4 = Spinbox(root, values=('air', 'bus' ,'carro', 'moto'))

btn = Button(root, text='executar', command=exe)


spin_1.grid()
spin_2.grid()
spin_3.grid()
spin_4.grid()
btn.grid()


root.mainloop()
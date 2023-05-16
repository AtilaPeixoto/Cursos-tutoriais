from tkinter import *


# ==================================================
# GUI
root = Tk()
root.title('nao precisa disso')

root.geometry('700x500')


# ==================================================
# Funcoes

def exe(valor):
    print(valor)
    
def exe2():
    var.set(slide_btn.get())
    

var = StringVar()


# ==================================================
# widget

# COMO O FROM É PALAVRA RESERVADA DO PYTHON PARA IMPORTAÇÃO HA A NECESSIDADE DO _ NO FROM DO TKINTER
slide_1 = Scale(root, from_=0, to=400, bg='red', troughcolor='blue')
slide_2 = Scale(root, from_=0, to=100, length=300, background='green', takefocus='naome')
slide_3 = Scale(root, from_=0, to=400, highlightbackground='blue')

# enviando valor para terminal
# slider_len tamanho da barrinha na barra
slide_exe = Scale(root, from_=0, to=50, resolution=0.5, sliderlength=5 , command=exe)

# do botao
slide_btn = Scale(root, from_=0, to=100, orient=HORIZONTAL, label='Mexa na barra e use o botao')
b = Button(root, text='executar', command=exe2)
label = Label(root, textvariable=var)

# ==================================================
# layout
slide_1.grid(row=0, column=0)
slide_2.grid(row=0, column=1)
slide_3.grid(row=0, column=3)
slide_exe.grid(row=0, column=2)
slide_btn.grid(row=2, column=1)
b.grid(row=3, column=1)
label.grid(row=4, column=1)



# fim
root.mainloop()
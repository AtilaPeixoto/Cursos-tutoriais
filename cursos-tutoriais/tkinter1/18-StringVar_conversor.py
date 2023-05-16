from tkinter import *


# funçao ==================
def converter():
    f = float(graus.get())
    c = (f - 32) * 5/9
    #final.set(str(c))
    final.set(f'{str(round(c))} Graus celsius')
    
    
# GUI ===============================
janela = Tk()
janela.title('Conversor Fahrenheit To Celsius')
final = StringVar()


# widget ===================
label_1 = Label(janela, text='Graus Fahrenheit')
label_2 = Label(janela, textvariable=final)

graus = Entry(janela, )

btn = Button(janela, text='Converter', command=converter)


# layout =========================

label_1.grid(row=0)
graus.grid(row=1)
label_2.grid(row=2)
btn.grid(row=3)





# ==========================
janela.mainloop()
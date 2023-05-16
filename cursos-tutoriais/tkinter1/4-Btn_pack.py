from tkinter import *

janela = Tk()
janela.title('title')


janela.geometry('500x250')

# # forma 1
# # desta forma executará  
# def cmd_clik(msg):
#     print('msg')

# btn = Button(janela, text='Executar', command=cmd_clik)
# btn.pack()


# # forma 2
# # desta forma executará sem uso do btn, entao nao funciona como deveria
# def cmd_clik(msg):
#     print(msg)
    
# btn = Button(janela, text='Executar', command=cmd_clik('mensagem'))
# btn.pack()




# forma funcional
def cmd_click(msg):
    print(msg)
    
btn = Button(janela, tet='executar', command=lambda:cmd_click('nova mensagem'))
btn.pack()


# perceba que o tkinter funciona perfeitamente, msm com os botoes tendo o mesmo nome
# resultado do pack(). Depois de feito o pack() do objeto, ele vai funcionar
btn = Button(janela, tet='executar', command=lambda:cmd_click('outra mensagem'))
btn.pack()

janela.mainloop()
from tkinter import *

'''definindo dimençoes e posições na tela do usuario'''

menu_principal = Tk()
menu_principal.title('titulo')

# dimensao da janela
largura = 500
altura = 300

# resolução do sistema
largura_screen = menu_principal.winfo_screenwidth()
altura_screen = menu_principal.winfo_screenheight()

# posição da janela
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# definir geometria
menu_principal.geometry(f'{largura}x{altura}+{posx}+{posy}')


menu_principal.mainloop()


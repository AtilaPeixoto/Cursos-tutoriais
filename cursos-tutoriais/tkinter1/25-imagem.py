from tkinter import *



root = Tk()
root.title('meu outro app')

img = PhotoImage(file='img/atilapeixoto.png',
                 )


# # o tkinter possui um metodo para redimencionamento de img's mas aceita apenas numeros inteiros 
# smal_img = img.subsample(2, 1)

label_img = Label(root, image=img).pack()




root.mainloop()
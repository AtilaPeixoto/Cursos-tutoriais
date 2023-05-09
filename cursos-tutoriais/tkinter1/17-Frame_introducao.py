from tkinter import *




# GUI ==================
root = Tk()
root.title('title')



# Windget ====================

frame_login = Frame(root, )

l_usuario = Label(frame_login, text='Usuario')
l_senha = Label(frame_login, text='Senha')

t_usuario = Entry(frame_login)
t_senha = Entry(frame_login, text='senha')

btn = Button(frame_login, text='Entrar')

#  Layout =======================

l_usuario.grid(row=0)
l_senha.grid(row=1)
t_usuario.grid(row=0, column=1)
t_senha.grid(row=1, column=1)
btn.grid(row=3, columnspan=2,)

t_usuario.focus()

# lembrar de colocar o frame dentro do layout tbm 
frame_login.grid()


root.mainloop()
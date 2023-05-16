from tkinter import *





root = Tk()
root.title('app')

frame_name = Frame(root)
frame_morada = Frame(root)

label_name = Label(frame_name, text='NAME')
label_apelido = Label(frame_name, text='Apelido')
label_rua = Label(frame_morada, text='Rua')
label_cidade = Label(frame_morada, text='Cidade')


text_name = Entry(frame_name)
text_apelido = Entry(frame_name)
text_rua = Entry(frame_morada)
text_cidade = Entry(frame_morada)

btn = Button(root, text='Salvar', )



label_name.grid(row=1, column=0)
label_apelido.grid(row=2, column=0)
label_rua.grid(row=3, column=0)
label_cidade.grid(row=4, column=0)

text_name.grid(row=1, column=1)
text_apelido.grid(row=2, column=1)
text_rua.grid(row=3, column=1)
text_cidade.grid(row=4, column=1)

btn.grid(row=5, column=0)

frame_name.grid(row=0, column=0)
frame_morada.grid(row=0, column=1)



root.mainloop()

from tkinter import *

root = Tk()
root.title('title')

# temos um espaço um gap nas colunas. para resolver isso é possivel usar os metodos columnspan e rowspan
Label(root, width=20, bg='red').grid(column=0)
Label(root, width=20,bg='green').grid(column=1)
Label(root, width=40, bg='yellow').grid(column=0)


# columnnspan estica o numero de colunas, ou no caso row linhas, mas ainda ha uma gap-zinho nas laterais
Label(root, width=20, bg='blue').grid(column=0, sticky='e')
Label(root, width=20,bg='green').grid(column=1)
Label(root, width=40, bg='yellow').grid(columnspan=2)

# resolvemos o gap com o uso da propriedade sticky. Esta recebe as cordenadas 'wesn', podendo ser uma ou mais
Label(root, width=20, bg='blue').grid(column=0, sticky='e')
Label(root, width=20,bg='green').grid(column=1)
Label(root, width=40, bg='yellow').grid(columnspan=2, sticky='we')

root.mainloop()
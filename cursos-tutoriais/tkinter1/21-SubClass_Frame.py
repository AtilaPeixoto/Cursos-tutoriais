from tkinter import *


class FrameNome(Frame):
    def __init__(self, x):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = 'solid'
        
        label = Label(self, text='nome:')
        text = Entry(self, )

        label.grid(row=0, column=0)
        text.grid(column=1, row=0)
        
        
        
        
        
janela = Tk()
janela.title('app')

frame1 = FrameNome(janela)
frame1.grid()


janela.mainloop()

'''suer classe é  frame
sub classe é a criada
oderia ser chamada de devrivada e classe base 
ate mesmo filha e pai/mae etc'''
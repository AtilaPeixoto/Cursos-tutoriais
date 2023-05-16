from tkinter import *

class NovoFrame(Frame):
    def __init__(self, X):
        super().__init__()
        self['height'] = 3
        self['width'] = 2
        self['bd'] = 2
        self['relief'] = 'solid'
    
        self.l_label = StringVar()
        self.t_text = StringVar()
       
        
        self.llebal = Label(self, textvariable=self.l_label).grid()
        self.ttext = Entry(self, textvariable=self.t_text).grid()
        btn = Button(self, text='Executar', command=self.Executar).grid()
        
        # # por alguma razao focus parece nao funcionar. Deve ser uma classe externa ao Frame
        # self.ttext.focus()
        
    def Executar(self):
        self.l_label.set(self.t_text.get())



root = Tk()
root.title('Meu app')
root.geometry('300x200')



subframe = NovoFrame(root).grid()
subframe = NovoFrame(root).grid()










root.mainloop()
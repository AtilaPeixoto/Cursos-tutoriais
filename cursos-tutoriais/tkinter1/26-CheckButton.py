from tkinter import *


root = Tk()
root.title('outro mais um app')

def apresentar():
    print(valor_check.get())


valor_check = IntVar()
check = Checkbutton(root, text='checkBox', 
                    variable=valor_check,
                    command=apresentar,
                    ).pack()




root.mainloop()
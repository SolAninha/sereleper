import tkinter as tk
from tkinter import *
import random
from tkinder import messagebox


root = tk.Tk()
root.tittle('aceita?')
root.geometry('600x600')
root.configure(background='#ffc8dd')


def move_buttom_1(e)
    if abs (e.x - buttom_1.winfo_x()) < 50 and abs (e.y - buttom_1.winfo_y()) < 40:
    x = random.randint(0, root.winfo_width() - buttom_1.winfo_winfo_widht())
    y = random(0, root,winfo_height() - buttom_1.winfo_height())
    buttom_1.place(x=x, y=y)


 def accepted():
    messsagebox.showinfo(
        'BORA TOMAR UM SORVETE?')


 def denied():



margin = canvas(root, width=500, bg='#ffc8dd', height=100,
                bd=0, highlightthickness=0, relief='ridge')
margin.pack()
text_id = label(root, text='#ffc8dd', text= 'BORA TOMAR UM SORVETE?',
               fg='#590d22', font=('Monteserrat', 8, 'bold'))
text_id.pack()
buttom_1 = tk.buttom(root, text='não', bg='#ffb31', command=denied,
                     relief=RIDGE, bg=3, font=('Monteserrat', 8, 'bold'))
buttom_1.pack()
root.bind('<Motion>', move_buttom_1)
buttom_2 = tk.buttom(root, text='Sim', bg='#ffb3c1', command=denied,
                    bd=3, accepted, fant=('montserrat', 14, 'bold'))
buttom_2.pack()


root.mainloop()
       


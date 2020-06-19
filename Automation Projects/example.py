#  ex_mouse.py
#
#  Copyright 2017 tavares <tavares@tavares-Inspiron-5558>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#
#

import  tkinter as  tk
from tkinter import messagebox
from platform import python_version


def main(args):

	root = tk.Tk()
	root.title("www.cadernodelaboratorio.com.br")
	root.geometry("400x400")



	lbl1= tk.Label(root, text="Pressione o mouse e veja o que ocorre", bg="red", fg="white")
	minhaTela = tk.Frame(root)

	lbl1.pack( padx= "10", pady="10")
	minhaTela.pack( padx= "5", pady="5",expand=1, fill="both")


	minhaTela.bind('<Button-1>',mouseBotaoEsquerdoPressionado)
	minhaTela.bind('<Button-2>',mouseBotaoMeioPressionado)
	minhaTela.bind('<Button-3>',mouseBotaoDireitoPressionado)


	tk.mainloop()

	return 0

def mouseBotaoEsquerdoPressionado(event):
	msg= ('Você pressionou o botão esquerdo em %d , %d') % (event.x, event.y)
	messagebox.showinfo("Olá", msg)

def mouseBotaoMeioPressionado(event):
	msg= ('Você pressionou o botão meio em %d , %d') % (event.x, event.y)
	messagebox.showinfo("Olá", msg)


def mouseBotaoDireitoPressionado(event):
	msg= ('Você pressionou o botão direito em %d , %d') % (event.x, event.y)
	messagebox.showinfo("Olá", msg)


if __name__ == '__main__':
    import sys
    print ("Versão Python: ", python_version())   #somente para verificar que estamos no ambiente virtual python 3.5
    sys.exit(main(sys.argv))
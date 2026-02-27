import tkinter as tk
from tkinter import messagebox
def opcion():
    if var.get()==1:
        messagebox.showinfo("Opcion elegida","Te gustan los tacos")
    elif var.get()==2:
        messagebox.showinfo("Opcion elegida","Te gusta la pizza")
    elif var.get()==3:
        messagebox.showinfo("Opcion elegida","Te gustan los esquites")
    elif var.get()==4:
        messagebox.showinfo("Opcion elegida","Te gusta el pozole")   
    else:
        messagebox.showinfo("Opcion elegida","No seleccionaste nada")
         

ven1=tk.Tk()
ven1.title("radio button")
ven1.geometry("300x400")

etiqueta1=tk.Label(ven1,text="uso de radio button")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ven1,text="Tacos",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(ven1,text="pizza",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(ven1,text="Esquites",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(ven1,text="Pozole",variable=var,value=4)
rad4.pack()

boton1=tk.Button(ven1,text="Verificar",command=opcion)
boton1.pack(pady=30)

ven1.mainloop()

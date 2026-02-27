import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var.get()==1:
        messagebox.showinfo("Ventana de informacion","Aca puedes escribir informacion al ususario")
    elif var.get()==2:
        messagebox.showwarning("Ventana de advertencia","Esta es una ADVERTENCIA")
    elif var.get()==3:
        messagebox.showerror("Ventana de error ","Has cometido un ERROR")   
    elif var.get()==4:
        respuesta=messagebox.askyesno("Ventana de opcion","¿Te gusta esta clase?") 
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Mas te vale")
        else: 
            messagebox.showinfo("Ventana de respuesta","Por eso vas a reprobar")
    elif var.get()==5:
        respuesta=messagebox.askokcancel("Ventana de opcion","¿Das tu alma a esta clase?") 
        if respuesta:
            messagebox.showinfo("Ventana de respuesta","Por eso vas a sacar 10")
        else: 
            messagebox.showinfo("Ventana de respuesta","Por eso repruebas")
    else:
         messagebox.showinfo("Ventana de respuesta","No elegiste nada")
         

ven1=tk.Tk()
ven1.title("radio button")
ven1.geometry("300x400")

etiqueta1=tk.Label(ven1,text="uso de radio button")
etiqueta1.pack(pady=20)

var=tk.IntVar()
rad1=tk.Radiobutton(ven1,text="Mostrar informacion",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(ven1,text="Advertencia",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(ven1,text="Error",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(ven1,text="Pregunta Si o No",variable=var,value=4)
rad4.pack()
rad5=tk.Radiobutton(ven1,text="Pregunta aceptar o cancelar",variable=var,value=5)
rad5.pack()


boton1=tk.Button(ven1,text="Verificar",command=ventanas)
boton1.pack(pady=30)

ven1.mainloop()
